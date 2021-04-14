import mysql.connector
import numpy as np
import pandas as pd
from tkinter import *
import sys
import csv
from functools import partial
from dbquery import Dbquery
from init_tables import Init
from UI import UserInterface


db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mju765")
mycursor = db.cursor()
query = "SELECT EXISTS(SELECT 1 FROM information_schema.schemata WHERE schema_name = '354airplaneProject1');"
mycursor.execute(query)
test = mycursor.fetchall()
test = test[0]
test = test[0]
if test == 0:
        query = "create schema if not exists 354airplaneProject1"
        mycursor.execute(query)
        db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="mju765",
                database="354airplaneProject1"
            )
        mycursor = db.cursor()
        
        Init.inittables(db, mycursor)
else:
        db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="mju765",
                database="354airplaneProject1"
        )
        mycursor = db.cursor()

        
ui = UserInterface(mycursor, db)
ui.StartUI()



#Init.fixairplanes(db, mycursor)




