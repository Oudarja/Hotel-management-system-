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


class Roombooking:
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

        #======================variable===================

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


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

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #===============label and entrys======================
        #Customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        #This entry field state has been changed into read only
        #textvariable=self.var_contact for taking input in entry field
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=29,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1)

        #Fetch data button
        btnFetchData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=9)
        btnFetchData.place(x=347,y=4)
        


        #Check_in_Date
        check_in_date=Label(labelframeleft,text="Check_In Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        #This entry field state has been changed into read only
        txt_check_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txt_check_in_date.grid(row=1,column=1)

        #Check_out_Date
        check_out_date=Label(labelframeleft,text="Check_Out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        #This entry field state has been changed into read only
        txt_check_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txt_check_out_date.grid(row=2,column=1)

        #Room Type

        lbl_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=3,column=0,sticky=W)
        #For gender
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)


        #Available Room
        lblRoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        txtRoomAvailable.grid(row=4,column=1)

        #Meal
        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        combo_Meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,width=27,font=("arial",12,"bold"),state="readonly")
        combo_Meal["value"]=("Breakfast","Lunch","Dinner","All")
        combo_Meal.current(0)
        combo_Meal.grid(row=5,column=1)

        #No of Days
        lblNoOfDays=Label(labelframeleft,text="No of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)

        #Paid Tax
        lblPaidtax=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPaidtax.grid(row=7,column=0,sticky=W)
        txtpaidtax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        txtpaidtax.grid(row=7,column=1)

        #Sub Total
        lblsubtotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblsubtotal.grid(row=8,column=0,sticky=W)
        txtsubtotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
        txtsubtotal.grid(row=8,column=1)

        #Total Cost

        lbltotal=Label(labelframeleft,text="Total cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lbltotal.grid(row=9,column=0,sticky=W)
        txttotal=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txttotal.grid(row=9,column=1)

        #=====================Bill Button====================
        
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,pady=1,sticky=W)



        #===============btn========================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)


        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1,pady=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1,pady=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1,pady=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.Reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1,pady=1)



        #========================table frame search system=============
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)


        lablSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
        lablSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("contact","Room No")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)


        #entry field
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1,pady=1)
        
        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1,pady=1)


        #=====================rightside image================
        img3=Image.open("imgs\\Bedroom.jpg")
        #Image width and height
        #antialiasing method for resizing, which helps in smoothing the edges.
        img3=img3.resize((500,230),Image.ANTIALIAS)
        '''
        img1 is then converted into a Tkinter PhotoImage object (self.photoimg1) using ImageTk.PhotoImage() from the ImageTk module. 
        This is necessary for displaying the image in a Tkinter label.
        '''
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=760,y=55,width=500,height=230)



        #===================show data table===========================

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)
        
        # Giving scroll bar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout",
                                                    "roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set
                                                    ,yscrollcommand=scroll_y.set
                                                    )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        #for showing to user

        self.room_table.heading("contact",text="contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No Of Days")


        self.room_table["show"]="headings"
        #Setting width of every column 
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)


        self.room_table.pack(fill=BOTH,expand=1)
        '''
        When the left mouse button is released within the self.room_table 
        widget, the self.get_cursor function will be called.
        '''
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
    


    #====================This function is for adding data into data base===========
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error,All fields are required",parent=self.root)

        else:
            #here connection to database is done
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
                                                                                   self.var_checkin.get(),
                                                                                   self.var_checkout.get(),
                                                                                   self.var_roomtype.get(),
                                                                                   self.var_roomavailable.get(),
                                                                                   self.var_meal.get(),
                                                                                   self.var_noofdays.get()))
                
                conn.commit()
                #To show data from databasae
                self.fetch_data()
                conn.close()
                
                #message box should be shown into the same corresponding window so parent= self.root
                messagebox.showinfo("Success,Room has been booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"Some thing went wrong:{str(es)}",parent=self.root)
    

    #====This function is for showing the selected tuple in the entry field====
    def get_cursor(self,events=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])


        #Update

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error,Please Enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                            self.var_contact.get()
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
            my_cursor.execute("delete from room where contact=%s",(self.var_contact.get(),))
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Room details has been deleted successfully",parent=self.root)

    def Reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
        my_cursor=conn.cursor()
        val=self.search_var.get()
        if val=="Room No":
            my_cursor.execute("select * from room where `Room No` LIKE '%"+str(self.txt_search.get())+"%'")
        else:
            my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            
            conn.commit()
            conn.close()

    

    def total(self):
        indate = self.var_checkin.get()
        outdate = self.var_checkout.get()

        # Ensure consistent date format
        date_format = "%d-%m-%y"

        try:
            indate = datetime.strptime(indate, date_format)
            outdate = datetime.strptime(outdate, date_format)
        except ValueError:
            # Handle invalid date format
            print("Invalid date format. Please use format dd-mm-yy.")
            return

       # Calculate the number of days
        self.var_noofdays.set(abs((outdate - indate).days))

        # Define the bill dictionary
        Bill_dict = {
            "Single": 1000,
            "Double": 2000,
            "Luxary": 3000,
            "Breakfast": 200,
            "Lunch": 800,
            "Dinner": 800,
            "All": 1500
            }

        # Validate meal and room type selections
        meal_type = self.var_meal.get()  # Get the value from StringVar
        room_type = self.var_roomtype.get()  # Get the value from StringVar

        if meal_type not in Bill_dict:
            print("Meal type not found in dictionary.")
            return
        if room_type not in Bill_dict:
            print("Room type not found in dictionary.")
            return

        # Calculate the subtotal
        meal_cost = Bill_dict[meal_type]
        room_cost = Bill_dict[room_type]
        total_cost = (meal_cost + room_cost) * float(self.var_noofdays.get())

        # Calculate taxes and total amount
        tax_rate = 0.3
        tax = total_cost * tax_rate
        subtotal = total_cost
        total = subtotal + tax

        # Format calculated values
        Tax = "Tk {:.2f}".format(tax)
        ST = "Tk {:.2f}".format(subtotal)
        TT = "Tk {:.2f}".format(total)

        # Update variables
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

    


    #for fetching data from data base
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
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
        


    #====================All data fetch===============
    # this function should be called in fetch button in command 
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            query=("select `Name` from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                #Now name from database will be shown 

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)


            #=================gender==================
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            query=("select Gender from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                #Now name from database will be shown 

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=30)
            #=================email===================
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            query=("select Email from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                #Now name from database will be shown 

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=60)

            #===================Nationality========================
                
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            query=("select Nationality from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                #Now name from database will be shown 

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=90)
            

            #====================Address===========================
                
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            query=("select Address from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)

                #Now name from database will be shown 

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120)



if __name__=="__main__":
    # Creates an instance of the Tkinter window.
    root=Tk()
    #Creates an instance of the HotelManagementSystem class, passing the Tkinter window instance as a parameter.
    obj=Roombooking(root)
    '''
        Enters the Tkinter main event loop, which waits for user events (such as button clicks) and responds to them.
        The program remains in this loop until the user closes the window.
    '''
    root.mainloop()
