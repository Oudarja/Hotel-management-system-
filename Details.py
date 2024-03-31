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


class DetailsRoom:
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

        #=====================title=======================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #=====================logo===============
        img2=Image.open("imgs\\logo.png")
        #Image width and height
        #antialiasing method for resizing, which helps in smoothing the edges.
        img2=img2.resize((100,50),Image.ANTIALIAS)
        '''
        img1 is then converted into a Tkinter PhotoImage object (self.photoimg1) using ImageTk.PhotoImage() from the ImageTk module. 
        This is necessary for displaying the image in a Tkinter label.
        '''
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #==============label Frame==========================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #===============label and entrys======================
        #Floor
        lbl_floor=Label(labelframeleft,text="Floor No:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,width=29,textvariable=self.var_floor,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)
        
        #Room No

        lbl_roomno=Label(labelframeleft,text="Room No:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W)

        self.var_roomno=StringVar()

        entry_roomno=ttk.Entry(labelframeleft,width=29,textvariable=self.var_roomno,font=("arial",13,"bold"))
        entry_roomno.grid(row=1,column=1)



        #Room Type
        lbl_roomtype=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W)

        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(labelframeleft,width=29,textvariable=self.var_roomtype,font=("arial",13,"bold"))
        entry_roomtype.grid(row=2,column=1)


        #===============btn========================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)


        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1,pady=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1,pady=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1,pady=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.Reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1,pady=1)



         #========================table frame search system=============
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)


        # Giving scroll bar
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(Table_Frame,columns=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set
                                                    ,yscrollcommand=scroll_y.set
                                                    )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)



     #for showing to user

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="RoomNo")
        self.room_table.heading("roomtype",text="RoomType")

        self.room_table["show"]="headings"

        #Setting width of every column 
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)


        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()



    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error,All fields are required",parent=self.root)

        else:
            #here connection to database is done
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),
                                                                        self.var_roomno.get(),
                                                                        self.var_roomtype.get(),
                                                                        ))
                
                conn.commit()
                #To show data from databasae
                self.fetch_data()
                conn.close()
                
                #message box should be shown into the same corresponding window so parent= self.root
                messagebox.showinfo("New Room has been added sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    
    
    #for fetching data from data base
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        #If there is existing data in table of cust details in page then clear this and insert newly data from database 
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                #"" as the first parameter indicates that the data should be inserted at the root level.
                #END indicates that the data should be inserted at the end of the existing data in the table.
                self.room_table.insert("",END,values=i)

        conn.commit()
        conn.close()

    #====This function is for showing the selected tuple in the entry field====
    def get_cursor(self,events=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])

    
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error,Please Enter Room number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                          self.var_floor.get(),
                                                                                          self.var_roomtype.get(),
                                                                                          self.var_roomno.get()
                                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    def Delete(self):
        mdelete=messagebox.askyesno("Hotel Managaement System","Do you want to delete this detail",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            #here after self.var_ref.get() a comma is given becasue 
            #execute() method of the cursor expects the parameters to be provided as a list, tuple, or dictionary 
            #So a comma is given to become a tuple
            my_cursor.execute("delete from details where RoomNo=%s",(self.var_roomno.get(),))
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Room details has been deleted successfully",parent=self.root)
    




    def Reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")


        




        
        
    





 









if __name__=="__main__":
    # Creates an instance of the Tkinter window.
    root=Tk()
    #Creates an instance of the HotelManagementSystem class, passing the Tkinter window instance as a parameter.
    obj=DetailsRoom(root)
    '''
        Enters the Tkinter main event loop, which waits for user events (such as button clicks) and responds to them.
        The program remains in this loop until the user closes the window.
    '''
    root.mainloop()