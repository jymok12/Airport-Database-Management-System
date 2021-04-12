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
