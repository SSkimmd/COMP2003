import time
import aiohttp_cors
import aiohttp
import asyncio
import socketio
import python_weather
import sqlite3

from aiohttp import web
from threading import Thread
from datetime import date

#create user object with sid and username/other stuff
#when logging in add to list of active users
#when disconnecting remove from list using sid
#track which user is updating per thread using the path of the new data which is also the username of the user
#get sid of the user by searching the list of active users from the username
#send data back to client

#when initially logging in with new device, check for ip against user connecting to browser
#if ip is the same, allow user to name and modify the new device
#cache it in some way so they dont have to the next time unless the user removes it as a device


class User:
    def __init__(self, username: str = None, location: str = None):
        self.username = username
        self.location = location

        self.db = None
        self.token = None

        self.devices = []
        self.calendar = None

class Device(dict):
    def __init__(self, sid, name):
        dict.__init__(self, sid=sid, name=name)

        self.sid = sid
        self.name = name

class SIOThread:
    def __init__(self):
        self.sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins="*")
        
        self.users = []
        self.SIOFunctions()

        self.app = web.Application()
        self.sio.attach(self.app)


        self.cors = aiohttp_cors.setup(self.app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                    allow_credentials=True,
                    expose_headers="*",
                    allow_headers="*",
                    allow_methods="*",   
                )
        })
        
        self.cors.add(self.app.router.add_post('/login', self.WebLogin))
        self.cors.add(self.app.router.add_post('/register', self.WebRegister))

        self.cors.add(self.app.router.add_post('/user', self.WebGetUser))
        self.cors.add(self.app.router.add_patch('/user', self.WebUpdateUser))

        self.cors.add(self.app.router.add_post('/weather', self.WebGetWeather))

        #192.168.0.19
        print("Server Started")
        web.run_app(self.app, host="192.168.0.20", port=5000, print=None, access_log=None)

    def SIOFunctions(self):
        @self.sio.on('login')
        async def UserLogin(sid, username, password, name):
            server_loop = asyncio.get_event_loop()


            user = await self.GetUser(username['username'])

            if user == None:
                return
            
            db = DBThread(self.sio, user, sid, server_loop).start()
            user.db = db

            device = Device(sid, name['name'])
            user.devices.append(device)

            print(f'Device Added Named: {name["name"]}')

    async def GetUser(self, username):
        for user in self.users:
            if user.username == username:
                return user  
        return None
    
    async def GetByToken(self, token):
        for user in self.users:
            if user.token == token:
                return user
        return None
    
    async def GetAuthenticatedUser(self, data):
        if 'token' not in data:
            return None
    
        token = data['token']
        user = await self.GetByToken(token) 

        if user is None:
            return None
        return user
    
    async def WebUpdateUser(self, data):
        response = await data.json()


        if not response['token']:
            return web.Response(text="No Token In Body")
        
        token = response['token']
        user = await self.GetByToken(token)

        if 'location' in response:
            user.location = response['location']

        return web.Response(text="User Updated Successfully")      

    
    async def WebGetUser(self, data):
        response = await data.json()

        if 'token' not in response:
            return web.Response(text="No Token In Body")
        
        user = await self.GetAuthenticatedUser(response)

        if user is None:
            return web.Response(text="User Doesn't Exist")
        
        return web.json_response(data={
            "devices": user.devices,
            "location": user.location
        })

    async def WebRegister(self, data):
        response = await data.json()

        username = response['username']
        password = response['password']

        if len(username) <= 0 or len(password) <= 0:
            return web.Response(text="Failed To Create Account")
        
        user = User(username)
        user.location = 'Plymouth'

        database = sqlite3.connect("users.db")
        cursor = database.cursor()
        #add user to database
        cursor.execute(f"INSERT INTO Users VALUES ('{username}', '{password}', '{user.location}')")

        database.commit()
        database.close()

        return web.Response(text='Successfully Registered')
       
    async def WebLogin(self, data): 
        response = await data.json()

        if 'username' not in response or 'password' not in response:
            return web.Response(text='Username Or Password Not In Body', status=400)
        
        database = sqlite3.connect("users.db")
        cursor = database.cursor()

        #get user
        user = cursor.execute("SELECT * FROM Users WHERE username = ?", (response['username'],)).fetchone()

        database.close()
        #verify password hash at this point

        if response['password'] != user[1]:
            return web.Response(text='Password Or Username Is Incorrect')

        user = User(username=user[0], location=user[2])
        user.token = 'thiswillberandomsoon'
        self.users.append(user)

        return web.json_response(data={
            "token": user.token
        })
        #check for token
        #if no token, get user based on username and password
        #if token get user based on token
        #add user to user list
    
    async def WebUpdateCalendar(self, data):
        response = await data.json() 

        user = await self.GetAuthenticatedUser(response)

        if user is None:
            return
        
        if 'calendar' not in response:
            return
        
        user.calendar = response['calendar']
    
    async def WebGetWeather(self, data):
        response = await data.json()

        if 'token' not in response:
            return web.Response("No Token In Body", status=400)

        user = await self.GetAuthenticatedUser(response)

        if user is None:
            return web.Response(text="User Doesnt Exist", status=400)

        async with python_weather.Client(unit=python_weather.METRIC) as client:
            weather = await client.get(user.location)
            return web.json_response(data={
                "temperature": weather.current.temperature,
                "kind": str(weather.current.kind),
                "humidity": weather.current.humidity
            })
        
        

class DBThread(Thread):
    def __init__(self, sio, user, sid, server_loop):
        super(DBThread, self).__init__(daemon=True)
        self.sio = sio
        self.user = user
        self.sid = sid
        self.server_loop = server_loop

    def run(self):
        asyncio.run(self.UpdateClient())
        
    async def UpdateClient(self):
        while True:
            WEATHER = await self.GetWeather()
            DATE = await self.GetDate()

            await self.sio.emit("update", {
                "date": DATE,
                "weather": WEATHER
            }, room=self.sid)

            time.sleep(20)
        
    async def GetDate(self):
        newDate = date.today().strftime('%B %d, %Y')
        return newDate

    async def GetWeather(self):
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            weather = await client.get(self.user.location)
            return f'{weather.current.temperature},  {weather.current.description}'
        
    async def GetCalendar(self):
        pass


if __name__ == '__main__':
    SIOThread()