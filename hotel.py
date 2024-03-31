from tkinter import*
#PIL is python image processing library
#ImageTk module provides tools for integrating PIL images with Tkinter GUI applications.
#Image module is part of the Python Imaging Library (PIL), and it provides a class with the same name (Image) for handling images.
from PIL import Image,ImageTk
#importing cust_win from customer.py
from customer import Cust_Win

from room import Roombooking

from Details import DetailsRoom

from Report import Developer

class HotelManagementSystem:
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
        self.root.geometry("1550x800+0+0")

#====================Heading Image=======================
        img1=Image.open("imgs\\heading.jpg")
        #Image width and height
        #antialiasing method for resizing, which helps in smoothing the edges.
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        '''
        img1 is then converted into a Tkinter PhotoImage object (self.photoimg1) using ImageTk.PhotoImage() from the ImageTk module. 
        This is necessary for displaying the image in a Tkinter label.
        '''
        self.photoimg1=ImageTk.PhotoImage(img1)
        '''
        A Tkinter Label widget (lblimg) is created with the Tkinter window (self.root) as its parent. It is configured to display the image (self.photoimg1). The bd parameter specifies the border width, and relief specifies the border style (RIDGE).
        
        '''
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #=====================logo Image==============
        img2=Image.open("imgs\\logo.png")
        #Image width and height
        #antialiasing method for resizing, which helps in smoothing the edges.
        img2=img2.resize((230,140),Image.ANTIALIAS)
        '''
        img1 is then converted into a Tkinter PhotoImage object (self.photoimg1) using ImageTk.PhotoImage() from the ImageTk module. 
        This is necessary for displaying the image in a Tkinter label.
        '''
        self.photoimg2=ImageTk.PhotoImage(img2)
        '''
        A Tkinter Label widget (lblimg) is created with the Tkinter window (self.root) as its parent. It is configured to display the image (self.photoimg1). The bd parameter specifies the border width, and relief specifies the border style (RIDGE).
        
        '''
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #=======================title=========================
        #lbl_title: This is a variable that is used to store the Label widget that will display the title of the Hotel Management System.
        # Label-> This is a class from a GUI library, likely Tkinter, used to create a label that can display text or images.
        #self.root is the root window or the main window of the GUI.
        #RAISED or RIDGE: Creates a raised, 3D effect on the border
        #bd=4 : Sets the border width of the label to 4 pixels.
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #===================in Frame============================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        #140+50=190
        main_frame.place(x=0,y=190,width=1550,height=610)
        
        #==========================menu========================
        #Menu bar creation
        lbl_manu= Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)

        #as now the menu is placed on the main_frame so starting position is x=0 y=0
        lbl_manu.place(x=0,y=0,width=230)

        #===============button frame===========================

        #button frame will be over main_frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        
        btn_frame.place(x=0,y=35,width=228,height=190)
        
        #==============button creration=================
        #pady=1 adds some vertical padding to the button.
        #cursor="hand1": Changes the cursor style to a hand icon when it hovers over the button, indicating it can be clicked.
        '''
        place method, when you specify the width parameter, it is measured in pixels.pack or grid, the width might be specified differently. 
        In case of pack or grid width parameter to specify the width in characters
        '''
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="DEVELOPER",width=22,command=self.developer,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,command=self.logout,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #========================body image=========================================
        
        img3=Image.open("imgs\\body_image.jpg")
        #Image width and height
        #antialiasing method for resizing, which helps in smoothing the edges.
        img3=img3.resize((1310,610),Image.ANTIALIAS)
        '''
        img1 is then converted into a Tkinter PhotoImage object (self.photoimg1) using ImageTk.PhotoImage() from the ImageTk module. 
        This is necessary for displaying the image in a Tkinter label.
        '''
        self.photoimg3=ImageTk.PhotoImage(img3)
        '''
        A Tkinter Label widget (lblimg) is created with the Tkinter window (self.root) as its parent. It is configured to display the image (self.photoimg1). The bd parameter specifies the border width, and relief specifies the border style (RIDGE).
        
        '''
        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=610)

        #=========================food image==========================================
        img4=Image.open("imgs\\food.jpg")
        #Image width and height
        #antialiasing method for resizing, which helps in smoothing the edges.
        img4=img4.resize((230,210),Image.ANTIALIAS)
        '''
        img1 is then converted into a Tkinter PhotoImage object (self.photoimg1) using ImageTk.PhotoImage() from the ImageTk module. 
        This is necessary for displaying the image in a Tkinter label.
        '''
        self.photoimg4=ImageTk.PhotoImage(img4)
        '''
        A Tkinter Label widget (lblimg) is created with the Tkinter window (self.root) as its parent. It is configured to display the image (self.photoimg1). The bd parameter specifies the border width, and relief specifies the border style (RIDGE).
        
        '''
        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)


       #============================room image=======================================
        img5=Image.open("imgs\\room.jpeg")
        #Image width and height
        #antialiasing method for resizing, which helps in smoothing the edges.
        img5=img5.resize((230,210),Image.ANTIALIAS)
        '''
        img1 is then converted into a Tkinter PhotoImage object (self.photoimg1) using ImageTk.PhotoImage() from the ImageTk module. 
        This is necessary for displaying the image in a Tkinter label.
        '''
        self.photoimg5=ImageTk.PhotoImage(img5)
        '''
        A Tkinter Label widget (lblimg) is created with the Tkinter window (self.root) as its parent. It is configured to display the image (self.photoimg1). The bd parameter specifies the border width, and relief specifies the border style (RIDGE).
        
        '''
        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=430,width=230,height=210)


    def cust_details(self):
        #This line creates a new top-level window (Toplevel) as a child of the root window (self.root).
        #This new window can be used to display additional content or forms.
        self.new_window=Toplevel(self.root)
        #This line creates an instance of the Cust_Win class and passes the newly created Toplevel window (self.new_window) 
        #as an argument.
        self.app=Cust_Win(self.new_window)

    # This is a function and the class is Roombooking
    def roombooking(self):
        #This line creates a new top-level window (Toplevel) as a child of the root window (self.root).
        #This new window can be used to display additional content or forms.
        self.new_window=Toplevel(self.root)
        #This line creates an instance of the RoomBooking class and passes the newly created Toplevel window (self.new_window) 
        #as an argument.
        self.app=Roombooking(self.new_window)

    def details_room(self):
        #This line creates a new top-level window (Toplevel) as a child of the root window (self.root).
        #This new window can be used to display additional content or forms.
        self.new_window=Toplevel(self.root)
        #This line creates an instance of the RoomBooking class and passes the newly created Toplevel window (self.new_window) 
        #as an argument.
        self.app=DetailsRoom(self.new_window)

    def developer(self):
        #This line creates a new top-level window (Toplevel) as a child of the root window (self.root).
        #This new window can be used to display additional content or forms.
        self.new_window=Toplevel(self.root)
        #This line creates an instance of the RoomBooking class and passes the newly created Toplevel window (self.new_window) 
        #as an argument.
        self.app=Developer(self.new_window)

    def logout(self):
        self.root.destroy()


        



if __name__=="__main__":
    # Creates an instance of the Tkinter window.
    root=Tk()
    #Creates an instance of the HotelManagementSystem class, passing the Tkinter window instance as a parameter.
    obj=HotelManagementSystem(root)
    '''
        Enters the Tkinter main event loop, which waits for user events (such as button clicks) and responds to them.
        The program remains in this loop until the user closes the window.
    '''
    root.mainloop()

