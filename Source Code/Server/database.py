import sqlite3
import sys
import asyncio


def init():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE Users (username TEXT, password TEXT, location TEXT)")

    connection.commit()
    connection.close()

def init_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users VALUES ('testusername', 'testpassword', 'Plymouth')")

    connection.commit()
    connection.close()

async def test():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    rows = cursor.execute("SELECT * FROM Users").fetchall()
    print(rows)

    row = cursor.execute("SELECT * FROM Users WHERE username = ?", ('testusername',)).fetchone()
    print(row)

    connection.close()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == '-i':
            init()
        elif sys.argv[1] == '-u':
            init_users()
        elif sys.argv[1] == '-t':
            asyncio.run(test())
        else:
            print("Arguments Not Specified, -i init(), -u init_users(), -t test()")
    else:
        print("Arguments Not Specified, -i init(), -u init_users(), -t test()")