from functools import partial
from tkinter import *
from dbquery import Dbquery
from greatecirclecaculator import GreatCircle
import time
import random
import functools
import operator
class MoreUiSpace():
    def __init__(self, mycursor, db, CMPT354):
        self.mycursor = mycursor
        self.db = db
        self.CMPT354 = CMPT354
    def pressedExampleButton(self):
        print("exampleButtonPressed")\

    def showButtons(self):
        button = Button(self.CMPT354, text="this is an example button", command=self.pressedExampleButton)
        button.place(x = 0, y= 650)
        button = Button(self.CMPT354, text="Add Flight", command=self.flightSelector)
        button.place(x=400, y=500, height=100, width=100)  # Move the button around
        button = Button(self.CMPT354, text="Delete Airline", command=self.deleteAirline)
        button.place(x=00, y=500, height=100, width=100)  # Move the button around
        button = Button(self.CMPT354, text="Create Random Airline", command=self.createRandomAirline)
        button.place(x=300, y=500, height=100, width=100)  # Move the button around
        button = Button(self.CMPT354, text="View Flights", command=self.viewFlights)
        button.place(x=500, y=500, height=100, width=100)  # Move the button around

        button = Button(self.CMPT354, text="View Countries", command=self.openViewCountries)
        button.place(x=600, y=500, height=100, width=100)  # Move the button around
        button = Button(self.CMPT354, text="Query1 TEST", command=self.openNewWindowForQ1)
        button.place(x=400, y=650, height=50, width=100)
        button = Button(self.CMPT354, text="Query2 TEST", command=self.openNewWindowForQ2)
        button.place(x=500, y=650, height=50, width=100)
        button = Button(self.CMPT354, text="Query4 TEST", command=self.openNewWindowForQ4)
        button.place(x=600, y=650, height=50, width=100)
        # Move the button around

    def doQueryOne(self):
        print("testing query 1: button works")

    def doQueryTwo(self):
        print("testing query 2: button works")

    def doQueryFour(self):
        print("testing query 4: button works")

    def openNewWindowForQ1(self):
        newWindow = Toplevel(self.CMPT354)
        newWindow.geometry("500x500")
        newWindow.title("Query 1")
        label = Label(newWindow, text="Please input the parameters for running this Query")
        label.place(x=120, y=20)
        lowerlimit = Entry(newWindow)
        lowerlimit.place(x=150, y=120)

        label2 = Label(newWindow, text="Lower Limit:")
        label2.place(x=10, y=120)
        upperlimit = Entry(newWindow)
        upperlimit.place(x=150, y=170)

        label3 = Label(newWindow, text="Upper Limit:")
        label3.place(x=10, y=170)
        # limit = Entry(newWindow)
        # limit.place(x=150, y=220)
        # l = limit.get()
        # label4 = Label(newWindow, text="Display Limit (0 for all):")
        # label4.place(x=10, y=220)

        # Weird issues here
        button2 = Button(newWindow, text="Display Results", command = partial(self.q1SQL, upperlimit,lowerlimit,newWindow))
        # The function q1SQL called regardless of whether or not the button is pressed
        button2.place(x=350, y=200, height=50, width=100)

    def q1SQL(self, upper, lower, window):
        ul = upper.get()
        ll = lower.get()
        print("button pressed")
        sql = """SELECT DISTINCT a.AirportCode, r.CodeArrival, r.TouristDemand, r.buisnessdemand
        FROM airport a, Routes r
        WHERE a.AirportCode = r.CodeDeparture AND r.TouristDemand < """ + str(
            ul) + """ AND  r.TouristDemand >""" + str(ll) + """;"""
        print(sql)
        self.mycursor.execute(sql)
        templist = self.mycursor.fetchall()
        listbox = Listbox(window, width=50, height=10, fg="blue")
        # print("listbox applied")
        i = 0
        for row in templist:
            s = ""
            s += str(row[0]) + "  " + str(row[1]) + "  " +  str(row[2]) + "  " + str(row[3])

            listbox.insert(i, s)
            i += 1
        listbox.place(x=50, y=270)

    def openNewWindowForQ2(self):
        newWindow = Toplevel(self.CMPT354)
        newWindow.geometry("500x500")
        newWindow.title("Query 2")
        label = Label(newWindow, text="Please input the parameters for running this Query")
        label.place(x=120, y=20)
        var = 1
        self.Q2SQLD(newWindow)
        check = Checkbutton(newWindow, text='Ascending Order', variable=var, onvalue=0, offvalue=1,
                            command=partial(self.Q2SQLA, newWindow))
        check2 = Checkbutton(newWindow, text='Descending Order', variable=var, onvalue=1, offvalue=0,
                             command=partial(self.Q2SQLD, newWindow))
        check.place(x=150, y=180)
        check2.place(x=150, y=210)

    def Q2SQLA(self, window):
        print("var = 0")
        sql = """SELECT DISTINCT CodeDeparture, CodeArrival, TouristDemand
                       FROM Routes
                       ORDER BY TouristDemand ASC
                       LIMIT 50;"""
        self.mycursor.execute(sql)
        print("execute")
        result = self.mycursor.fetchall()
        print("fetch")
        listbox = Listbox(window, width=50, height=10, fg="blue")
        i = 0
        for row in result:
            s = row[0] + " to " + row[1]
            listbox.insert(i, s)
        listbox.place(x=50, y=270)

    def Q2SQLD(self, window):
        sql = """SELECT DISTINCT CodeDeparture, CodeArrival, TouristDemand
                           FROM Routes
                           ORDER BY TouristDemand DESC
                           LIMIT 50;"""
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        listbox = Listbox(window, width=50, height=10, fg="blue")
        i = 0
        for row in result:
            s = row[0] + " to " + row[1]
            listbox.insert(i, s)
            i += 1
        listbox.place(x=50, y=270)
    def openNewWindowForQ4(self):
        newWindow = Toplevel(self.CMPT354)
        newWindow.geometry("1000x500")
        newWindow.title("Query 4")
        label = Label(newWindow, text="Showing Stats for Airports With Flights")
        label.place(x=120, y=20)
        sql = "drop view if exists a"
        self.mycursor.execute(sql)
        sql1 = """CREATE View A AS SELECT CodeDeparture AS Airport, COUNT(CodeDeparture) AS NumberOfDepartures
        FROM flight
        GROUP BY CodeDeparture  
        ORDER BY COUNT(NumberOfDepartures) DESC;"""
        sql = "drop view if exists b"
        self.mycursor.execute(sql)
        sql2 = """CREATE view B AS SELECT CodeDeparture AS Airport, AVG(TouristDemand) AS AverageDemand
        FROM Routes
        GROUP BY CodeDeparture
        ORDER BY COUNT(CodeDeparture) DESC;"""

        sql3 = """SELECT A.Airport, A.NumberOfDepartures, B.AverageDemand
        FROM A
        INNER JOIN B ON A.Airport = B.Airport;"""
        self.mycursor.execute(sql1)
        self.mycursor.execute(sql2)
        self.mycursor.execute(sql3)
        result = self.mycursor.fetchall();
        listbox = Listbox(newWindow, width=150, height=10, fg="blue")
        i = 0
        for row in result:
            s = "Airport: " + str(row[0]) + " has " + str(row[1]) + " departure(s) and average tourist demand = " + str(row[2])
            listbox.insert(i, s)
        listbox.place(x=50, y=270)

    def checkboxcheck(self):
        print("Checkbox ticked")

    def viewFlights(self):
        newWindow = Toplevel(self.CMPT354)
        newWindow.title("Airlines")
        newWindow.geometry("1000x500")
        label = Label(newWindow, text="Viewing Flights")
        label.place(x=180, y=20)

        listbox = Listbox(newWindow, width=150, height=15, fg="blue")
        sql = "SELECT * FROM flight"
        self.mycursor.execute(sql)
        # get all airlines
        airline = self.mycursor.fetchall()
        i = 0
        for row in airline:
            s = "flightNumber: " + str(row[0]) + " Price: " +str(row[2]) + " LoadFactor: " +str(row[4]) + " AirlineName: " +str(row[5]) + " Airplane Used: " + row[6] + " Departing From: " + row[7] + " Arriving At: " + row[8]
            listbox.insert(i, s)
            i += 1

        listbox.place(x=20, y=80)


    def createRandomAirline(self):
        names = open('names.txt','r')
        text = names.read()
        text = text.split("\n")
        num = random.randrange(4500)
        name = text[num]
        name = name + " Air"
        reputataion = random.randrange(100)
        randnum = random.randint(0,2)
        callsign = name[0:2]
        coststructure = "LOW"
        if randnum == 1:
            coststructure = "LOW"
        if randnum == 2:
            coststructure = "MED"
        if randnum == 0:
            coststructure = "HIGH"
        query = "Insert into airline values ('" + str(name) + "', '" + str(coststructure) + "', '" + str(reputataion) + "', '" + str(callsign) + "')"
        print(query)
        self.mycursor.execute(query)
        self.db.commit()
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
        query = "select count(flight.airlinename) from flight where flight.airlinename = '" +airlinenamefinal + "'"
        query = query.replace("\n", "")
        print(query)
        self.mycursor.execute(query)
        test = self.mycursor.fetchall()
        flightNumber = test[0]
        flightNumber = flightNumber[0]
        print("flightnumber = ")
        flightNumber = int(flightNumber)
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
        print("capacity = ")
        print(capacity)

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
        query = "select c.gdpPercapita+d.gdppercapita from country c, country d, airport a, airport b where a.CountryID = c.CountryKey AND b.CountryID = d.CountryKey AND a.AirportCode ='" + airport1 + "' AND b.airportCode = '" + airport2 +"'"
        query = query.replace("\n", "")
        self.mycursor.execute(query)
        print(query)
        gdp = self.mycursor.fetchall()
        gdp = gdp[0]
        gdp = gdp[0]
        wealthMultipier = gdp/40000
        cost *= wealthMultipier

        loadFactor *= 100
        print("loadfactor = ")
        print(loadFactor)

        if loadFactor > 100:
            loadFactor = 100

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
        sortingbytuple = 0;
        if depth == 0:
            sql = self.getsqlCountry(picked)
            sortingbytuple = 5
        if depth == 1:
            sql = self.getsqlRoute(picked)
            sortingbytuple = 3
        if depth == 2:
            sql = self.getsqlAirline(savedSelection)

        if depth == 3:
            sql = self.getPlaneSelection(savedSelection)

        print(sql)
        self.mycursor.execute(sql)
        # get all airlines
        country = self.mycursor.fetchall()
        country.sort(key=lambda tup: tup[sortingbytuple])
        country.reverse()
        i = 0
        for row in country:

            s = row[0] +  "," +row[1]
            listbox.insert(i, s)
            i += 1
        if depth >= 4:
            button = Button(newWindow, text=" click to submit selections and create flight", command = partial(self.createFlight,savedSelection, newWindow))
            button.place(x = 0, y = 0,width = 500, height = 500)
        if depth <= 4:
            listbox.bind('<Double-1>', partial(self.openSelectorMenuWithEvent, savedSelection, selectingFrom, depth+1, newWindow))

            listbox.place(x=20, y=80)

    def runDeleteQuery(self,newWindow,event):
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection[0])
        query = "delete from airline where airlinename = '"+ picked +"'"
        print(query)
        self.mycursor.execute(query)
        self.db.commit()
        newWindow.destroy()

    def deleteAirline(self):
        newWindow = Toplevel(self.CMPT354)
        newWindow.title("Airlines")
        newWindow.geometry("500x500")
        label = Label(newWindow, text="Select an airline to delete")
        label.place(x=180, y=20)

        listbox = Listbox(newWindow, width=70, height=15, fg="blue")
        sql = "SELECT * FROM airline"
        self.mycursor.execute(sql)
        # get all airlines
        airline = self.mycursor.fetchall()
        i = 0
        for row in airline:
            listbox.insert(i, row[0])
            i += 1

        listbox.place(x=20, y=80)
        # Double click event with mouse
        listbox.bind('<Double-1>', partial(self.runDeleteQuery,newWindow))
    def openViewCountries(self):
        newWindow = Toplevel(self.CMPT354)
        newWindow.title("countries")
        newWindow.geometry("500x500")
        label = Label(newWindow, text="Viewing Countries GDP")
        label.place(x=180, y=20)

        listbox = Listbox(newWindow, width=70, height=15, fg="blue")
        sql = "SELECT * FROM country"
        self.mycursor.execute(sql)
        # get all airlines
        country= self.mycursor.fetchall()
        i = 0
        for row in country:
            s = row[1] + " = " + str(row[2])
            listbox.insert(i, s)
            i += 1

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
        country.sort(key=lambda tup: tup[1])
        i = 0
        for row in country:
            listbox.insert(i, row[1])
            i += 1

        listbox.place(x=20, y=80)
        # Double click event with mouse
        listbox.bind('<Double-1>', partial(self.openSelectorMenuWithEvent,savedSelection,selectingFrom, depth, newWindow))
