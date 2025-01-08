from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

class email(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(1000, 417)
        self.minsize(1000, 417)
        self.title('send email')
        self.canvas = Canvas(width=1000, height=417, bg='brown')
        self.canvas.pack()
        s_e = StringVar()
        r_e = StringVar()
        s_p = StringVar()
        mail = StringVar()
        def sendmail():
            
            # Python code to illustrate Sending mail from  
            # your Gmail account  

            import smtplib 
  
            # creates SMTP session 
            s = smtplib.SMTP('smtp.gmail.com', 587) 
  
            # start TLS for security 
            s.starttls() 
  
            # Authentication 
            s.login(s_e, s_p) 
  
            # message to be sent 
            message = mail
      
            # sending the mail 
            s.sendmail(s_e, r_e, message) 
  
            # terminating the session 
            s.quit()
    Label(self, text='email', bg='gray', fg='black', font=('Courier new', 25, 'bold')).place(x=330, y=22)
    Label(self, text='senders email', bg='gray', font=('Courier new', 10, 'bold')).place(x=270, y=82)
    Entry(self, textvariable=s_e, width=30).place(x=400, y=84)
    Label(self, text='recievers email', bg='gray', font=('Courier new', 10, 'bold')).place(x=270, y=130)
    Entry(self, textvariable=r_e, width=30).place(x=400, y=132)
    Label(self, text='senders password', bg='gray', font=('Courier new', 10, 'bold')).place(x=270, y=180)
    Entry(self, textvariable=s_p, width=30).place(x=400, y=182)
    Label(self, text='message', bg='gray', font=('Courier new', 10, 'bold')).place(x=270, y=210)
    Entry(self, textvariable=s_p, width=30).place(x=400, y=210)
    Button(self, text="Submit", width=15, command=sendmail).place(x=450, y=250)
email.mainloop()
