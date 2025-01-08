from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk

import mysql.connector
from mysql.connector import Error

py=sys.executable

class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(width=1366, height=768, bg='red')
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320,768)
        self.state('zoomed')
        self.title('LIBRARY MANAGEMENT SYSTEMS')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)
        messagebox.showinfo('Hello','welcome to library management system')
        def a_s():
            os.system('%s %s' % (py, 'Add_Student.py'))

        def a_b():
            os.system('%s %s' % (py, 'Add_Books.py'))

        def r_b():
            os.system('%s %s' % (py, 'remove_book.py'))

        def r_s():
            os.system('%s %s' % (py, 'Remove_student.py'))

        def i_b():
            os.system('%s %s' % (py, 'issueTable.py'))

        def ret():
            os.system('%s %s' % (py, 'ret.py'))

        def s_b():
            os.system('%s %s' % (py,'Search.py'))

        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to Logout?")
            if conf:
             self.destroy()
             #os.system('%s %s' % (py, 'Main.py'))
        def c_g():
            os.system('%s %s' % (py,'colour.py'))


      # def handle(event):
        #     if self.listTree.identify_region(event.x,event.y) == "separator":
        #         return "break"
        def add_user():
            os.system('%s %s' % (py, 'Reg.py'))
        def rem_user():
            os.system('%s %s' % (py, 'Rem.py'))
        def sest():
            os.system('%s %s' % (py,'Search_Student.py'))
        def remainder():
            os.system('%s %s' % (py,'email.py'))
        def book_scrap():
            os.system('%s %s' % (py,'webscrap.py'))



        self.listTree = ttk.Treeview(self,height=14,columns=('Student','Book','Issue Date','Return Date'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='ID')
        self.listTree.column("#0", width=50,minwidth=50,anchor='center')
        self.listTree.heading("Student", text='Student')
        self.listTree.column("Student", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Book", text='Book')
        self.listTree.column("Book", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Issue Date", text='Issue Date')
        self.listTree.column("Issue Date", width=125, minwidth=125,anchor='center')
        self.listTree.heading("Return Date", text='Return Date')
        self.listTree.column("Return Date", width=125, minwidth=125, anchor='center')
        self.listTree.place(x=320,y=360)
        self.vsb.place(x=1028,y=361,height=287)
        self.hsb.place(x=320,y=620,width=700)#320,650,700
        ttk.Style().configure("Treeview",font=('Times new Roman',15))

        list1 = Menu(self.mymenu, tearoff=0)
        list1.add_command(label="Student", command=a_s)
        list1.add_command(label="Book", command=a_b)
        list1.add_separator()
        list3 = Menu(self.mymenu, tearoff=0)
        list3.add_command(label = "Add admin",command = add_user)
        list3.add_command(label = "Remove admin",command = rem_user)
        list3.add_separator()

        self.mymenu.add_cascade(label='Add Tools', menu=list1)
        self.mymenu.add_cascade(label = 'Admin Tools', menu = list3)

        self.config(menu=self.mymenu)

        def ser():
            if(len(self.studid.get())==0):
                messagebox.showinfo("Error", "Empty Field!")
            else:

             try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='password')
                self.cursor = self.conn.cursor()
                change = int(self.studid.get())
                self.cursor.execute("Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,student s,book b where s.stud_id = bi.stud_id and b.book_id = bi.book_id and s.stud_id = %s",[change])
                pc = self.cursor.fetchall()
                if pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in pc:
                        self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4]))
                else:
                    messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued on this ID")
             except Error:
              messagebox.showerror("Error","Something Goes Wrong")
        def ent():
            if (len(self.bookid.get()) == 0):
                messagebox.showinfo("Error", "Empty Field!")
            else:
             try:
                self.conn = mysql.connector.connect(host='localhost',
                                                        database='library',
                                                            user='root',
                                                                password='password')
                self.myCursor =self.conn.cursor()
                book = int(self.bookid.get())
                self.myCursor.execute("Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,student s,book b where s.stud_id = bi.stud_id and b.book_id = bi.book_id and b.book_id = %s",[book])
                pc = self.myCursor.fetchall()
                if pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in pc:
                        self.listTree.insert("", 'end', text=row[0],values=(row[1], row[2], row[3], row[4]))
                else:
                    messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued")
             except Error:
                messagebox.showerror("Error", "Something Goes Wrong")

        def check():
            try:
                conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='password')
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z =mycursor.fetchone()
                if not z:
                    messagebox.showinfo("Error", "Please Register A user")
                    x = messagebox.askyesno("Confirm","Do you want to register a user")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'Reg.py'))
                else:
        
                    self.label3 = Label(self, text='LIBRARY MANAGEMENT SYSTEM',fg='black',bg="pink" ,font=('Courier new', 30, 'bold'))
                    self.label3.place(x=400, y=22)
                    self.label4 = Label(self, text="ENTER STUDENT ID",bg="pink", font=('Courier new', 18,'underline','bold'))
                    self.label4.place(x=75, y=107)
                    self.studid = Entry(self, textvariable=self.a, width=90)
                    self.studid.place(x=330, y=110)
                    self.srt = Button(self, text='Search', width=15, font=('arial', 10),command = ser).place(x=1216, y=106)
                    self.label5 = Label(self, text="ENTER BOOK ID",bg="pink", font=('Courier new', 18,'underline', 'bold'))
                    self.label5.place(x=75, y=150)
                    self.bookid = Entry(self, textvariable=self.b, width=90)
                    self.bookid.place(x=330, y=160)
                    self.brt = Button(self, text='Find', width=15, font=('arial', 10),command = ent).place(x=1216, y=165)#1000,150
                    self.label6 = Label(self, text="DETAILS",bg="pink",  font=('Courier new', 15, 'underline', 'bold'))
                    self.label6.place(x=650, y=300)
                    self.button = Button(self, text='Search Student', width=25, font=('Courier new', 10), command=sest).place(x=240,y=250)
                    self.button = Button(self, text='Search Book', width=25, font=('Courier new', 10), command=s_b).place(x=520,y=250)
                    self.brt = Button(self, text="Issue Book", width=15, font=('Courier new', 10), command=i_b).place(x=800, y=250)
                    self.brt = Button(self, text="Return Book", width=15, font=('Courier new', 10), command=ret).place(x=1000, y=250)
                    self.brt = Button(self, text="LOGOUT", width=15,bg="red", font=('Courier new', 10), command=log).place(x=1150, y=600)
                    self.label7= Label(self,text='play this game',bg='blue',font=('Courier new',15,'bold'))
                    self.label7.place(x=75,y=660)
                    self.label8= Label(self,text='bored?',bg='orange',font=('Courier new',15,'bold'))
                    self.label8.place(x=75,y=645)
                    self.brt = Button(self, text="Colour game",width=15,bg="red",font=('Courier new',10), command=c_g).place(x=75,y=690)
                    self.label9=Label(self,text='Remaind the student',bg='orange',font=('Courier new',15,'bold'))
                    self.label9.place(x=75,y=700)
                    self.brt= Button(self, text='remainder',width=15,bg='blue',font=('Courier new',15,'bold'),command=remainder).place(x=75,710)
                    self.label10=Label(self,text='Books online',bg='orange',font=('Courier new',15,'bold'))
                    self.label10.place(x=75,y=720)
                    self.brt= Button(self, text='search',width=15,bg='blue',font=('Courier new',15,'bold'),command=remainder).place(x=75,730)
            except Error:
                messagebox.showerror("Error", "Something Went Wrong")
        check()

MainWin().mainloop()
