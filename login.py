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
from hotel import HotelManagementSystem

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()



class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")

        self.root.geometry("1550x800+0+0")


        img=Image.open("imgs\\login.jpg")
        #Image width and height
        #antialiasing method for resizing, which helps in smoothing the edges.
        img=img.resize((1550,800),Image.ANTIALIAS)

        self.photoimg=ImageTk.PhotoImage(img)
        '''
        img1 is then converted into a Tkinter PhotoImage object (self.photoimg1) using ImageTk.PhotoImage() from the ImageTk module. 
        This is necessary for displaying the image in a Tkinter label.
        '''
        lblimg=Label(self.root,image=self.photoimg,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=800)


        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"F:\PROJECT\Hotel Management System\imgs\userlogin.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label

        username=Label(frame,text="Admin email",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtemail=Entry(frame,font=("times new roman",15,"bold"))
        self.txtemail.place(x=70,y=185,width=250)


        
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=70,y=250,width=250)


        #login btn

        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg='white',bg='red',activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register btn

        
        registerbtn=Button(frame,text="New user registration",command=self.register_window,font=("times new roman",10,"bold"),bd=3,borderwidth=0,fg='white',bg='black',activeforeground="white",activebackground="black")
        registerbtn.place(x=95,y=350,width=160)

        #forgot pass
        
        #fgpassbtn=Button(frame,text="Forgot password",font=("times new roman",10,"bold"),bd=3,borderwidth=0,fg='white',bg='black',activeforeground="white",activebackground="black")
        #fgpassbtn.place(x=75,y=370,width=160)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtemail.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel management system")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                           self.txtemail.get(),
                                                                           self.txtpass.get()
                                                                            ))
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid email & password")
            else:
                self.new_window=Toplevel(self.root)
                #Open hotel management system
                self.app=HotelManagementSystem(self.new_window)
            
            conn.commit()
            conn.close()
                
            




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
        self.app=Login_window(self.new_window)

            



if __name__=="__main__":
    main()
