import aiohttp
from aiohttp import web
import socketio
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from threading import Thread
import asyncio

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iotdb-3f12d-default-rtdb.europe-west1.firebasedatabase.app"
})

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
        self.sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
        
        self.users = []
        self.SIOFunctions()

        self.app = web.Application()
        self.sio.attach(self.app)
        web.run_app(self.app, host="192.168.0.34", port=5000, print=None, access_log=None)

    def SIOFunctions(self):
        @self.sio.on('login')
        async def login(sid, username, password):
            server_loop = asyncio.get_event_loop()

            user = User(sid, username['username'])
            db = DBThread(self.sio, user, server_loop).start()
            user.db = db
            self.users.append(user)

            print("User Connected With Username: " + user.username)

        @self.sio.on('text')
        async def text(sid, data):
            print(data)
    
    async def GetUser(self, sid):
        for user in self.users:
            if user.sid == sid:
                return user


class DBThread(Thread):
    def __init__(self, sio, user, server_loop):
        super(DBThread, self).__init__(daemon=True)
        self.sio = sio
        self.user = user
        self.sid = user.sid
        self.server_loop = server_loop

    def run(self):
        self.HandleLogin()
        
    def HandleLogin(self):
        username = self.user.username
        fb = db.reference('')

        stream = None
        if(fb.child(username).get() is not None):
            stream = fb.child(username).listen(self.OnDatabaseUpdate)
        else:
            fb.child(username).set({
                "calendar":[
                    {"name": "test1"},
                    {"name": "test2"}
                ]
            })
            stream = asyncio.get_event_loop().create_task(fb.child(username).listen(self.OnDatabaseUpdate))

    def OnDatabaseUpdate(self, message):
        async def send():
            await self.sio.emit(message.data, '', room=self.sid)
        asyncio.run_coroutine_threadsafe(send(), self.server_loop).result()















#@sio.event
#def connect(sid, environ):
#    print('connect ', sid)
#
#@sio.event
#def text(sid, data):
#    print(data)
#
#@sio.event
#def login(sid, username, password):
#    print()
#
#@sio.event
#def disconnect(sid):
#    print('disconnect ', sid)

if __name__ == '__main__':
    SIOThread()