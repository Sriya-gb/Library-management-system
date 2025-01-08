from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(1200, 200)
        self.minsize(1200, 200)
        self.title("Remove Admin")
        self.canvas = Canvas(width=1200, height=200, bg='orange')
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='password')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where id = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","Admin Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error","Something went wrong")
        Label(self, text = "Enter Admin Id: ",bg='gray',fg='black',font=('Courier new', 15, 'bold')).place(x = 205,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 460,y = 44)
        Button(self, text='Remove', width=15, font=('arial', 10),command = ent).place(x=400, y = 90)



Rem().mainloop()