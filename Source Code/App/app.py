import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iotdb-3f12d-default-rtdb.europe-west1.firebasedatabase.app"
})



username = ""
fb = db.reference('')
def Start():
    global username

    os.system("cls")

    username = input("Enter Username: ")
    if fb.child(username).get() is None:
        Start()
    else:
        print("[0] Add Item")
        print("[1] Remove Item")
        print("[2] List Items")
        choice = input("Input: ")

        if choice == "0":
            item = input("Enter New Items Name: ")
            CreateItem(item)
            Start()
            print("Added")

        if choice == "1":
            item = input("Enter Items Name: ")
            Delete(item)
            Start()        
            print("Deleted")

        if choice == "2":
            print(fb.child(username).child('calendar').get())
            input()
            Start()


def CreateItem(name):
    fb.child(username).child('calendar').child(name).set({"name": name, "date": "", "type": ""})

def Delete(name):
    fb.child(username).child('calendar').child(name).delete()


if __name__ == '__main__':
    Start()