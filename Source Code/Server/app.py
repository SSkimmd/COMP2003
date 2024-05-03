import time
import aiohttp_cors
import aiohttp
import asyncio
import socketio
import python_weather
import sqlite3
from datetime import datetime


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
        print("Server Succesfully Started")
        web.run_app(self.app, host="127.0.0.1", port=5000, print=None, access_log=None)

    def SIOFunctions(self):
        @self.sio.on('login')
        async def UserLogin(sid, username, password, name):
            server_loop = asyncio.get_event_loop()

            username = username['username']
            password = password['password']

            #attempt to login
            user = await self.Login(username, password)

            #if user doesn't exist just return
            if user == None:
                return
            
            #if user exists, create and start device thread
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
    
    async def GetUserFromDatabase(self, username):
        database = sqlite3.connect("users.db")
        cursor = database.cursor()

        #get user
        user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchone()

        database.close()

        return user
    
    async def Logout(self, username):
        user = await self.GetUser(username)
        self.users.remove(user)
    
    async def Login(self, username, password, token = None):
        #check if user is cached
        user = await self.GetUser(username)

        #if user isnt cached check if they're in the database
        if user is None or token is None:
            user = await self.GetUserFromDatabase(username)

            #if user is not in database return none
            if user is None:
                return None

            #check password
            if user[1] != password:
                return None

            dbusername = user[0]
            dblocation = user[2]
            dbtoken = user[3]

            #create user object
            user = User(dbusername, dblocation)

            #get random token from database user
            user.token = dbtoken

            #cache user
            self.users.append(user)

            #if user object generated successfully return it
            return user
        else:
            #if user is cached check token
            if token is not None:
                if user.token != token:
                    return None
                
                return user
            #if token doesn't exist the user has removed it
            else:
                #force logout
                await self.Logout(username)

                #attempt to log back in, hopefully don't go into an infinite loop
                await self.Login(username, password)

    
    async def WebUpdateUser(self, data):
        response = await data.json()

        if 'token' not in response:
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

        #get username and password from body of request
        username = response['username']
        password = response['password']

        #check if password and username have a length more than 0, should be checked at client level first
        if len(username) <= 0 or len(password) <= 0:
            return web.Response(text="Failed To Create Account", status=400)
        
        #create user object
        user = User(username, 'Plymouth')

        #generate random token
        user.token = 'thiswillberandomsoon'

        #open database connection
        database = sqlite3.connect("users.db")
        cursor = database.cursor()

        #add user to database
        cursor.execute(f"INSERT INTO Users VALUES ('{username}', '{password}', '{user.location}', '{user.token}')")

        database.commit()
        database.close()

        return web.Response(text='Successfully Registered')
       
    async def WebLogin(self, data): 
        response = await data.json()

        #ensure correct data is in the body of the request
        if 'username' not in response or 'password' not in response:
            return web.Response(text='Username Or Password Not In Body', status=400)
        

        username = response['username']
        password = response['password']

        user = None

        if 'token' in response:
            token = response['token']
            user = await self.Login(username, password, token)
        else:
            user = await self.Login(username, password)

        #if user still doesn't exist, return error code
        if user is None:
            return web.Response(text="Incorrect Username Or Password", status=400)

        #return token
        return web.json_response(data={
            "token": user.token
        })
    
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
            moon_phase = ''
            for forecast in weather.forecasts:
                moon_phase = forecast.astronomy.moon_phase.emoji
                sunset = forecast.astronomy.sun_set
                sunrise = forecast.astronomy.sun_rise
                break


            count = 0  
            x = 0
            y=0
           
            # Get current time
            current_time = datetime.now()


