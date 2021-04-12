from functools import partial
from tkinter import *
from dbquery import Dbquery
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
    def runCountryGDPquery(self,editgdpMenu):
        print("usertext1 = " + self.userText)
        print("usertext2 = " + self.userText2)

        query = 'Update country set gdpPercapita = '
        query+=self.userText2
        query+=" where countryname = '"
        query+=self.userText
        query+="'"
        query = query.replace("\n","")

        print("running query: " + query)
        self.mycursor.execute(query)
        self.db.commit()
        editgdpMenu.destroy()
    def editCountryGdp(self):
        editgdpMenu = Tk()
        editgdpMenu.geometry("650x250")
        textField = Text(editgdpMenu)
        textField.place(x=0, y=200)
        sumbitButton = Button(editgdpMenu, text="save country selection",
                              command=partial(self.saveTextSelection, textField, editgdpMenu))
        sumbitButton.place(x=0, y=20)
        sumbitButtonNum = Button(editgdpMenu, text="save GDP value",
                                 command=partial(self.saveTextSelection2, textField, editgdpMenu))
        sumbitButtonNum.place(x=165, y=20)
        runButton = Button(editgdpMenu, text="run query with selected data",
                           command=partial(self.runCountryGDPquery, editgdpMenu))
        runButton.place(x=350, y=20)
        editgdpMenu.mainloop()
    def displayFeatureButtons(self):
        openTextWindowButton = Button(self.CMPT354, text="editAllAirportPopulations", command=self.editAllAirports)
        openTextWindowButton.place(x=0, y=450)
        openEditSomeButton = Button(self.CMPT354, text="editAirportsInCountry", command=self.editSomeAirports)
        openEditSomeButton.place(x = 140, y = 450)
        openCountryEditMenu = Button(self.CMPT354, text= "editCountryGDP", command = self.editCountryGdp)
        openCountryEditMenu.place(x = 280, y=450)
    def openGetTextMenu(self):
        print("pressed")
    def saveTextSelection(self,textfield,theRoottk):
        self.userText = ""
        text = textfield.get("1.0",END)
        label = Label(theRoottk,text="savedSelection as: " + text)
        label.place(x = 0, y = 55)
        self.userText = text
        print(text)
    def saveTextSelection2(self,textfield,theRoottk):
        self.userText2 = ""
        text = textfield.get("1.0",END)
        label = Label(theRoottk,text="savedSelection as: " + text)
        label.place(x = 0, y = 85)
        self.userText2 = text
        print(text)

    def runQuery(self, inmenu):
        query = "UPDATE airport SET nearbyPopulation = nearbyPopulation *" + self.userText + " where AirportCode = airportCode;"
        self.mycursor.execute(query)
        self.db.commit()
        print("ran the following query: " + query)
        self.userText = ""
        self.mycursor.execute(Dbquery.updateRoutesQuery)
        self.db.commit()
        inmenu.destroy()
    def runQuerySome(self, inmenu):
        print("usertext1 = "+ self.userText)
        print("usertext2 = " + self.userText2)
        query = "UPDATE airport a, country c SET a.nearbyPopulation = a.nearbyPopulation*"+ self.userText2+ " where a.AirportCode = a.airportCode AND  a.countryId = c.countryKey AND c.countryName = '"+ self.userText+"' ;"
        self.mycursor.execute(query)
        self.db.commit()
        self.mycursor.execute(Dbquery.updateRoutesQuery)
        self.db.commit()
        inmenu.destroy()
        self.userText = ""
        self.userText2 = ""
    def editAllAirports(self):
        editAllMenu = Tk()
        editAllMenu.geometry("450x150")
        textField = Text(editAllMenu)
        textField.place(x=0, y=100)
        sumbitButton = Button(editAllMenu, text="save text selection", command=partial(self.saveTextSelection,textField,editAllMenu))
        sumbitButton.place(x=125, y=20)
        runButton = Button(editAllMenu, text="run query with selected data",command=partial(self.runQuery, editAllMenu))
        runButton.place(x=250,y=20)
        editAllMenu.mainloop()
    def editSomeAirports(self):
        editSomeMenu = Tk()
        editSomeMenu.geometry("650x250")
        textField = Text(editSomeMenu)
        textField.place(x=0, y=200)
        sumbitButton = Button(editSomeMenu, text="save country selection",
                              command=partial(self.saveTextSelection, textField, editSomeMenu))
        sumbitButton.place(x=0, y=20)
        sumbitButtonNum = Button(editSomeMenu, text="save multiplier selection",
                              command=partial(self.saveTextSelection2, textField, editSomeMenu))
        sumbitButtonNum.place(x=165, y=20)
        runButton = Button(editSomeMenu, text="run query with selected data",
                           command=partial(self.runQuerySome, editSomeMenu))
        runButton.place(x=350, y=20)
        editSomeMenu.mainloop()

    def StartUI(self):
        self.listBoxCreate()
        self.otherFeaturesLabel()
        self.displayFeatureButtons()
        #self.editAllAirportsFromCountry()
        self.CMPT354.mainloop()  # Executes GUI