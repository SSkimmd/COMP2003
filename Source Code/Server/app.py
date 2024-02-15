import time
import aiohttp_cors
import aiohttp
import asyncio
import socketio
import python_weather

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
    def __init__(self, username):
        self.username = username

        self.db = None
        self.token = None

        self.devices = []
        self.location = None

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

        #192.168.0.19
        web.run_app(self.app, host="192.168.0.19", port=5000, print=None, access_log=None)

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

        if not response['token']:
            return web.Response(text="No Token In Body")
    
        
        token = response['token']
        user = await self.GetByToken(token)

        if user is None:
            return web.Response(text="User Doesn't Exist")

        if user.token != token:
            return web.Response(text="Incorrect Token Re-Authenticate")
        
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
        user.token = 'thiswillberandomsoon'
        user.location = 'Plymouth'

        self.users.append(user)

        return web.json_response(data={
            "token": user.token
        })
            
    async def WebLogin(self, data):  
        response = await data.json() 

        username = response['username']  

        user = await self.GetUser(username)

        if user == None:
            return web.Response(text='User Does Not Exist', status=400)
        
        if response['token']:
            if user.token != response['token']:
                return web.Response(text="Incorrect Token, Re-Authenticate")

        return web.json_response(data={
            "token": user.token
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


if __name__ == '__main__':
    SIOThread()