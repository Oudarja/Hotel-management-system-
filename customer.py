from tkinter import*
#PIL is python image processing library
#ImageTk module provides tools for integrating PIL images with Tkinter GUI applications.
#Image module is part of the Python Imaging Library (PIL), and it provides a class with the same name (Image) for handling images.
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector

from tkinter import messagebox


class Cust_Win:
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

       #============================variables=========================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)

        self.var_ref.set(str(x))


        self.var_cust_name=StringVar()

        self.var_gender=StringVar()

        self.var_post=StringVar()

        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()

        self.var_id_number=StringVar()



        #title
        lbl_title=Label(self.root,text="INCLUDE CUSTOMER INFORMATION",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
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

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #===============label and entrys======================
        #CustRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        #This entry field state has been changed into read only
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #Cust name
        lbl_cust_name=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)


        textname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
        textname.grid(row=1,column=1)


        #Gender Combobox
        lbl_cust_name=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=2,column=0,sticky=W)
        #For gender
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)


        

        #Postcode
        lbl_post_ref=Label(labelframeleft,text="Post Code",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_post_ref.grid(row=3,column=0,sticky=W)
        txtpostcode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13,"bold"))
        txtpostcode.grid(row=3,column=1)


        #mobile number
        lbl_mobile=Label(labelframeleft,text="Mobile",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_mobile.grid(row=4,column=0,sticky=W)
        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        txtmobile.grid(row=4,column=1)


        #email
        lbl_mail=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_mail.grid(row=5,column=0,sticky=W)
        
        txtmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
        txtmail.grid(row=5,column=1)


        #Nationality
    
        lbl_nationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_nationality.grid(row=6,column=0,sticky=W)
        combo_nation=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nation["value"]=("Bangladeshi","Indian","Pakistani","British","American","Russian","European","Australian","other")
        combo_nation.current(0)
        combo_nation.grid(row=6,column=1)

        #Id proof type combobox
        lbl_idproof=Label(labelframeleft,text="Id Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_idproof.grid(row=7,column=0,sticky=W)
        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_idproof["value"]=("NID","Driving Licience","Passport")
        combo_idproof.current(0)
        combo_idproof.grid(row=7,column=1)

        #Id number 
        lbl_id=Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_id.grid(row=8,column=0,sticky=W)
        
        txtid=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
        txtid.grid(row=8,column=1)

        # Address
        lbl_address=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_address.grid(row=9,column=0,sticky=W)
        
        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        txtaddress.grid(row=9,column=1)


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



        #==========================Table frame  search=========================================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)


        lablSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
        lablSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
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


        #===================show data table===========================


        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)
        
        # Giving scroll bar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","gender",
                                                    "post","mobile","email","nationality","idproof"
                                                    ,"idnum","address"),xscrollcommand=scroll_x.set
                                                    ,yscrollcommand=scroll_y.set
                                                    )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        #for showing to user

        self.cust_Details_Table.heading("ref",text="Refer No")
        self.cust_Details_Table.heading("name",text="Name")
        self.cust_Details_Table.heading("gender",text="Gender")
        self.cust_Details_Table.heading("post",text="Post Code")
        self.cust_Details_Table.heading("mobile",text="Mobile No")
        self.cust_Details_Table.heading("email",text="Email")
        self.cust_Details_Table.heading("nationality",text="Nationality")
        self.cust_Details_Table.heading("idproof",text="IdProof")
        self.cust_Details_Table.heading("idnum",text="Id Num")
        self.cust_Details_Table.heading("address",text="Address")


        self.cust_Details_Table["show"]="headings"
        #Setting width of every column 
        self.cust_Details_Table.column("ref",width=100)
        self.cust_Details_Table.column("name",width=100)
        self.cust_Details_Table.column("gender",width=100)
        self.cust_Details_Table.column("post",width=100)
        self.cust_Details_Table.column("mobile",width=100)
        self.cust_Details_Table.column("email",width=100)
        self.cust_Details_Table.column("nationality",width=100)
        self.cust_Details_Table.column("idproof",width=100)
        self.cust_Details_Table.column("idnum",width=100)
        self.cust_Details_Table.column("address",width=100)


        self.cust_Details_Table.pack(fill=BOTH,expand=1)
        #The bind method is used to bind an event to a callback function. 
        #In this case, the event being bound is the release of the left mouse
        #button ("<ButtonRelease-1>").
        '''
        When the left mouse button is released over the self.cust_Details_Table widget, 
        the function self.get_cursor will be called.
        '''
        #ButtonRelease-1-->left button
        #ButtonRelease-2--> middle mouse buttone
        #ButtonRelease-3-->right button
        self.cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        
        #when this window open to fetch and show 
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_id_number.get()=="":
            messagebox.showerror("Error,All fields are required",parent=self.root)

        else:
            #here connection to database is done
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                            self.var_cust_name.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_post.get(),
                                                                                            self.var_mobile.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_nationality.get(),
                                                                                            self.var_id_proof.get(),
                                                                                            self.var_id_number.get(),
                                                                                            self.var_address.get()))
                
                conn.commit()
                #To show data from databasae
                self.fetch_data()
                conn.close()
                
                #message box should be shown into the same corresponding window so parent= self.root
                messagebox.showinfo("Success, Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"Some thing went wrong:{str(es)}",parent=self.root)
        

    #for fetching data from data base
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        #If there is existing data in table of cust details in page then clear this and insert newly data from database 
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                #"" as the first parameter indicates that the data should be inserted at the root level.
                #END indicates that the data should be inserted at the end of the existing data in the table.
                self.cust_Details_Table.insert("",END,values=i)

        conn.commit()
        conn.close()
     #====This function is for showing the selected tuple in the entry field====
    def get_cursor(self,events=""):
        cursor_row=self.cust_Details_Table.focus()
        content=self.cust_Details_Table.item(cursor_row)
        row=content["values"]
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_post.set(row[3])
        self.var_mobile.set(row[4])
        self.var_email.set(row[5])
        self.var_nationality.set(row[6])
        self.var_id_proof.set(row[7])
        self.var_id_number.set(row[8])
        self.var_address.set(row[9])
        
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error,Please Enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Gender=%s,`Post Code`=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnum=%s,Address=%s where Ref=%s",(
                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                self.var_gender.get(),
                                                                                                                                                self.var_post.get(),
                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                self.var_email.get(),
                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                self.var_id_number.get(),
                                                                                                                                                self.var_address.get(),
                                                                                                                                                self.var_ref.get()

                                                                                                                                          ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)


    def Delete(self):
        mdelete=messagebox.askyesno("Hotel Managaement System","Do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            #here after self.var_ref.get() a comma is given becasue 
            #execute() method of the cursor expects the parameters to be provided as a list, tuple, or dictionary 
            #So a comma is given to become a tuple
            my_cursor.execute("delete from customer where Ref=%s",(self.var_ref.get(),))
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Customer details has been deleted successfully",parent=self.root)
    
    def Reset(self):
        self.var_cust_name.set("")
        #self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        #self.var_nationality.set("")
        #self.var_id_proof.set("")
        #self.var_id_number.set("")
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            
            conn.commit()
            conn.close()









    


if __name__=="__main__":
    # Creates an instance of the Tkinter window.
    root=Tk()
    #Creates an instance of the HotelManagementSystem class, passing the Tkinter window instance as a parameter.
    obj=Cust_Win(root)
    '''
        Enters the Tkinter main event loop, which waits for user events (such as button clicks) and responds to them.
        The program remains in this loop until the user closes the window.
    '''
    root.mainloop()
