def onRouteSpecSubmit(entry):

    text = entry.get()
    countriesSelected.append(text)
    for x in countriesSelected:
        print(x)
    entry.delete(0, END)
def openCountrySelectGui():
    gui = Tk()
    label = Label(gui, text = "Please type the name of the coutries you would like to select airports from")
    entry = Entry(gui, width=50)
    entry.pack()
    text = entry.get()
    submutButton = Button(gui, text="submit", command=partial(onRouteSpecSubmit, entry))
    xButton = Button(gui, text = "x", command = gui.destroy).pack()
    submutButton.pack()
    def saveText(self,textField,getTextWindow):
        self.userText = textField.get("1.0",END)
        print(self.userText)
        getTextWindow.destroy()
        self.useDbQuery.editAllAirports(self.userText)
        self.db.commit()


    def getText(self,sometext):
        getTextWindow = Tk()  # Name of root
        getTextWindow.geometry("350x100")
        yLabel = 50  # Inside airportDisplays
        Title = Label(getTextWindow, text=sometext, fg="red", font="24")
        Title.place(x=0, y=0)
        textField = Text(getTextWindow)
        textField.place(x=0, y=50)
        sumbitButton = Button(getTextWindow, text= "sumbit", command=partial(self.saveText,textField,getTextWindow))
        sumbitButton.place(x=125,y=20)
    def getSomeText(self):
        getTextWindow = Tk()  # Name of root
        getTextWindow.geometry("350x100")
        yLabel = 50  # Inside airportDisplays
        Title = Label(getTextWindow, text="enter country name", fg="red", font="24")
        Title.place(x=0, y=0)
        textField = Text(getTextWindow)
        textField.place(x=0, y=50)
        sumbitButton = Button(getTextWindow, text="sumbit", command=partial(self.saveText, textField, getTextWindow))
        sumbitButton.place(x=125, y=20)
    def incAllApPop(self):
        self.getText("enter amount to increase nearbyPopulation by")
    def editAllAirports(self):
        allAirportEditButton = Button(self.CMPT354, text="edit all airports", command=self.incAllApPop)
        allAirportEditButton.place(x=0, y=450)
    def editSomeAirports(self):
        self.getSomeText()
    def editAllAirportsFromCountry(self):
        someAirportEditButton = Button(self.CMPT354, text="select all airports in country to edit", command=self.editSomeAirports)
        someAirportEditButton.place(x = 80, y=450)



root = Tk()
label  = Label(root, text = "airway project")
countrySelectButton = Button(root, text = "Select Countries",command = openCountrySelectGui)
label.pack()
countrySelectButton.pack()
root.mainloop()

