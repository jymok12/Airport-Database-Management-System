import mysql.connector
import numpy as np
import pandas as pd
from tkinter import *
import sys
import csv
from functools import partial
import sqlite3
from init_tables import Init
from UI import UserInterface


db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mju765")
mycursor = db.cursor()
query = "create schema if not exists 354airplaneProject1"
mycursor.execute(query)
db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mju765",
        database="354airplaneProject1"
    )
mycursor = db.cursor()
print("test")
Init.inittables(db, mycursor)
ui = UserInterface(mycursor, db)
ui.StartUI()


#Init.fixairplanes(db, mycursor)




