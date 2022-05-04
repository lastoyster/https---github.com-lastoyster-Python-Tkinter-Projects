from tkinter import *
#Import calendar module
import calendar

def showCal():

    #create a GUI window
    new_gui = Tk()

#set the bgcolor of GUI window
new_gui.config(background="white")

new_gui_title("Calendar")

new_gui.geometry("550x600")

#get method returns current text as string
fetch_year = int(year_field.get())

#calendar method of calendar module return function
#the calendar of the given year
cal_content = calendar.calendar(fetch_year)

cal_year.grid(row = 5, column =1, padx=20)

new_gui.mainloop()

if_name_== "_main_":

# Create a GUI window
gui = Tk()
     
    # Seta the background colour of GUI window
gui.config(background = "white")
 
    # set the name of tkinter GUI window
gui.title("CALENDAR")
 
    # Set the configuration of GUI window
 gui.geometry("250x140")
 
    # Create a CALENDAR : label with specified font and size
cal = Label(gui, text = "CALENDAR", bg = "dark gray",
                            font = ("times", 28, 'bold'))
 
    # Create a Enter Year : label
year = Label(gui, text = "Enter Year", bg = "light green")
     
    # Create a text entry box for filling or typing the information. 
    year_field = Entry(gui)
 
    # Create a Show Calendar Button and attached to showCal function
    Show = Button(gui, text = "Show Calendar", fg = "Black",
                              bg = "Red", command = showCal)
 
    # Create a Exit Button and attached to exit function
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
     
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row = 1, column = 1)
 
    year.grid(row = 2, column = 1)
 
    year_field.grid(row = 3, column = 1)
 
    Show.grid(row = 4, column = 1)
 
    Exit.grid(row = 6, column = 1)
     
    # start the GUI
    gui.mainloop()
    
