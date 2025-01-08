from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys
py = sys.executable

class Add(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('Add Book')
        self.canvas = Canvas(width=500, height=500, bg='orange')
        self.canvas.pack()
        b = StringVar()
        c = StringVar()
        def b_q():
            if len(b.get()) == 0 or len(c.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                g = 'YES'
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                            database='library',
                                                                user='root',
                                                                    password='password')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into book(name,author,availability) values (%s,%s,%s)",[b.get(),c.get(),g])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another book?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Books.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Error","Something went wrong")
        Label(self, text='').pack()
        Label(self, text='Book Details:',bg='purple',fg='red',font=('Courier new', 20, 'bold')).place(x=150, y=70)
        Label(self, text='').pack()
        Label(self, text='Book Name:',bg='gray',fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=b, width=30).place(x=170, y=182)
        Label(self, text='Book Author:',bg='green',fg='yellow', font=('Courier new', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=c, width=30).place(x=170, y=232)
        Button(self, text="Submit", command=b_q).place(x=245, y=300)
Add().mainloop()