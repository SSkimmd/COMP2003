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
    def __init__(self, sid, username):
        self.sid = sid
        self.username = username
        self.db = None

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

        self.resource = self.cors.add(self.app.router.add_resource("/login"))
        self.cors.add(self.resource.add_route("POST", self.Login))

        #192.168.0.19
        web.run_app(self.app, host="192.168.0.19", port=5000, print=None, access_log=None)

    def SIOFunctions(self):
        @self.sio.on('login')
        async def UserLogin(sid, username, password):
            server_loop = asyncio.get_event_loop()

            user = User(sid, username['username'])
            db = DBThread(self.sio, user, server_loop).start()
            user.db = db
            self.users.append(user)

            print(f'User Logged With Username: {username["username"]} And Password: {password["password"]}')
    
    async def GetSID(self, username):
        for user in self.users:
            if username == user.username:
                return user.sid
            
    async def Login(self, data):  
        user = await data.json()   

        id = await self.GetSID(user["username"])

        return web.json_response(data={
            "ID": id
        })


class DBThread(Thread):
    def __init__(self, sio, user, server_loop):
        super(DBThread, self).__init__(daemon=True)
        self.sio = sio
        self.user = user
        self.sid = user.sid
        self.server_loop = server_loop

    def run(self):
        asyncio.run(self.UpdateClient())

    async def UpdateClient(self):
        DATE = await self.GetDate()
        WEATHER = await self.GetWeather()

        await self.sio.emit("update", {
            "date": DATE,
            "weather": WEATHER
        }, room=self.sid)
        
    async def GetDate(self):
        newDate = date.today().strftime('%B %d, %Y')
        return newDate

    async def GetWeather(self):
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            weather = await client.get('en')
            return f'{weather.current.temperature} celcius, {weather.current.description}'


if __name__ == '__main__':
    SIOThread()