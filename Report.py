from tkinter import*
#PIL is python image processing library
#ImageTk module provides tools for integrating PIL images with Tkinter GUI applications.
#Image module is part of the Python Imaging Library (PIL), and it provides a class with the same name (Image) for handling images.
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector

from tkinter import messagebox


class Developer:
    '''
    This is the constructor method for the class. It is called when an object of the class is created. 
    It takes self (which is a reference to the instance of the class) and root as parameters.
    root will be the Tkinter window.
    '''
    def __init__(self,root):
        #Assigns the Tkinter window instance to the class variable 
        self.root=root
        # Sets the title of the Tkinter window to "Hotel Management System".
        self.root.title("Hotel Management System")
        #here 1295x550 is width and height and next two parameter is
        # postion of x and y 
        self.root.geometry("1295x550+230+220")


        # Developer Information Frame
        developer_frame = Frame(self.root, bd=2, relief=RIDGE)
        developer_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Developer Information Labels
        lbl_developer = Label(developer_frame, text="Developer:", font=("Arial", 20, "bold"))
        lbl_developer.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        lbl_name = Label(developer_frame, text="Oudarja Barman Tanmoy", font=("Arial", 16))
        lbl_name.grid(row=1, column=0, padx=5, sticky=W)

        lbl_email = Label(developer_frame, text="Email: xyz@gmail.com", font=("Arial", 16))
        lbl_email.grid(row=2, column=0, padx=5, sticky=W)

        lbl_mobile = Label(developer_frame, text="Mobile: xxxxxyyyyyzzz", font=("Arial", 16))
        lbl_mobile.grid(row=3, column=0, padx=5, sticky=W)

        lbl_website = Label(developer_frame, text="Website: www.johndoe.com", font=("Arial", 16))
        lbl_website.grid(row=4, column=0, padx=5, sticky=W)






if __name__=="__main__":
    # Creates an instance of the Tkinter window.
    root=Tk()
    #Creates an instance of the HotelManagementSystem class, passing the Tkinter window instance as a parameter.
    obj=Developer(root)
    '''
        Enters the Tkinter main event loop, which waits for user events (such as button clicks) and responds to them.
        The program remains in this loop until the user closes the window.
    '''
    root.mainloop()
