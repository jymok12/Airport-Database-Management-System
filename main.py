import mysql.connector
from tkinter import *
import sys
import csv

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mju765",
    database = "test1database"
    )
mycursor = db.cursor()
query =  "CREATE TABLE IF NOT EXISTS Country (CountryKey Varchar(3),CountryName VARCHAR(255) NOT NULL,GDPpercapita INT NOT NULL,TourismExpend Float NOT NULL,GDPIndustrailRatio INT NOT NULL,population Int not null,PRIMARY KEY(CountryKey));"
mycursor.execute(query)
with open ('countryData.csv') as csv_file:
    csv_file = csv.reader(csv_file,delimiter = ',')
    all_value = []
    for row in csv_file:
        value = (row[0],row[1],row[2],row[3],row[4],row[5])
        all_value.append(value)
query = "insert ignore into country(countrykey,countryname,gdppercapita,tourismexpend,gdpindustrailratio,population) values (%s,%s,%s,%s,%s,%s)"
mycursor.executemany(query,all_value)
db.commit()
query =  "CREATE TABLE IF NOT EXISTS Airport(AirportCode CHAR(4), AirportName VARCHAR(64),CountryID CHAR(2), NSCoordinates float,EWCoordinates float, NearbyPopulation INT, MaximumRunWayLength INT,PRIMARY KEY (AirportCode),FOREIGN KEY (CountryID) REFERENCES Country(CountryKey), CONSTRAINT CHKCoordinates CHECK (NSCoordinates <= 180.0 AND NSCoordinates >=-180.0 AND EWCoordinates <= 180.0 AND EWCoordinates >= -180.0));"
mycursor.execute(query)
with open ('airportdata.csv',encoding = "utf8") as csv_file:
    csv_file = csv.reader(csv_file,delimiter = ',')
    all_value = []
    for row in csv_file:
        value = (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        all_value.append(value)
query = "insert ignore into Airport(AirportCode,AirportName,CountryID,NSCoordinates,EWCoordinates,NearbyPopulation,MaximumRunWayLength) values (%s,%s,%s,%s,%s,%s,%s)"
mycursor.executemany(query,all_value)
db.commit()
query =  "CREATE TABLE IF NOT EXISTS Airplane(ModelName0 VARCHAR(63), Standard1 VARCHAR(20), PaxCap2 VARCHAR(64),Pilots3 INT, Crew4 INT,Turnaround5 INT, Speed6 INT, PlaneRange7 VARCHAR(16),Fuel8 VARCHAR(16), Available9 VARCHAR(16), Delivery10 VARCHAR(16), Runway11 INT, SizeClass12 VARCHAR(16), Conversion13 VARCHAR(16), NoiseRating14 int, PRIMARY KEY (ModelName0));"
mycursor.execute(query)
with open ('Airplanes.csv') as csv_file:
    csv_file = csv.reader(csv_file,delimiter = ',')
    all_value = []
    for row in csv_file:
        value = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
        all_value.append(value)
query = "insert ignore into Airplane(ModelName0, Standard1, PaxCap2,Pilots3,Crew4,Turnaround5,Speed6,PlaneRange7,Fuel8,Available9,Delivery10,Runway11,SizeClass12,Conversion13, noiseRating14) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
mycursor.executemany(query,all_value)
db.commit()
