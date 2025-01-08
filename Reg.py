from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

class reg(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(1000, 417)
        self.minsize(1000, 417)
        self.title('Add Admin')
        self.canvas = Canvas(width=1000, height=417, bg='brown')
        self.canvas.pack()
        u = StringVar()
        n = StringVar()
        p = StringVar()


        def insert():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='password')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(user,name,password) values (%s,%s,%s)",[u.get(), n.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "Admin Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another admin?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'Reg.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Error", "Something went Wrong")

        Label(self, text='User Details', bg='gray', fg='black', font=('Courier new', 25, 'bold')).place(x=330, y=22)
        Label(self, text='Username:', bg='gray', font=('Courier new', 10, 'bold')).place(x=270, y=82)
        Entry(self, textvariable=u, width=30).place(x=400, y=84)
        Label(self, text='Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=270, y=130)
        Entry(self, textvariable=n, width=30).place(x=400, y=132)
        Label(self, text='Password:', bg='gray', font=('Courier new', 10, 'bold')).place(x=270, y=180)
        Entry(self, textvariable=p, width=30).place(x=400, y=182)
        Button(self, text="Submit", width=15, command=insert).place(x=430, y=220)
reg().mainloop()