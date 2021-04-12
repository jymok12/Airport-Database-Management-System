from functools import partial
from tkinter import *
from dbquery import Dbquery

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
    def getsqlAirline(self, picked):
        sql = "SELECT * FROM airline"
        return sql
    def openSelectorMenuWithEvent(self,savedSelection,selectingFrom, depth,event):
        newWindow = Toplevel(self.CMPT354)
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
        if depth == 0:
            sql = self.getsqlCountry(picked)
        if depth == 1:
            sql = self.getsqlRoute(picked)
        if depth == 2:
            sql = self.getsqlAirline(picked)
        print(sql)
        self.mycursor.execute(sql)
        # get all airlines
        country = self.mycursor.fetchall()
        i = 0
        for row in country:
            s = row[0]+ "," + row[1]
            listbox.insert(i, s)
            i += 1
        listbox.bind('<Double-1>', partial(self.openSelectorMenuWithEvent, savedSelection, selectingFrom, depth+1))

        listbox.place(x=20, y=80)
    def openSelectorMenu(self, savedSelection,selectingFrom):
        depth = 0
        newWindow = Toplevel(self.CMPT354)
        newWindow.title("Select from " + selectingFrom)
        newWindow.geometry("500x500")
        label = Label(newWindow, text="Select an "+ selectingFrom+ " to make a flight in")
        label.place(x=180, y=20)
        selectingFrom = []
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
        listbox.bind('<Double-1>', partial(self.openSelectorMenuWithEvent,savedSelection,selectingFrom, depth))