# Extract the hour from the current time
            current_hour = current_time.hour
            for forecast in weather.forecasts:
                for hourly in forecast.hourly:
                    print (hourly.kind.emoji)
                    count += 1
                    if 0 <= current_hour < 3 and (count == 1 or x == 1):
                        x = 1
                        if y == 1:
                            kind1 = hourly.kind
                            y += 1
                        elif y == 2:
                            kind2 = hourly.kind
                            y += 1
                        elif y == 3:
                            kind3 = hourly.kind
                            y+=1
                        elif y ==4:
                            y+=1
                            kind4 = hourly.kind
                        else:
                            y += 1
                    elif 3 <= current_hour < 6 and (count == 2 or x == 2):
                        x = 2
                        if y == 1:
                            kind1 = hourly.kind
                            y += 1
                        elif y == 2:
                            kind2 = hourly.kind
                            y += 1
                        elif y == 3:
                            y+=1
                            kind3 = hourly.kind
                        elif y ==4:
                            y+=1
                            kind4 = hourly.kind
                        else:
                            y += 1
                    elif 6 <= current_hour < 9 and (count == 3 or x == 3):
                        x = 3
                        if y == 1:
                            kind1 = hourly.kind
                            y += 1
                        elif y == 2:
                            kind2 = hourly.kind
                            y += 1
                        elif y == 3:
                            y+=1
                            kind3 = hourly.kind
                        elif y ==4:
                            y+=1
                            kind4 = hourly.kind
                        else:
                            y += 1
                    elif 9 <= current_hour < 12 and (count == 4 or x == 4):
                        x = 4
                        if y == 1:
                            kind1 = hourly.kind
                            y += 1
                        elif y == 2:
                            kind2 = hourly.kind
                            y += 1
                        elif y == 3:
                            y+=1
                            kind3 = hourly.kind
                        elif y ==4:
                            y+=1
                            kind4 = hourly.kind
                        else:
                            y += 1
                    elif 12 <= current_hour < 15 and (count == 5 or x == 5):
                        x = 5
                        if y == 1:
                            kind1 = hourly.kind
                            y += 1
                        elif y == 2:
                            kind2 = hourly.kind
                            y += 1
                        elif y == 3:
                            y+=1
                            kind3 = hourly.kind
                        elif y ==4:
                            y+=1
                            kind4 = hourly.kind
                        else:
                            y += 1
                    elif 15 <= current_hour < 18 and (count == 6 or x == 6):
                        x = 6
                        print(current_hour,count,x,y)
                        if y == 1:
                            kind1 = hourly.kind
                            y += 1
                            print("yup")
                        elif y == 2:
                            kind2 = hourly.kind
                            y += 1
                            print("yup")
                        elif y == 3:
                            y+=1
                            kind3 = hourly.kind
                            print("yup")
                        elif y ==4:
                            y+=1
                            kind4 = hourly.kind
                            print("yup")
                        else:
                            y += 1
                    elif 18 <= current_hour < 21 and (count == 7 or x == 7):
                        x = 7
                        if y == 1:
                            kind1 = hourly.kind
                            y += 1
                        elif y == 2:
                            kind2 = hourly.kind
                            y += 1
                        elif y == 3:
                            y+=1
                            kind3 = hourly.kind
                        elif y ==4:
                            y+=1
                            kind4 = hourly.kind
                        else:
                            y += 1
                    else:
                        if y == 1:
                            kind1 = hourly.kind
                            y += 1
                        elif y == 2:
                            kind2 = hourly.kind
                            y += 1
                        elif y == 3:
                            y+=1
                            kind3 = hourly.kind
                        elif y ==4:
                            y+=1
                            kind4 = hourly.kind



                    #if hour_time <3:
                    #hourly.kind
                    #print (hour_time)
           


        #next 2 days Today tomorrow day after
            #for hourly in forecast.hourly:
              #  print (hourly)
            #for forecast in weather.forecasts:
              #  print(f"For {forecast.date}: {forecast.kind}")


            #type = weather.current.kind
           # print (type)
            return web.json_response(data={
                "temperature": weather.current.temperature,
                "kind": str(weather.current.kind.emoji),
                "humidity": weather.current.humidity,
                "moon_phase": str(moon_phase),
                "sunrise": str(sunrise),
                "sunset": str(sunset),
                "ultraviolet":str (weather.current.ultraviolet),
                "wind_speed": round((weather.current.wind_speed / 1.60934)),
                "kind1":str(kind1.emoji),
                "kind2":str(kind2.emoji),
                "kind3":str(kind3.emoji),
                "kind4":str(kind4.emoji),
        
        

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