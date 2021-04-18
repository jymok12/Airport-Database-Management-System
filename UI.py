from functools import partial
from tkinter import *
from dbquery import Dbquery
from moreui import MoreUiSpace
from greatecirclecaculator import GreatCircle
class UserInterface:

    def __init__(self, mycursor, db):
        self.CMPT354 = Tk()  # Name of root
        self.CMPT354.geometry("750x750")
        self.yLabel = 50  # Inside airportDisplays
        self.Title = Label(self.CMPT354, text="Welcome to the Airplane Project!", fg="red", font="24")
        self.Title.place(x=250, y=0)
        self.mycursor = mycursor
        self.numFeatures = 0;
        self.userText = ""
        self.userText2 = ""
        self.db = db
        self.extraUISpace = MoreUiSpace(self.mycursor,self.db,self.CMPT354)

    def displayCode(self,airport, airportDetailWindow):
        sql = "SELECT AirportCode From Airport Where AirportName LIKE " + '"' + airport + '"'
        self.mycursor.execute(sql)
        code = self.mycursor.fetchall()
        codeLabel = Label(airportDetailWindow, text=code[0])
        textLabel = Label(airportDetailWindow, text="AirportCode: ")
        textLabel.place(x=0, y=50)  # Inc by 30 for each y
        codeLabel.place(x=75, y=50)

    def displayCountry(self, airport, airportDetailWindow):
        # print(airport)
        sql = "SELECT CountryName FROM country, airport WHERE AirportName LIKE " + '"' + airport + '"' + " AND CountryID = CountryKey "
        # print(sql)
        self.mycursor.execute(sql)
        # print(mycursor)
        country = self.mycursor.fetchall()
        # print(country)
        countyLabel = Label(airportDetailWindow, text=country[0])
        textLabel = Label(airportDetailWindow, text="Country: ")
        textLabel.place(x=0, y=80)
        countyLabel.place(x=55, y=80)  # Needs to be 55+ for Country

    def displayLocation(self,airport, airportDetailWindow):
        sql = "SELECT NSCoordinates From Airport Where AirportName LIKE " + '"' + airport + '"'
        self.mycursor.execute(sql)
        NS = self.mycursor.fetchall()
        NSLabel = Label(airportDetailWindow, text=NS[0])
        textLabel = Label(airportDetailWindow, text="(NS) Latitude: ")
        textLabel.place(x=0, y=110)
        NSLabel.place(x=80, y=110)

        sql = "SELECT EWCoordinates From Airport Where AirportName LIKE " + '"' + airport + '"'
        self.mycursor.execute(sql)
        EW = self.mycursor.fetchall()
        EWLabel = Label(airportDetailWindow, text=EW[0])
        textLabel = Label(airportDetailWindow, text="(EW) Longitude: ")
        textLabel.place(x=0, y=140)
        EWLabel.place(x=90, y=140)

    def displayNearbyPopulation(self,airport, airportDetailWindow):
        sql = "SELECT NearbyPopulation From Airport Where AirportName LIKE " + '"' + airport + '"'
        self.mycursor.execute(sql)
        nearbyPopulation = self.mycursor.fetchall()
        nearbyPopulationLabel = Label(airportDetailWindow, text=nearbyPopulation[0])
        textLabel = Label(airportDetailWindow, text="Nearby population: ")
        textLabel.place(x=0, y=170)
        nearbyPopulationLabel.place(x=110, y=170)

    def displayMaximumRunWayLength(self,airport, airportDetailWindow):
        sql = "SELECT MaximumRunWayLength From Airport Where AirportName LIKE " + '"' + airport + '"'
        self.mycursor.execute(sql)
        maximumRunWayLength = self.mycursor.fetchall()
        maximumRunWayLengthLabel = Label(airportDetailWindow, text=maximumRunWayLength[0])
        textLabel = Label(airportDetailWindow, text="MaximumRunWayLength(m): ")
        textLabel.place(x=0, y=200)
        maximumRunWayLengthLabel.place(x=165, y=200)

    def displayGDPPerCapita(self,airport, airportDetailWindow):
        sql = "SELECT GDPpercapita From Airport , country Where CountryId = CountryKey AND AirportName LIKE " + '"' + airport + '"'
        self.mycursor.execute(sql)
        GDPpercapita = self.mycursor.fetchall()
        GDPpercapitaLabel = Label(airportDetailWindow, text=GDPpercapita[0])
        textLabel = Label(airportDetailWindow, text="Country GDP Per Capita: ")
        textLabel.place(x=0, y=240)
        GDPpercapitaLabel.place(x=135, y=240)

    def displayTourism(self,airport, airportDetailWindow):
        sql = "SELECT TourismExpend From Airport , country Where CountryId = CountryKey AND AirportName LIKE " + '"' + airport + '"'
        self.mycursor.execute(sql)
        TourismExpend = self.mycursor.fetchall()
        TourismExpendLabel = Label(airportDetailWindow, text=TourismExpend[0])
        textLabel = Label(airportDetailWindow, text="Country Tourism Expenditure: ")
        textLabel.place(x=0, y=270)
        TourismExpendLabel.place(x=165, y=270)

    def displayGDPIndurtialRatio(self,airport, airportDetailWindow):
        sql = "SELECT GDPIndustrailRatio From Airport , country Where CountryId = CountryKey AND AirportName LIKE " + '"' + airport + '"'
        self.mycursor.execute(sql)
        GDPIndustrialRatio = self.mycursor.fetchall()
        GDPIndustrialRatioLabel = Label(airportDetailWindow, text=GDPIndustrialRatio[0])
        textLabel = Label(airportDetailWindow, text="Country GDP Industrial ratio: ")
        textLabel.place(x=0, y=300)
        GDPIndustrialRatioLabel.place(x=160, y=300)

    def displayPopulation(self,airport, airportDetailWindow):
        sql = "SELECT population From Airport , country Where CountryId = CountryKey AND AirportName LIKE " + '"' + airport + '"'
        self.mycursor.execute(sql)
        population = self.mycursor.fetchall()
        populationLabel = Label(airportDetailWindow, text=population[0])
        textLabel = Label(airportDetailWindow, text="Country population: ")
        textLabel.place(x=0, y=330)
        populationLabel.place(x=115, y=330)

    def airportDetails(self,event):
        print("hi")
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection[0])
        airportDetailWindow = Toplevel(self.CMPT354)
        airportDetailWindow.title("Airport Detail window")
        airportDetailWindow.geometry("500x500")
        Label(airportDetailWindow, text=picked).pack()
        self.displayCode(picked, airportDetailWindow)

        # Get CountryName
        self.displayCountry(picked, airportDetailWindow)

        # Get Location (GPS Cords)
        self.displayLocation(picked, airportDetailWindow)

        # Get NearbyPopulation
        self.displayNearbyPopulation(picked, airportDetailWindow)

        # Get MaximumRunWayLength
        self.displayMaximumRunWayLength(picked, airportDetailWindow)

        # Get GDPPerCapita
        self.displayGDPPerCapita(picked, airportDetailWindow)

        # Get TourismExpend
        self.displayTourism(picked, airportDetailWindow)

        # Get GDPIndustrialRatio
        self.displayGDPIndurtialRatio(picked, airportDetailWindow)

        # Get Population
        self.displayPopulation(picked, airportDetailWindow)

    def listBoxCreate(self):
        # Create frame and scrollbar and listbox
        my_frame = Frame(self.CMPT354)
        scrollbar = Scrollbar(my_frame, orient=VERTICAL)
        label = Label(text="Select an airport to view more detail")
        label.place(x=270, y=30)
        listbox = Listbox(my_frame, width=120, height=20, fg="blue", yscrollcommand=scrollbar)

        sql = "SELECT * FROM airport"
        self.mycursor.execute(sql)
        # get all airports
        airports = self.mycursor.fetchall()
        airports.sort(key=lambda tup: tup[5])
        airports.reverse()
        i = 0

        for row in airports:
            listbox.insert(i, row[1])
            i += 1
        print("Airport amount = ", i)

        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        my_frame.pack()

        listbox.pack(pady=10)
        my_frame.place(x=0, y=50)

        # Double click event with mouse
        listbox.bind('<Double-1>', self.airportDetails)
        listbox.pack()

    def otherFeaturesLabel(self):
        label = Label(text="Other features")
        label.place(x=300, y=390)
    def updateRoutes(self):
        self.mycursor.execute(Dbquery.updateRoutesQuery())
        self.db.commit()
        self.mycursor.execute(Dbquery.updateRoutesBuisnessQuery())
        self.db.commit()
        self.mycursor.execute(Dbquery.updateRoutesDomesticModifierTourism())
        self.db.commit()
        self.mycursor.execute(Dbquery.updateRoutesDomesticBusiness())
        self.db.commit()
        self.updateFlight()
    def runCountryGDPquery(self,editgdpMenu):
        print("usertext1 = " + self.userText)
        print("usertext2 = " + self.userText2)

        query = 'Update country set gdpPercapita = '
        query+=self.userText
        query+=" where countryname = '"
        query+=self.userText2
        query+="'"
        query = query.replace("\n","")

        print("running query: " + query)
        self.mycursor.execute(query)
        self.db.commit()
        self.updateRoutes()
        editgdpMenu.destroy()
    def editCountryGdp(self):
        editgdpMenu = Tk()
        editgdpMenu.geometry("400x400")

        titleLabel = Label(editgdpMenu, text="This section takes a number and a valid country " \
                                              "\n and sets the GDP amount amount to selected country")
        titleLabel.place(x=25, y=0)

        inputLabelGDP = Label(editgdpMenu, text = "Please enter a GDP number value:")
        inputLabelGDP.place(x = 0 , y =75)
        textFieldGDP = Text(editgdpMenu, height = 1, width = 15)
        textFieldGDP.place(x = 0 , y = 100)
        submitButtonNum = Button(editgdpMenu, text="Save GDP value",
                                 command=partial(self.saveTextSelection, textFieldGDP, editgdpMenu))
        submitButtonNum.place(x=0, y=125)

        inputLabelCountry = Label(editgdpMenu, text="Please enter a valid country:")
        inputLabelCountry.place(x=0, y=225)
        textFieldCountry = Text(editgdpMenu, height=1, width=15)
        textFieldCountry.place(x=0, y=250)
        submitButton = Button(editgdpMenu, text="Save country selection",
                              command=partial(self.saveTextSelection2, textFieldCountry, editgdpMenu))
        submitButton.place(x=0, y=275)



        runButton = Button(editgdpMenu, text="Run query with selected data",
                           command=partial(self.runCountryGDPquery, editgdpMenu))
        runButton.place(x=0, y=350)
        editgdpMenu.mainloop()

    def updateairlineinfo(self):
        newWindow = Toplevel(self.CMPT354)
        newWindow.title("Update Reputation Data by double clicking an airline")
        newWindow.geometry("500x500")
        label = Label(newWindow, text="Select an airline to change its reputation")
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
        listbox.bind('<Double-1>', self.AirlineRepUpdate)

    def AirlineRepUpdate(self, event):
        widget = event.widget
        selection = widget.curselection()
        newWindow = Toplevel(self.CMPT354)
        newWindow.geometry("500x500")
        airline = widget.get(selection[0])
        newWindow.title("Update Reputation Data for " + airline)
        newRep = Entry(newWindow)
        newRep.place(x=250, y=170)
        label = Label(newWindow, text="Input the new Reputation for " + airline)
        label.place(x=10, y=170)
        print(newRep)
        button2 = Button(newWindow, text="Display Results",
                         command=partial(self.RepUpdateSQL, newRep, newWindow, airline))
        button2.place(x=350, y=200, height=50, width=100)
    def RepUpdateSQL(self,newRep,window,airline):
        newRep1 = newRep.get()
        sql = """UPDATE airline
                 SET Reputation = """+ str(newRep1) +"""
                WHERE AirlineName = '"""+ airline +"""' ;"""
        print(sql)
        self.mycursor.execute(sql)
        label = Label(window, text= airline + "'s reputation has been updated!")
        label.place(x=10, y=370)
        self.updateFlight()

    def AirportRouteDetails(self,event):
        newWindow = Toplevel(self.CMPT354)
        newWindow.title("Route Details")
        newWindow.geometry("750x500")
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection[0])
        print(picked)
        my_Frame = Frame(newWindow)
        scrollbar = Scrollbar(my_Frame, orient=VERTICAL)
        label = Label(newWindow, text="Routes From Airport: " + picked + '\n' + "To: ")
        label.place(x=180, y=20)

        listbox = Listbox(my_Frame, width=115, height=15, fg="blue", yscrollcommand = scrollbar)

        sql = "Select a.airportCode, b.airportCode, r.touristDemand, r.BuisnessDemand, b.airportname from airport a, " \
              "routes r, airport b Where r.codedeparture = a.airportCode AND a.airportName = '"+picked+"' " \
                                                                                "AND b.airportcode = r.codeArrival; "
        print(sql)
        self.mycursor.execute(sql)
        # get all airlines
        airport = self.mycursor.fetchall()
        airport.sort(key=lambda tup: tup[2])
        airport.reverse()
        i = 0
        for row in airport:

            s = row[0]+"-"+row[1]+", Tourist Demand =  "+str(row[2])+ ", Business Demand = "+ str(row[3])
            listbox.insert(i, s)
            i += 1

        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        my_Frame.pack()
        listbox.pack(pady = 10)
        my_Frame.place(x = 20, y = 80)
        listbox.pack()
    def openRoutesFromAirportWindow(self):
        newWindow = Toplevel(self.CMPT354)
        newWindow.title("Select Airport")
        newWindow.geometry("500x500")

        my_frame = Frame(newWindow)
        scrollbar = Scrollbar(my_frame, orient=VERTICAL)
        label = Label(newWindow, text="Select an airport to view routes:" + "\n" + "These airports have a nearby population \n greater that 1,000,000")
        label.place(x=140, y=20)

        listbox = Listbox(my_frame, width=70, height=15, fg="blue", yscrollcommand = scrollbar)
        sql = "SELECT * FROM airport"
        print(sql)
        self.mycursor.execute(sql)
        airport= self.mycursor.fetchall()
        airport.sort(key=lambda tup: tup[5])
        airport.reverse()
        i = 0
        for row in airport:
            if row[5] > 1000000:
                listbox.insert(i, row[1])
                i += 1

        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        my_frame.pack()

        listbox.pack(pady = 10)
        my_frame.place(x=20, y=80)

        # Double click event with mouse
        listbox.bind('<Double-1>', self.AirportRouteDetails)
        listbox.pack()

    def displayFeatureButtons(self):
        openTextWindowButton = Button(self.CMPT354, text="Edit \n Airport population", command=self.editAirportPopulation)
        openTextWindowButton.place(x=0, y=425, height = 50, width = 125)
        openEditSomeButton = Button(self.CMPT354, text="Edit \n Airports in Country", command=self.editAirportsInCountry)
        openEditSomeButton.place(x = 140, y = 425, height = 50, width = 125)
        openCountryEditMenu = Button(self.CMPT354, text= "Edit \n CountryGDP", command = self.editCountryGdp)
        openCountryEditMenu.place(x = 280, y=425, height = 50, width = 125)

        button = Button(self.CMPT354, text="Airlines", command=self.openAirLineNewWindow)
        button.place(x=100, y=500, height=100, width=100)  # Move the button around
        button = Button(self.CMPT354, text="Routes", command=self.openRoutesFromAirportWindow)
        button.place(x=200, y=500, height=100, width=100)  # Move the button around
        button = Button(self.CMPT354, text="Update Reputation", command=self.updateairlineinfo)
        button.place(x=420, y=425, height=50, width=100)  # Move the button around
        button = Button(self.CMPT354, text="Update Prices", command=self.updateFlightPrices)
        button.place(x=500, y=600, height=50, width=100)  # Move the button around

        self.extraUISpace.showButtons()
    def updateFlightPrices(self):

        newWindow = Toplevel(self.CMPT354)
        newWindow.title("Select a flight")
        newWindow.geometry("500x500")
        label = Label(newWindow, text="Select a flight to modify the price in")
        label.place(x=180, y=20)


        listbox = Listbox(newWindow, width=70, height=15, fg="blue")
        sql = "SELECT * FROM Flight"
        self.mycursor.execute(sql)
        # get all airlines

        country = self.mycursor.fetchall()
        country.sort(key=lambda tup: tup[1])
        i = 0
        for row in country:
            s = row[0] + "," + row[5]
            listbox.insert(i, s)
            i += 1

        listbox.place(x=20, y=80)

        # Double click event with mouse
        listbox.bind('<Double-1>',
                     partial(self.openPriceInsertMenu))
    def openPriceInsertMenu(self,event):
        widget = event.widget
        selection = widget.curselection()
        newWindow = Toplevel(self.CMPT354)
        newWindow.geometry("500x500")
        data = widget.get(selection)
        data = data.split(",")
        airline = data[1]
        airline.strip()
        flightNumber = data[0]
        newWindow.title("Update")
        newPrice = Entry(newWindow)
        newPrice.place(x=250, y=170)
        label = Label(newWindow, text="Input the new price for the route")
        label.place(x=10, y=170)
        print(newPrice)
        button2 = Button(newWindow, text="Display Results",
                         command=partial(self.priceUpdateSql, newPrice, newWindow, airline, flightNumber))
        button2.place(x=350, y=200, height=50, width=100)

    def priceUpdateSql(self, newPrice, window, airline, flightNumber):
        newPrice = newPrice.get()
        sql = """UPDATE flight
                 SET flight.price = """ + str(newPrice) + """
                WHERE flight.AirlineName = '""" + airline + """' AND flight.flightnumber = '""" + flightNumber + "'"
        print(sql)
        self.mycursor.execute(sql)
        label = Label(window, text="Price has been updated!")
        label.place(x=10, y=370)
        self.updateFlight()

    def openGetTextMenu(self):
        print("pressed")
    def saveTextSelection(self,textfield,theRoottk):
        self.userText = ""
        text = textfield.get("1.0",END)
        if text == '\n': #Get rid of empty
            text = "1"
        label = Label(theRoottk,text="Multiplier: " + text)
        label.place(x = 0, y = 175)
        self.userText = text
        print(text)
    def saveTextSelection2(self,textfield,theRoottk):
        self.userText2 = ""
        text = textfield.get("1.0",END)
        label = Label(theRoottk,text="Country:" + text)
        label.place(x = 0, y = 305)
        self.userText2 = text
        print(text)

    def runQuery(self, inmenu):
        query = "UPDATE airport SET nearbyPopulation = nearbyPopulation *" + self.userText + " where AirportCode = airportCode;"
        print(query)
        self.mycursor.execute(query)
        self.db.commit()

        self.userText = ""
        self.updateRoutes()

        label = Label(inmenu, text= "Success")
        label.place(x=0, y=250)
        inmenu.destroy()
    def runQuerySome(self, inmenu):
        print("usertext1 = "+ self.userText)
        print("usertext2 = " + self.userText2)

        query = "UPDATE airport a, country c SET a.nearbyPopulation = a.nearbyPopulation*"+ self.userText+ " where a.AirportCode = a.airportCode AND  a.countryId = c.countryKey AND c.countryName = '"+ self.userText2+"' ;"
        query = query.replace("\n", "")
        print(query)
        self.mycursor.execute(query)
        self.db.commit()
        self.updateRoutes()
        inmenu.destroy()
        self.userText = ""
        self.userText2 = ""
    def editAirportPopulation(self):
        editAllMenu = Tk()
        editAllMenu.geometry("400x400")

        titleLabel = Label(editAllMenu,text = "This section takes a number \n and multiplies the nearby population of the airport " \
                                              "by an \n input number")
        titleLabel.place(x = 50, y = 0)

        inputLabel = Label(editAllMenu, text = "Please enter a number:")
        inputLabel.place(x= 0, y = 75)
        textField = Text(editAllMenu,height = 1, width = 15)
        textField.place(x=0, y=100)
        submitButton = Button(editAllMenu, text="Save text selection", command=partial(self.saveTextSelection3,textField,editAllMenu))
        submitButton.place(x=0, y=125)

        runButton = Button(editAllMenu, text="Run query with selected data",command=partial(self.runQuery, editAllMenu))
        runButton.place(x=0,y= 220)
        editAllMenu.mainloop()

    def editAirportsInCountry(self):
        editSomeMenu = Tk()
        editSomeMenu.geometry("400x400")

        titleLabel = Label(editSomeMenu, text= "This section takes a number and a valid country " \
                                                "\n and multiplies the nearby population of the all airports in country")
        titleLabel.place(x=25, y=0)

        inputLabelMultipler = Label(editSomeMenu, text="Please enter a number:")
        inputLabelMultipler.place(x=0, y=75)
        textFieldNumber = Text(editSomeMenu, height=1, width=15)
        textFieldNumber.place(x=0, y=100)
        submitButtonNum = Button(editSomeMenu, text="Save multiplier selection",
                              command=partial(self.saveTextSelection, textFieldNumber, editSomeMenu))
        submitButtonNum.place(x=0, y=125)


        inputLabelCountry = Label(editSomeMenu, text="Please enter a valid country:")
        inputLabelCountry.place(x=0, y=225)
        textFieldCountry = Text(editSomeMenu, height=1, width=15)
        textFieldCountry.place(x=0, y=250)
        submitButton = Button(editSomeMenu, text="Save country selection",
                              command=partial(self.saveTextSelection2, textFieldCountry, editSomeMenu))
        submitButton.place(x=0, y=275)

        runButton = Button(editSomeMenu, text="Run query with selected data",
                           command=partial(self.runQuerySome, editSomeMenu))
        runButton.place(x=0, y=350)
        editSomeMenu.mainloop()

    def saveTextSelection3(self, textfield, theRoottk):
        self.userText = ""
        text = textfield.get("1.0", END)
        if text == '\n':  # Get rid of empty
            text = "1"
        if text[0:1] == '-':
            text = text[1:len(text)]
            print(text + " is text")
        label = Label(theRoottk, text="Multiplier: " + text)
        label.place(x=0, y=175)
        self.userText = text
        print(text)
    def displayBaseOfOperation(self, airline, detailWindow):
        my_frame = Frame(detailWindow)
        scrollbar = Scrollbar(my_frame, orient=VERTICAL)
        label = Label(detailWindow, text="Airports that Airline operates in:")
        label.place(x=10, y=30)
        listbox = Listbox(my_frame, width=75, height=10, fg="blue", yscrollcommand=scrollbar)
        airline = airline.split(",")
        airline = airline[0]

        print("display this")
        sql = "Select distinct a.airportName from airport a where a.airportCode in (Select distinct f.CodeDeparture " \
              "from flight f where f.AirlineName = '"+airline+"') union all Select distinct a.airportName from " \
                                                              "airport a where a.airportCode in (Select distinct " \
                                                              "f.codearrival from flight f where f.AirlineName = " \
                                                              "'"+airline+"') "
        print(sql)
        self.mycursor.execute(sql)
        airport = self.mycursor.fetchall()

        i = 0
        for row2 in airport:
            listbox.insert(i, row2[0])
            i += 1

        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        my_frame.pack()

        listbox.pack(pady=10)
        my_frame.place(x=10, y=40)
    def updateFlight(self):
        self.mycursor.execute("select * from flight")
        flightdata = self.mycursor.fetchall()
        print(flightdata)
        for row in flightdata:
            airline = row[5]

            price = row[2]


            departure = row[7]

            arrival = row[8]
            flightNumber = row[0]
            print(airline)
            self.mycursor.execute("select reputation from airline where airline.airlinename = '" + airline + "'")
            reputation = self.mycursor.fetchall()
            reputation = reputation[0]
            reputation = reputation[0]


            self.mycursor.execute( "select r.touristDemand+r.buisnessDemand from routes r, airport a, airport b where r.codedeparture = a.AirportCode AND r.codeArrival = b.AirportCode AND a.airportcode = '" + departure + "' AND b.airportcode = '"+ arrival+ "'")

            demand = self.mycursor.fetchall()
            demand = demand[0]
            demand = demand[0]
            print("demand = ")
            print(demand)



            airplaneUsed = row[6]

            query = "select * from airplane where airplane.modelname0 = '" + airplaneUsed + "'"
            self.mycursor.execute(query)
            helpme = self.mycursor.fetchall()
            data = helpme[0]
            capacity = float(data[2])

            query = "select a.nscoordinates, a.ewcoordinates, b.nscoordinates,b.ewcoordinates from airport a, airport b where a.airportCode = '" + departure + "' AND b.airportCode = '" + arrival + "'"
            query = query.replace("\n", "")
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
            dist = dist * 0.539957
            basecost = 35
            basecost = basecost + (dist / 10)
            reputation = reputation / 100
            reputation += 0.3
            print("reputation = ")
            print(reputation)
            demand *= reputation
            pricefactor = price/ basecost
            print("demand = ")
            print(demand)
            print("capacity = ")
            print(capacity)
            loadFactor = demand / (capacity + 1)
            print("loadfactor = ")
            print(loadFactor)
            loadFactor /= pricefactor
            print("loadfactor = ")
            print(loadFactor)
            loadFactor *= 100

            print("demand = ")
            print(demand)

            if loadFactor > 100:
                loadFactor = 100
            print("loadfactor = ")
            print(loadFactor)
            query = "update flight set flight.loadfactor = " + str(loadFactor) + " where flight.airlinename  = '"+ airline +"' AND flight.flightNumber = '"+ flightNumber+ "'"
            print(query)
            self.mycursor.execute(query)
            self.db.commit()
    def displayAirplaneOperation(self, airline, detailWindow):

        my_frame = Frame(detailWindow)
        scrollbar = Scrollbar(my_frame, orient=VERTICAL)
        label = Label(detailWindow, text="Airplanes Operated: ")
        label.place(x=10, y=250)
        listbox = Listbox(my_frame, width=75, height=10, fg="blue", yscrollcommand=scrollbar)
        airline = airline.split(",")
        airline = airline[0]

        sql = "Select distinct f.airplanemodeltype from flight f where f.AirlineName = '" + airline + "'"

        print(sql)
        self.mycursor.execute(sql)
        # get all airplanes
        airports = self.mycursor.fetchall()
        i = 0
        for row in airports:
            listbox.insert(i, row[0])
            i += 1

        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        my_frame.pack()

        listbox.pack(pady=10)
        my_frame.place(x=10, y=260)

    def AirlineDetails(self, event):

        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection[0])
        print(picked)
        airlineDetailWindow = Toplevel(self.CMPT354)
        airlineDetailWindow.title("Airline Detail window")
        airlineDetailWindow.geometry("500x500")
        Label(airlineDetailWindow, text=picked).pack()
        self.displayBaseOfOperation(picked, airlineDetailWindow)
        self.displayAirplaneOperation(picked, airlineDetailWindow)

    def openAirLineNewWindow(self):
        newWindow = Toplevel(self.CMPT354)
        newWindow.title("Airlines")
        newWindow.geometry("500x500")
        label = Label(newWindow, text="Select an airline to view")
        label.place(x=180, y=20)

        listbox = Listbox(newWindow, width=70, height=15, fg="blue")
        sql = "SELECT * FROM airline"
        print(sql)
        self.mycursor.execute(sql)
        # get all airlines
        airline = self.mycursor.fetchall()
        i = 0
        for row in airline:
            s = row[0] + ", reputation = " + str(row[2]) + "Cost Structure = " + str(row[1])
            listbox.insert(i, s)
            i += 1

        listbox.place(x=20, y=80)
        # Double click event with mouse
        listbox.bind('<Double-1>', self.AirlineDetails)

        ##THIS FEATURE IS BROKEN

    def Update_With_Trigger(self):
        pass



    def StartUI(self):
        self.listBoxCreate()
        self.otherFeaturesLabel()
        self.displayFeatureButtons()

        #self.editAllAirportsFromCountry()
        self.CMPT354.mainloop()  # Executes GUI