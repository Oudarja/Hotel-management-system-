from tkinter import*
#PIL is python image processing library
#ImageTk module provides tools for integrating PIL images with Tkinter GUI applications.
#Image module is part of the Python Imaging Library (PIL), and it provides a class with the same name (Image) for handling images.
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime

from  login import Login_window
import mysql.connector

from tkinter import messagebox



class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")


        #==============variable================

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        #======================Image=======================
        
        img=Image.open(r"F:\PROJECT\Hotel Management System\imgs\reg.jpeg")
        img=img.resize((1550,800),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        lblimg1=Label(self.root,image=self.photoimg,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=1550,height=800)

        #====================frame====================

        frame=Frame(self.root,bg="white")

        frame.place(x=520,y=100,width=800,height=530)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",25,"bold"),bg="darkgreen",fg="white")
        register_lbl.place(x=20,y=20)

        #=====================Label and entry=================

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")

        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")

        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=370,y=130,width=250)


        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        txt_email.place(x=370,y=200,width=250)


        security_q=Label(frame,text="Select security question",font=("times new roman",15,"bold"),bg="white",fg="black")

        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_q['values']=("Give your birth place","Give your girl friend name","Give your pet name")
        self.combo_security_q.place(x=50,y=270,width=250)

        self.combo_security_q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")

        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)


        pswd=Label(frame,text="password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))

        self.txt_pswd.place(x=50,y=340,width=250)


        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))

        self.txt_confirm_pswd.place(x=370,y=340,width=250)



        #==================check button=====================

        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the terms and conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)

        #====================button===================

        img1=Image.open(r"F:\PROJECT\Hotel Management System\imgs\register_button.jpg")
        img1=img1.resize((150,50),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,command=self.register_data,image=self.photoimg1,borderwidth=0,cursor="hand2")
        b1.place(x=100,y=450,width=200)


        
        img2=Image.open(r"F:\PROJECT\Hotel Management System\imgs\login_button.jpg")
        img2=img2.resize((150,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(frame,command=self.login__,image=self.photoimg2,borderwidth=0,cursor="hand2")
        b1.place(x=350,y=450,width=200)




        #=====================Function declration============

    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()=="" or self.var_securityQ=="":
            messagebox.showerror("Error","All fields are required")

        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password should be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)

            row=my_cursor.fetchone()

            if row!=None:
                messagebox.showerror("Error","user already exist")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get()
                                                                                       ))
            conn.commit()
            conn.close()

            messagebox.showinfo("Sucess","Registartion Completed")


    def login__(self):
        self.new_window=Toplevel(self.root)
        #This line creates an instance of the RoomBooking class and passes the newly created Toplevel window (self.new_window) 
        #as an argument.
        self.app=Login_window(self.new_window)



if __name__=="__main__":
    # Creates an instance of the Tkinter window.
    root=Tk()
    #Creates an instance of the HotelManagementSystem class, passing the Tkinter window instance as a parameter.
    obj=Register(root)
    '''
        Enters the Tkinter main event loop, which waits for user events (such as button clicks) and responds to them.
        The program remains in this loop until the user closes the window.
    '''
    root.mainloop()
