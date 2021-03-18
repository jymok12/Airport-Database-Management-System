# This is a sample Python script.
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mju765",
    database = "354temp"
    )
mycursor = db.cursor()
mycursor.execute("SELECT * FROM Country")
for x in mycursor:
        print(x)

mycursor.execute("SELECT * FROM AirplaneType")
for x in mycursor:
        print(x)

mycursor.execute("SELECT * FROM Airport")
for x in mycursor:
        print(x)

mycursor.execute("SELECT * FROM Route")
for x in mycursor:
        print(x)

mycursor.execute("SELECT * FROM Flight")
for x in mycursor:
        print(x)

print("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
