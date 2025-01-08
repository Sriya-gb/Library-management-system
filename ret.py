from tkinter import *
from tkinter import messagebox
import os,sys
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date
py = sys.executable


class ret(Tk):
    def __init__(self):
        super().__init__()
        self.title("Return Book")
        self.maxsize(1200,350)
        self.minsize(1200,350)
        self.canvas = Canvas(width=1200, height=350, bg='red')
        self.canvas.pack()
        self.cal = 0
        a = StringVar()

        def r_b():
            if len(a.get()) == '0':
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                        user='root',
                                                        password='password')
                    self.mycursor = self.conn.cursor()

                    self.mycursor.execute("Select book_id from issue_book where return_date = '' and book_id = %s",[a.get()])
                    temp = self.mycursor.fetchone()
                    if temp:
                        self.mycursor.execute("update book set availability ='YES' where book_id = %s", [a.get()])
                        self.conn.commit()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("update issue_book set return_date = %s where book_id = %s", [idate,a.get()])
                        self.conn.commit()
                        self.mucursor.excecute('SELECT DATEDIFF(day, issue_date, return_date) from issue_book where book_id=%s',[a.get()])
                        fee=self.mycursor.fetchone()
                        self.conn.close()
                        messagebox.showinfo('Info', ('Succesfully Returned. fee to be paid is',fee))
                        d = messagebox.askyesno("Confirm", "Return more books?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'ret.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued")
                except Error:
                    messagebox.showerror("Error","Something went Wrong")
        Label(self, text='Return Book', fg='red',font=('arial', 35, 'bold')).pack()
        Label(self, text='Enter Book ID', font=('Comic Scan Ms', 15, 'bold')).place(x=280, y=120)#x inc right,y inc down
        Entry(self, textvariable=a, width=40).place(x=400, y=124)
        Button(self, text="Return", width=25, command=r_b).place(x=420, y=180)
ret().mainloop()
