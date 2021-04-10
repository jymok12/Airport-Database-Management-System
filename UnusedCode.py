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




root = Tk()
label  = Label(root, text = "airway project")
countrySelectButton = Button(root, text = "Select Countries",command = openCountrySelectGui)
label.pack()
countrySelectButton.pack()
root.mainloop()

