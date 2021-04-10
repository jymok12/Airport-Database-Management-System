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
        passwd="mju765",
        database="354airplaneProject1"
    )
mycursor = db.cursor()

ui = UserInterface(mycursor)
ui.StartUI()
#Init.inittables(db, mycursor)
#Init.fixairplanes(db, mycursor)




