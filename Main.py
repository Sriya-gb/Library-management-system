from tkinter import *
from tkinter import messagebox
import os
import mysql.connector
from mysql.connector import Error
py=sys.executable

class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.configure(bg="orange")
        self.title("LIBRARY MANAGEMENT SYSTEM")

        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME" )
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID PASSWORD")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='password')
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admin` where user= %s AND password = %s ',(user,password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'options.py'))
                    else:
                        messagebox.showinfo('Error', 'Username and password not found')
                except Error:
                    messagebox.showinfo('Error',"Something went Wrong,Try again")

        def check():


                    self.label = Label(self, text="LOGIN", bg = 'gray' , fg = 'black', font=("courier-new", 24,'bold'))
                    self.label.place(x=550, y=90)
                    self.label1 = Label(self, text="User-Id" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label1.place(x=370, y=180)
                    self.user_text = Entry(self, textvariable=self.a, width=45)
                    self.user_text.place(x=480, y=190)
                    self.label2 = Label(self, text="Password" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label2.place(x=340, y=250)
                    self.pass_text = Entry(self, show='$', textvariable=self.b, width=45)
                    self.pass_text.place(x=480, y=255)
                    self.butt = Button(self, text="Login",bg ='white', font=10, width=8, command=chex).place(x=580, y=300)
                    self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM", bg='gray', fg='black', font=("courier-new", 24, 'bold'))
                    self.label3.place(x=350, y=30)


        check()

Lib().mainloop()