from tkinter import *
from tkinter import ttk 
from tkcalendar import Calendar,DateEntry
import time, datetime
import mysql.connector
import tkinter.messagebox
import traceback
win= Tk()
win.title("Hospital Management System")
win.geometry("1080x700")
mydb = mysql.connector.connect(
                        host="localhost",
                        user = "root",
                        password="root",
                        database = "HOSPITAL"
                        )
cur = mydb.cursor()

class Application:

        def __init__(self, master):
                
                self.master=master
                win = Frame(self.master,height=700)
                # win.pack_propagate(0)
                win.pack(fill='both', expand='True')
                # win.pack()
                global photo1
                global photo2
                global photo3
                global photo4
                label1 = Label(win,text="HOSPITAL MANAGEMENT SYSTEM",bg="red",fg="white",font="arial 40 bold")
                label1.place(x=0,y=0)
                label1.pack(fill=X)

                def clock():
                        hrs = time.strftime("%I")  
                        min = time.strftime("%M")  
                        sec = time.strftime("%S")  
                        am_pm = time.strftime("%p")
                        day = time.strftime("%a")
                        days = time.strftime("%d")
                        mnth = time.strftime("%b")
                        yrs = time.strftime("%j")
                        date = (hrs + ":" + min + ":" + sec + " " + am_pm + "\n" +day +", " + days + " " + mnth + " " + yrs )
                        # date = datetime.datetime.today().strftime ('%d %b %Y')
                        label2 = Label(win,text=date,bg="red",fg="white",font="arial 15 bold")
                        label2.place(x=850,y=100)
                        label2.after(1000,clock)
                clock()

                button=Button(win,text="EXIT" ,width="15",command=quit, bg="brown", font=" arial 10 bold",fg="white" )
                button.place(x=0,y=80)

                photo1 = tkinter.PhotoImage(file = 'img\doctor.png')
                photo1 = photo1.subsample(3,3)                 
                button1 = Button(master,image=photo1,text="DOCTOR",borderwidth=0,command=self.doctor)
                Button(master,text="DOCTOR",borderwidth=0,font="arial 20 bold",width=10,height=0,fg="Black",command=self.doctor).place(x=230,y=270)
                button1.place(x=230,y=100)
                
                photo2 = tkinter.PhotoImage(file = 'img\patient.png')
                photo2= photo2.subsample(3,3)                 
                button2 = Button(master,text="PATIENTS", command=self.patient,image=photo2,borderwidth=0)
                Button(master,text="PATIENT",borderwidth=0,font="arial 20 bold",width=10,height=0,fg="Black",command=self.patient).place(x=600,y=270)
                button2.place(x=600,y=100)

                photo3 = tkinter.PhotoImage(file = 'img\Appointment.png')
                photo3 = photo3.subsample(3,3)                 
                button3 = Button(master,text="APPOINTMENT", command=self.appointment,image=photo3,borderwidth=0)
                Button(master,text="APPOINTMENT",borderwidth=0,font="arial 20 bold",width=12,height=0,fg="Black",command=self.appointment).place(x=210,y=530)
                button3.place(x=230,y=360)

                photo4 = tkinter.PhotoImage(file = 'img\About.png')
                photo4 = photo4.subsample(4,4)                 
                button4 = Button(master,text="ABOUT US",image=photo4,borderwidth=0,command=self.aboutus)
                Button(master,text="ABOUT US",borderwidth=0,font="arial 20 bold",width=10,height=0,fg="Black",command=self.aboutus).place(x=600,y=530)
                button4.place(x=600,y=360)
        
        def patient(self):
                # mas=Tk()
                # mas.geometry("1080x700")
                mas=self.master
                frame = Frame(mas,width=1400,height=700)
                mas.title("Hospital Management System")
                frame.pack( fill = "both", expand = True)
                frame.place(x=0,y=0)
                self.label = Label(frame,text="MANAGE PATIENT",bg="red",fg="white",font=" arial 40 bold")
                self.label.place(x=350,y=0)
               


                def search():
                        self.ser=self.find.get()
                        qr2 = ("SELECT * from PATIENT where ID like '"+self.ser+"' OR NAME like '"+self.ser+"'")
                        cur.execute(qr2)
                        res = cur.fetchall()
                        if res==[]:
                                tkinter.messagebox.showinfo("Warning", "No record found")

                        for rec in res:
                                self.var1=rec[0]
                                self.var2=rec[1]
                                self.var3=rec[2]
                                self.var4=rec[3]
                        self.id.delete(0,'end')
                        self.name.delete(0,'end')
                        self.addr.delete(0,'end')
                        self.cont.delete(0,'end')
                      
                        self.id.insert(0,self.var1)
                        self.name.insert(0,self.var2)
                        self.addr.insert(0,self.var3)
                        self.cont.insert(0,self.var4)

                def add():
                        self.val1 = str(self.id.get())
                        self.val2 = str(self.name.get())
                        self.val3 = str(self.addr.get())
                        self.val4 = str(self.cont.get())
                        
                        try:

                                if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '':
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                elif not self.val1.isdigit() or not self.val4.isdigit():
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Valid Id Number")

                                else:
                                        qr = "INSERT INTO PATIENT VALUES('"+self.id.get()+"','"+self.name.get()+"','"+self.addr.get()+"','"+self.cont.get()+"')"
                                        cur.execute(qr)                        
                                        if cur.rowcount!=0:
                                                tkinter.messagebox.showinfo("Successfully", "Data Added")
                        except:
                                tkinter.messagebox.showinfo("Warning", "Allready registered")

                        mydb.commit()

                def reset():
                        self.id.delete(0,'end')
                        self.name.delete(0,'end')
                        self.addr.delete(0,'end')
                        self.cont.delete(0,'end')
                        self.find.delete(0,'end')
                                
                def show():

                        self.root = Tk()
                        self.root.geometry("717x500")
                        self.root.title("Hospital Management System")
                        rlabel = Label(self.root,text="LIST OF PATIENTS",bg="red",fg="white",font=" arial 40 bold" )
                        # rlabel.pack(fill=x)
                        rlabel.grid(row=0,columnspan=100,pady=50,padx=200)
                        Label(self.root,text="ID NO.",bg="red", width=10, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=0,sticky="n")
                        Label(self.root,text="NAME",bg="red", width=10, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=1)
                        Label(self.root,text="ADDRESS",bg="red", width=10, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=2)
                        Label(self.root,text="CONTACT",bg="red", width=10, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=3)
                        button1=Button(self.root,text="BACK" ,width="15",command=self.root.destroy, bg="brown", font=" arial 10 bold",fg="white" )
                        button1.grid(row=0,column=0)
                        qr="select * from PATIENT"
                        cur.execute(qr)
                        result=cur.fetchall()
                        lst = result
                        for i in range(len(lst)):
                                for j in range(len(lst[0])):
                                        e = Label(self.root,text=lst[i][j],bg="pink", width=10, fg='blue', borderwidth = 3, relief="sunken",
                                                                font=('Arial',20,'bold'))
                                        e.grid(row=i+2,column=j)

                def delete():       
                        self.var=self.id.get()         
                        qr="DELETE FROM PATIENT WHERE ID ='"+self.var+"';"
                        cur.execute(qr)
                        self.find.delete(0,'end')
                        self.id.delete(0,'end')
                        self.name.delete(0,'end')
                        self.addr.delete(0,'end')
                        self.cont.delete(0,'end')
                        if cur.rowcount==0:
                                tkinter.messagebox.showinfo("Warning", "Record not deleted")
                        else:
                                tkinter.messagebox.showinfo("Successfully", "Record deleted successfully")

                def update():        
                        try:  
                                if self.id.get() == '' or self.name.get() == '' or self.addr.get() == '' or self.cont.get() == '':
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                elif not self.id.get().isdigit() or not self.cont.get().isdigit():
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Valid Id Number")    
                                
                                else:
                                        qr="UPDATE PATIENT SET NAME = '"+self.name.get()+"', ADDRESS = '"+self.addr.get()+"' ,CONT = '"+self.cont.get()+"' WHERE ID = '"+self.id.get()+"';"
                                        cur.execute(qr)
                                        if cur.rowcount==0:
                                                tkinter.messagebox.showinfo("Warning", "ID Number Not Found")
                                        else:
                                                tkinter.messagebox.showinfo("Successfully", "Record Updated Successfully") 

                        except Exception:
                                traceback.print_exc()
                                tkinter.messagebox.showinfo("Warning", "ID Number Not Found")

                def quit():
                        self.root.destroy()

                                


                self.label0 = Label(frame,text="SEARCH PATIENT :",fg="Black", font="arial 20 bold")
                self.label0.place(x=200,y=100)
                self.find= Entry(frame, width="30", bd=5, font="arial 20 bold")
                self.find.insert(0,"ENTER ID OR NAME")
                self.find.place(x=500,y=100)
                
                self.label1 = Label(frame,text="PATIENT ID :",fg="Black", font="arial 20 bold")
                self.label1.place(x=230,y=200)
                self.id= Entry(frame, width="30", bd=5, font="arial 20 bold")
                self.id.place(x=500,y=200)

                self.label2 = Label(frame,text="NAME :",fg="Black", font="arial 20 bold")
                self.label2.place(x=230,y=300)
                self.name= Entry(frame, width="30", bd=5, font="arial 20 bold")
                self.name.place(x=500,y=300)
                
                self.label3 = Label(frame,text="ADDRESS :",fg="Black", font="arial 20 bold")
                self.label3.place(x=230,y=400)
                self.addr= Entry(frame, width="30", bd=5, font="arial 20 bold")
                self.addr.place(x=500,y=400)

                self.label4 = Label(frame,text="CONTACT :",fg="Black", font="arial 20 bold")
                self.label4.place(x=230,y=500)
                self.cont= Entry(frame, width="30", bd=5, font="arial 20 bold")
                self.cont.place(x=500,y=500)

                button1=Button(frame,text="BACK" ,width="15",command=frame.destroy, bg="brown", font=" arial 10 bold",fg="white" )
                button1.place(x=0,y=80)
                button2=Button(frame,text="ADD" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=add)
                button2.place(x=400,y=600)
                button3=Button(frame,text="RESET" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=reset)
                button3.place(x=0,y=180)
                button4=Button(frame,text="SEARCH" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=search)
                button4.place(x=0,y=130)
                button5=Button(frame,text="DELETE" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=lambda:[delete(), quit()])
                button5.place(x=800,y=600)
                button6=Button(frame,text="SHOW" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=show)
                button6.place(x=200,y=600)
                button7=Button(frame,text="UPDATE" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=update)
                button7.place(x=600,y=600)     

        def doctor(self):
                # master=Tk()
                # master.geometry("1080x700")
                mas=self.master
                master = Frame(mas,width=1400,height=700)
                mas.title("Hospital Management System")
                master.pack( fill = "both", expand = True)
                master.place(x=0,y=0)

                rlabel = Label(master,text="MANAGE DOCTOR",bg="red",fg="white",font=" arial 40 bold")
                rlabel.place(x=350,y=0)


                def search():
                        self.ser=self.find.get()
                        qr2 = ("SELECT * from DOCTOR where ID like '"+self.ser+"' OR NAME like '"+self.ser+"' OR SPECIALIZE like '"+self.ser+"'")
                        cur.execute(qr2)
                        res = cur.fetchall()
                        if res==[]:
                                tkinter.messagebox.showinfo("Warning", "No record found")

                        for rec in res:
                                self.var1=rec[0]
                                self.var2=rec[1]
                                self.var3=rec[2]
                                self.var4=rec[3]
                        self.id.delete(0,'end')
                        self.name.delete(0,'end')
                        self.specialize.delete(0,'end')
                        self.cont.delete(0,'end')
                      
                        self.id.insert(0,self.var1)
                        self.name.insert(0,self.var2)
                        self.specialize.insert(0,self.var3)
                        self.cont.insert(0,self.var4)

                def add():
                        self.val1 = str(self.id.get())
                        self.val2 = str(self.name.get())
                        self.val3 = str(self.specialize.get())
                        self.val4 = str(self.cont.get())
                        
                        try:

                                if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '':
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                elif not self.val1.isdigit() or not self.val4.isdigit():
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Valid Id Number")

                                else:
                                        qr = "INSERT INTO DOCTOR VALUES('"+self.id.get()+"','"+self.name.get()+"','"+self.specialize.get()+"','"+self.cont.get()+"')"
                                        cur.execute(qr)                        
                                        if cur.rowcount!=0:
                                                tkinter.messagebox.showinfo("Successfully", "Data Added")
                        except:
                                tkinter.messagebox.showinfo("Warning", "Allready registered")

                        mydb.commit()



                def reset():
                        self.id.delete(0,'end')
                        self.name.delete(0,'end')
                        self.specialize.delete(0,'end')
                        self.cont.delete(0,'end')
                        self.find.delete(0,'end')
                                

                def show():

                        self.root = Tk()
                        self.root.geometry("1000x500")
                        self.root.title("Hospital Management System")
                        rlabel = Label(self.root,text="LIST OF DOCTORS",bg="red",fg="white",font=" arial 40 bold" )
                        rlabel.grid(row=0,columnspan=100,pady=30,padx=200)
                        Label(self.root,text="ID NO.",bg="red", width=14, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=0,sticky="n")
                        Label(self.root,text="NAME",bg="red", width=14, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=1)
                        Label(self.root,text="SPECIALIZATION",bg="red", width=14, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=2)
                        Label(self.root,text="CONTACT",bg="red", width=14, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=3)
                        button1=Button(self.root,text="BACK" ,width=14,command=self.root.destroy, bg="brown", font=" arial 10 bold",fg="white" )
                        button1.grid(row=0,column=0)
                        qr="select * from doctor"
                        cur.execute(qr)
                        result=cur.fetchall()
                        lst = result
                        for i in range(len(lst)):
                                for j in range(len(lst[0])):
                                        e = Label(self.root,text=lst[i][j],bd=5,bg="pink", width=14, fg='blue', borderwidth = 3, relief="sunken",
                                                                font=('Arial',20,'bold'))
                                        e.grid(row=i+2,column=j)


                def delete():       
                        self.var=self.id.get()         
                        qr="DELETE FROM DOCTOR WHERE ID ='"+self.var+"';"
                        cur.execute(qr)
                        self.find.delete(0,'end')
                        self.id.delete(0,'end')
                        self.name.delete(0,'end')
                        self.specialize.delete(0,'end')
                        self.cont.delete(0,'end')
                        if cur.rowcount==0:
                                tkinter.messagebox.showinfo("Warning", "Record not deleted")
                        else:
                                tkinter.messagebox.showinfo("Successfully", "Record deleted successfully")


                def update():        
                        try:  
                                if self.id.get() == '' or self.name.get() == '' or self.specialize.get() == '' or self.cont.get() == '':
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                elif not self.id.get().isdigit() or not self.cont.get().isdigit():
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Valid Id Number")    
                                
                                else:
                                        qr="UPDATE DOCTOR SET NAME = '"+self.name.get()+"', SPECIALIZE = '"+self.specialize.get()+"' ,CONT = '"+self.cont.get()+"' WHERE ID = '"+self.id.get()+"';"
                                        cur.execute(qr)
                                        if cur.rowcount==0:
                                                tkinter.messagebox.showinfo("Warning", "ID Number Not Found")
                                        else:
                                                tkinter.messagebox.showinfo("Successfully", "Record Updated Successfully") 

                        except Exception:
                                traceback.print_exc()
                                tkinter.messagebox.showinfo("Warning", "ID Number Not Found")



                def quit():
                        self.root.destroy()

                                


                self.label0 = Label(master,text="SEARCH DOCTOR :",fg="Black", font="arial 20 bold")
                self.label0.place(x=200,y=100)
                self.find= Entry(master, width="30", bd=5, font="arial 20 bold")
                self.find.insert(0,"ENTER ID OR NAME OR SPECIALIZATION")
                self.find.place(x=500,y=100)
                
                self.label1 = Label(master,text="ID NO. :",fg="Black", font="arial 20 bold")
                self.label1.place(x=230,y=200)
                self.id= Entry(master, width="30", bd=5, font="arial 20 bold")
                self.id.place(x=500,y=200)
                self.label2 = Label(master,text="NAME :",fg="Black", font="arial 20 bold")
                self.label2.place(x=230,y=300)
                self.name= Entry(master, width="30", bd=5, font="arial 20 bold")
                self.name.place(x=500,y=300)
                
                self.label3 = Label(master,text="SPECIALZATION :",fg="Black", font="arial 20 bold")
                self.label3.place(x=230,y=400)
                self.specialize= Entry(master, width="30", bd=5, font="arial 20 bold")
                self.specialize.place(x=500,y=400)
                self.label4 = Label(master,text="CONTACT :",fg="Black", font="arial 20 bold")
                self.label4.place(x=230,y=500)
                self.cont= Entry(master, width="30", bd=5, font="arial 20 bold")
                self.cont.place(x=500,y=500)

                button1=Button(master,text="BACK" ,width="15",command=master.destroy, bg="brown", font=" arial 10 bold",fg="white" )
                button1.place(x=0,y=80)
                button2=Button(master,text="ADD" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=add)
                button2.place(x=400,y=600)
                button3=Button(master,text="RESET" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=reset)
                button3.place(x=0,y=180)
                button4=Button(master,text="SEARCH" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=search)
                button4.place(x=0,y=130)
                button5=Button(master,text="DELETE" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=lambda:[delete(), quit()])
                button5.place(x=800,y=600)
                button6=Button(master,text="VIEW" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=show)
                button6.place(x=200,y=600)
                button7=Button(master,text="UPDATE" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=update)
                button7.place(x=600,y=600)

        def appointment(self):
                # master=Tk()
                # master.geometry("1080x650")
                # master.title("Hospital Management System")

                mas=self.master
                master = Frame(mas,width=1400,height=700)
                mas.title("Hospital Management System")
                master.pack( fill = "both", expand = True)
                master.place(x=0,y=0)

                rlabel = Label(master,text="MANAGE APPOINTMENTS",bg="red",fg="white",font=" arial 40 bold")
                rlabel.place(x=200,y=0)

                def add():
                        self.val1 = str(self.pname.get())
                        self.val2 = str(self.dname.get())
                        self.val3 = str(self.date.get())
                        self.val4 = str(self.time.get())
                        
                        try:

                                if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '':
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                else:
                                        qr = "INSERT INTO APPOINTMENT VALUES('"+self.pname.get()+"','"+self.dname.get()+"','"+self.date.get()+" "+self.time.get()+"')"
                                        cur.execute(qr)                        
                                        if cur.rowcount!=0:
                                                tkinter.messagebox.showinfo("Successfully", "Appointment Added")
                        except:
                                tkinter.messagebox.showinfo("Warning", "Someone allready take appointment on this date.")

                        mydb.commit()

                def reset():
                        self.pname.delete(0,'end')
                        self.dname.delete('end')
                        self.date.delete('end')
                        self.time.delete('end')
                                
                def show():

                        self.root = Tk()
                        self.root.geometry("800x500")
                        self.root.title("Hospital Management System")
                        rlabel = Label(self.root,text="APPOINTMENTS",bg="red",fg="white",font=" arial 40 bold" )
                        rlabel.grid(row=0,columnspan=100,pady=50,padx=250)
                        Label(self.root,text="PATIENT",bg="red", width=15, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=0,sticky="n")
                        Label(self.root,text="DOCTOR",bg="red", width=15, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=1)
                        Label(self.root,text="ADDRESS",bg="red", width=15, fg='white',
                                                                                        font=('Arial',20,'bold')).grid(row=1,column=2)
                        button1=Button(self.root,text="BACK" ,width="15",command=self.root.destroy, bg="brown", font=" arial 10 bold",fg="white" )
                        button1.grid(row=0,column=0)
                        qr="select * from APPOINTMENT"
                        cur.execute(qr)
                        result=cur.fetchall()
                        lst = result
                        for i in range(len(lst)):
                                for j in range(len(lst[0])):
                                        e = Label(self.root,text=lst[i][j],bd=5,bg="pink", width=15, fg='blue', borderwidth = 3, relief="sunken",
                                                                font=('Arial',20,'bold'))
                                        e.grid(row=i+2,column=j)

                def delete():       
                        self.var=(str(self.date.get())+" "+str(self.time.get())) 
                        print(self.var)        
                        qr="DELETE FROM APPOINTMENT WHERE DATETIME ='"+self.var+"';"
                        cur.execute(qr)
                        self.pname.delete(0,'end')
                        self.dname.delete('end')
                        self.date.delete('end')
                        self.time.delete('end')
                        if cur.rowcount==0:
                                tkinter.messagebox.showinfo("Warning", "Record not deleted")
                        else:
                                tkinter.messagebox.showinfo("Successfully", "Record deleted successfully")

                def update():        
                        try:  
                                if self.pname.get() == '' or self.dname.get() == '' or self.date.get() == '' or self.time.get() == '':
                                        tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                else:
                                        qr="UPDATE APPOINTMENT SET PNAME = '"+self.pname.get()+"', DNAME = '"+self.dname.get()+"' ,DATETIME = '"+self.date.get()+" "+self.time.get()+"' WHERE DATETIME = '"+self.date.get()+" "+self.time.get()+"';"
                                        cur.execute(qr)
                                        if cur.rowcount==0:
                                                tkinter.messagebox.showinfo("Warning", "Someone allready take appointment on this date.")
                                        else:
                                                tkinter.messagebox.showinfo("Successfully", "Record Updated Successfully") 

                        except Exception:
                                traceback.print_exc()
                                tkinter.messagebox.showinfo("Warning", "Someone allready take appointment on this date.")
                
                def get():
                        qr="SELECT * FROM DOCTOR"
                        cur.execute(qr)
                        res=cur.fetchall() 
                        list=[]
                        for rec in res:
                                list.append("Dr. "+str(rec[1]))
                        return list

                def quit():
                        self.root.destroy()

                self.label1 = Label(master,text="PATIENT NAME :",fg="Black", font="arial 20 bold")
                self.label1.place(x=230,y=100)
                self.pname= Entry(master, width="30", bd=5, font="arial 20 bold")
                self.pname.place(x=500,y=100)

                self.label2 = Label(master,text="DOCTOR NAME :",fg="Black", font="arial 20 bold")
                self.label2.place(x=230,y=200)

                n = tkinter.StringVar() 
                self.dname = ttk.Combobox(master, textvariable = n, width="29", font="arial 20 bold") 
                self.dname['values'] =get()
                self.dname.place(x=500,y=200)
                self.dname.current(1) 
   
                self.label3 = Label(master,text="DATE :",fg="Black", font="arial 20 bold")
                self.label3.place(x=230,y=300)
                self.date = DateEntry(master,bg="darkblue",fg="BLACK",year=2021, width="29", bd=5, font="arial 20 bold")
                self.date.place(x=500,y=300)

                self.label4 = Label(master,text="TIME :",fg="Black", font="arial 20 bold")
                self.label4.place(x=230,y=400)
                m = tkinter.StringVar() 
                self.time = ttk.Combobox(master, textvariable = m, width="29", font="arial 20 bold") 
                self.time['values'] = ( '12:00 PM',
                                        '1:00 PM', 
                                        '2:00 PM', 
                                        '3:00 PM', 
                                        '4:00 PM', 
                                        '5:00 PM', 
                                        '6:00 PM', ) 
                self.time.place(x=500,y=400)
                self.time.current(1) 

                button1=Button(master,text="BACK" ,width="15",command=master.destroy, bg="brown", font=" arial 10 bold",fg="white" )
                button1.place(x=0,y=80)
                button2=Button(master,text="ADD" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=add)
                button2.place(x=400,y=500)
                button3=Button(master,text="RESET" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=reset)
                button3.place(x=0,y=130)
                button5=Button(master,text="DELETE" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=lambda:[delete(),quit()])
                button5.place(x=800,y=500)
                button6=Button(master,text="SHOW" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=show)
                button6.place(x=200,y=500)
                button7=Button(master,text="UPDATE" ,width="15", bg="brown", font=" arial 10 bold",fg="white", command=update)
                button7.place(x=600,y=500)     

        def aboutus(self):
                mas=self.master
                frame = Frame(mas,width=1400,height=700)
                mas.title("Hospital Management System")
                frame.pack( fill = "both", expand = True)
                frame.place(x=0,y=0)
                global img
                img=tkinter.PhotoImage(file="img\devloper.png")
                img= img.subsample(3,3)
                Label(frame,image=img).place(x=100,y=50)
                Label(frame,text="Jatan",font="arial 20 bold",width=10,height=0,fg="Black").place(x=150,y=320)

obj=Application(win)
win.mainloop()