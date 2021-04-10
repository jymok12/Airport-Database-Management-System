

import csv


class Init:

    @classmethod
    def inittables(cls, db, mycursor):


        query = "CREATE TABLE IF NOT EXISTS Country (CountryKey Varchar(3),CountryName VARCHAR(255) NOT NULL," \
                "GDPpercapita INT NOT NULL,TourismExpend Float NOT NULL,GDPIndustrailRatio float NOT NULL,population " \
                "Int not null,PRIMARY KEY(CountryKey)); "
        mycursor.execute(query)
        with open('countryData.csv') as csv_file:
            csv_file = csv.reader(csv_file, delimiter=',')
            all_value = []
            for row in csv_file:
                value = (row[0], row[1], row[2], row[3], row[4], row[5])
                all_value.append(value)
        query = "insert ignore into country(countrykey,countryname,gdppercapita,tourismexpend,gdpindustrailratio," \
                "population) values (%s,%s,%s,%s,%s,%s) "
        mycursor.executemany(query, all_value)
        db.commit()
        query = "CREATE TABLE IF NOT EXISTS Airport(AirportCode CHAR(4), AirportName VARCHAR(64),CountryID CHAR(2), " \
                "NSCoordinates float,EWCoordinates float, NearbyPopulation INT, MaximumRunWayLength INT,PRIMARY KEY (" \
                "AirportCode),FOREIGN KEY (CountryID) REFERENCES Country(CountryKey), CONSTRAINT CHKCoordinates CHECK " \
                "(NSCoordinates <= 180.0 AND NSCoordinates >=-180.0 AND EWCoordinates <= 180.0 AND EWCoordinates >= " \
                "-180.0)); "
        mycursor.execute(query)
        with open('airportdata.csv', encoding="utf8") as csv_file:
            csv_file = csv.reader(csv_file, delimiter=',')
            all_value = []
            for row in csv_file:
                value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                all_value.append(value)
        query = "insert ignore into Airport(AirportCode,AirportName,CountryID,NSCoordinates,EWCoordinates," \
                "NearbyPopulation,MaximumRunWayLength) values (%s,%s,%s,%s,%s,%s,%s) "
        mycursor.executemany(query, all_value)
        db.commit()
        query = "CREATE TABLE IF NOT EXISTS tempAirplane(ModelName0 VARCHAR(63), Standard1 VARCHAR(20), PaxCap2 VARCHAR(" \
                "64),Pilots3 INT, Crew4 INT,Turnaround5 INT, Speed6 INT, PlaneRange7 VARCHAR(16),Fuel8 VARCHAR(16), " \
                "Available9 VARCHAR(16), Delivery10 VARCHAR(16), Runway11 INT, SizeClass12 VARCHAR(16), Conversion13 " \
                "VARCHAR(16), NoiseRating14 int, PRIMARY KEY (ModelName0)); "
        mycursor.execute(query)
        with open('Airplanes.csv') as csv_file:
            csv_file = csv.reader(csv_file, delimiter=',')
            all_value = []
            for row in csv_file:
                value = (
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                    row[12], row[13], row[14])
                all_value.append(value)
        query = "insert ignore into tempAirplane(ModelName0, Standard1, PaxCap2,Pilots3,Crew4,Turnaround5,Speed6," \
                "PlaneRange7,Fuel8,Available9,Delivery10,Runway11,SizeClass12,Conversion13, noiseRating14) values (" \
                "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        mycursor.executemany(query, all_value)
        db.commit()
        query = "Drop table if exists testAirports;"
        mycursor.execute(query)
        query = "CREATE TABLE IF NOT EXISTS testAirports(AirportCode CHAR(4), AirportName VARCHAR(64),CountryID CHAR(" \
                "2), NSCoordinates float,EWCoordinates float,NearbyPopulation INT, MaximumRunWayLength INT," \
                "PRIMARY KEY (AirportCode),FOREIGN KEY (CountryID) REFERENCES Country(CountryKey)); "
        mycursor.execute(query)
        query = "insert ignore into testairports Select *from airport where NearbyPopulation> 700000;"
        mycursor.execute(query)
        query = "drop table if exists routes;"
        mycursor.execute(query)
        print("reached here")
        query = "CREATE TABLE IF NOT EXISTS Routes(CodeDeparture char(4),CodeArrival char(4),TouristDemand INTEGER," \
                "BuisnessDemand INTEGER,CargoDemand INTEGER,PRIMARY KEY (CodeDeparture, CodeArrival),FOREIGN KEY (" \
                "CodeDeparture) REFERENCES airport(AirportCode),FOREIGN KEY (CodeArrival) REFERENCES airport(" \
                "AirportCode)); "
        mycursor.execute(query)
        query = "insert ignore into routes SELECT DISTINCT a.AirportCode, b.AirportCode," \
                "(c.tourismExpend+d.tourismExpend)*1000/(c.population+d.population)*((" \
                "c.GDPpercapita*a.NearbyPopulation)/1000000000)+(b.NearbyPopulation*d.GDPpercapita)/1000000000, " \
                "(((c.GDPpercapita*d.GDPpercapita)/50000)^2)/1000*(a.NearbyPopulation+b.nearbyPopulation)/150000*(" \
                "c.GDPIndustrailRatio*d.GDPIndustrailRatio), null FROM testairports a, testairports b, country c, " \
                "country d wHERE a.AirportCode <> b.AirportCode AND c.CountryKey = a.CountryID AND d.CountryKey = " \
                "b.CountryID "
        mycursor.execute(query)
        db.commit()

    @classmethod
    def fixairplanes(cls, db, mycursor):
        with open('Airplanes.csv', 'w', newline='\n') as f:
            writer = csv.writer(f)

            query = "CREATE TABLE IF NOT EXISTS Airplane(ModelName0 VARCHAR(63), Standard1 VARCHAR(20), PaxCap2 VARCHAR(" \
                    "64),Pilots3 INT, Crew4 INT,Turnaround5 INT, Speed6 INT, PlaneRange7 VARCHAR(16),Fuel8 VARCHAR(16), " \
                    "Available9 VARCHAR(16), Delivery10 VARCHAR(16), Runway11 INT, SizeClass12 VARCHAR(16), Conversion13 " \
                    "VARCHAR(16), NoiseRating14 int, PRIMARY KEY (ModelName0)); "
            mycursor.execute(query)
            query = "select * from tempairplane"
            mycursor.execute(query)
            for x in mycursor:
                y = ",".join(map(str, x))
                y = y.split(',')
                if ("kg" in y[1]) or ("Cargo" in y[1]):
                    y[1] = "0"
                if ("kg" in y[2]) or ("Cargo" in y[2]) or ((y[1]) == "0"):
                    y[2] = "0"
                if "-" in y[7]:
                    temp = y[7].split('-')
                    y[7] = temp[1]
                if "-" in y[8]:
                    temp = y[8].split('-')
                    y[8] = temp[1]
                if "-" in y[9]:
                    temp = y[9].split('-')
                    y[9] = temp[1]
                if " " in y[9]:
                    temp = y[9].split(' ')
                    y[9] = temp[1]
                if "(" in y[9]:
                    y[9] = y[9].strip("(")
                if ")" in y[9]:
                    y[9] = y[9].strip(")")
                if "/" in y[9]:
                    temp = y[9].split("/")
                    y[9] = temp[2]
                if "-" in y[10]:
                    temp = y[10].split('-')
                    y[10] = temp[1]
                if " " in y[10]:
                    temp = y[10].split(' ')
                    y[10] = temp[1]
                if "(" in y[10]:
                    y[10] = y[10].strip("(")
                if ")" in y[10]:
                    y[10] = y[10].strip(")")
                if "/" in y[10]:
                    temp = y[10].split("/")
                    y[10] = temp[1]
                joined = ','.join(y)
                joined.strip(",")
                print(joined)
                writer.writerow([y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9], y[10], y[11], y[12], y[13], y[14]])





