from functools import partial
from tkinter import *
from dbquery import Dbquery
from greatecirclecaculator import GreatCircle
import time
import functools
import operator
class MoreUiSpace():
    def __init__(self, mycursor, db, CMPT354):
        self.mycursor = mycursor
        self.db = db
        self.CMPT354 = CMPT354
    def pressedExampleButton(self):
        print("exampleButtonPressed")
    def showButtons(self):
        button = Button(self.CMPT354, text="this is an example button", command=self.pressedExampleButton)
        button.place(x = 0, y= 650)
        button = Button(self.CMPT354, text="Add Flight", command=self.flightSelector)
        button.place(x=400, y=500, height=100, width=100)  # Move the button around
    def flightSelector(self):
        savedSelection = []
        self.openSelectorMenu(savedSelection,"countries")
    def getsqlCountry(self, picked):
        sql = "SELECT * FROM testairports a, country c where a.CountryID = c.countryKey AND c.countryname = '"+ picked + "'"
        sql = sql.replace("\n", "")
        return(sql)
    def getsqlRoute(self, picked):
        picked = picked.split(",")
        picked = picked[0]
        sql = "SELECT * FROM routes r where r.codedeparture = '" + picked + "'"
        sql = sql.replace("\n", "")
        return(sql)
    def getsqlAirline(self, savedSelection):

        sql = "SELECT * FROM airline"
        return sql
    def getPlaneSelection(self,savedSelection):
        routetext = savedSelection[2]
        routetext = routetext.split(",")
        departure = routetext[0]
        arrival = routetext[1]
        query = "select a.nscoordinates, a.ewcoordinates, b.nscoordinates,b.ewcoordinates from airport a, airport b where a.airportCode = '"+ departure+"' AND b.airportCode = '"+ arrival+"'"
        query = query.replace("\n", "")
        print(query)
        self.mycursor.execute(query)
        coords = self.mycursor.fetchall()
        greatCircle = GreatCircle()
        for row in coords:
            greatCircle.latitude1_degrees = float(row[0])
            greatCircle.latitude2_degrees = float(row[2])
            greatCircle.longitude1_degrees = float(row[1])
            greatCircle.longitude2_degrees = float(row[3])

        greatCircle.calculate()
        dist = greatCircle.distance_kilometres
        dist = dist*0.539957
        query = "Select a.maximumrunwaylength from airport a where a.AirportCode= '" + departure + "'"
        query = query.replace("\n", "")
        self.mycursor.execute(query)
        max1 = self.mycursor.fetchall()
        maxlen = 0
        for row in max1:
            maxlen = row[0]
        print(maxlen)
        query = "Select a.maximumrunwaylength from airport a where a.AirportCode= '" + arrival + "'"
        query = query.replace("\n", "")
        self.mycursor.execute(query)
        max1 = self.mycursor.fetchall()
        maxlen2 = 0
        for row in max1:
            maxlen2 = row[0]
        print(maxlen2)
        minlen = min(maxlen,maxlen2)
        print(maxlen)
        query = "select * from airplane ap where ap.runway11 <= "+str(minlen)+ " AND ap.planerange7 >= " + str(dist)
        savedSelection.append(dist)

        return query
    def createFlight(self, savedSelection,newWindow):
        airlinename = savedSelection[3]
        airlinename =airlinename.split(",")
        airlinenamefinal = airlinename[0]
        airlineType = str(airlinename[1])
        query = "select Max(f.flightNumber) from flight f where f.airlinename = '" +airlinenamefinal + "'"
        query = query.replace("\n", "")
        print(query)
        self.mycursor.execute(query)
        test = self.mycursor.fetchall()
        flightNumber = test[0]
        flightNumber = flightNumber[0]
        print(flightNumber)
        if type(flightNumber) == None.__class__:
            print("is triggering this statement")
            flightNumber = 0

        query = "select callsign from airline where airline.airlinename = '" + airlinenamefinal + "'"
        query = query.replace("\n", "")
        print(query)
        self.mycursor.execute(query)
        callsign = self.mycursor.fetchall()
        callsign = callsign[0]
        callsign = callsign[0]


        flightNumber = str(int(flightNumber)+1)
        flightNumber = flightNumber+callsign
        print("flightnumber: ")
        print(flightNumber)
        takeofftime = time.time()
        cost = 0
        multiplier = 1;
        query = "select reputation from airline where airline.airlinename = '" + airlinenamefinal + "'"
        query = query.replace("\n", "")
        self.mycursor.execute(query)
        reputation = self.mycursor.fetchall()
        reputation = reputation[0]
        reputation = reputation[0]
        reputation = int(reputation)
        if airlineType == "LOW":
            multiplier = 0.8
            cost = 15;
        if airlineType == "MED":
            cost = 35
        if airlineType == "HIGH":
            multiplier = 1.1
            cost = 50
        range = float(savedSelection[4])
        cost = cost+(range/10)*multiplier
        airplane = savedSelection[5]
        airplane = airplane.split(",")
        airplane = airplane[0]
        query = "select * from airplane where airplane.modelname0 = '" + airplane + "'"
        query = query.replace("\n", "")
        self.mycursor.execute(query)
        helpme = self.mycursor.fetchall()
        data = helpme[0]
        speed = data[6]
        capacity = float(data[2])

        cities = str(savedSelection[2])

        airport1 = cities[0:4]
        airport2 = cities[5:9]
        query = "select r.touristDemand+r.buisnessDemand from routes r, airport a, airport b where r.codedeparture = a.AirportCode AND r.codeArrival = b.AirportCode AND a.airportcode = '" + airport1 + "' AND b.airportcode = '"+ airport2+ "'"
        query = query.replace("\n", "")
        self.mycursor.execute(query)
        demand = self.mycursor.fetchall()
        demand = demand[0]
        demand = demand[0]
        reputation = reputation/100
        reputation += 0.3
        demand *= reputation
        loadFactor = capacity/demand
        if loadFactor > 1:
            loadFactor = 1
        landingtime = takeofftime + (range/speed*3600)

        query = "insert ignore into flight values ('" + str(flightNumber) + "', '"+ str(takeofftime) + "', '" + str(cost) + "', '" + str(landingtime) + "', '" + str(loadFactor) +"', '" + str(airlinenamefinal) + "', '" + str(airplane) + "', '" + str(airport1) +"', '" + str(airport2) + "')"
        print(query)
        self.mycursor.execute(query)
        self.db.commit()



        newWindow.destroy()
    def openSelectorMenuWithEvent(self,savedSelection,selectingFrom, depth, newWindow,event):




        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection[0])
        text = selectingFrom.pop()
        savedSelection.append(picked)
        newWindow.title("Select from " + text)
        newWindow.geometry("500x500")


        label = Label(newWindow, text="Select an " + text + " to make a flight in")
        label.place(x=180, y=20)


        print(savedSelection)
        listbox = Listbox(newWindow, width=70, height=15, fg="blue")
        sql = ""
        if depth == 0:
            sql = self.getsqlCountry(picked)
        if depth == 1:
            sql = self.getsqlRoute(picked)
        if depth == 2:
            sql = self.getsqlAirline(savedSelection)
        if depth == 3:
            sql = self.getPlaneSelection(savedSelection)

        print(sql)
        self.mycursor.execute(sql)
        # get all airlines
        country = self.mycursor.fetchall()
        i = 0
        for row in country:
            s = row[0]+ "," + row[1]
            listbox.insert(i, s)
            i += 1
        if depth >= 4:
            button = Button(newWindow, text=" click to submit selections and create flight", command = partial(self.createFlight,savedSelection, newWindow))
            button.place(x = 0, y = 0,width = 500, height = 500)
        if depth <= 4:
            listbox.bind('<Double-1>', partial(self.openSelectorMenuWithEvent, savedSelection, selectingFrom, depth+1, newWindow))

            listbox.place(x=20, y=80)




    def openSelectorMenu(self, savedSelection,selectingFrom):
        depth = 0
        newWindow = Toplevel(self.CMPT354)
        newWindow.title("Select from " + selectingFrom)
        newWindow.geometry("500x500")
        label = Label(newWindow, text="Select an "+ selectingFrom+ " to make a flight in")
        label.place(x=180, y=20)
        selectingFrom = []
        selectingFrom.append("nothing")
        selectingFrom.append("airplane")
        selectingFrom.append("airline")
        selectingFrom.append("route")
        selectingFrom.append("airport")
        listbox = Listbox(newWindow, width=70, height=15, fg="blue")
        sql = "SELECT * FROM Country"
        self.mycursor.execute(sql)
        # get all airlines
        country = self.mycursor.fetchall()
        i = 0
        for row in country:
            listbox.insert(i, row[1])
            i += 1

        listbox.place(x=20, y=80)
        # Double click event with mouse
        listbox.bind('<Double-1>', partial(self.openSelectorMenuWithEvent,savedSelection,selectingFrom, depth, newWindow))
