from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Book")
        self.maxsize(800,500)
        self.minsize(800,500)
        self.canvas = Canvas(width=800, height=500, bg='pink')
        self.canvas.pack()
        l1=Label(self,text="Search Library",bg='gray', font=("Courier new",20,'bold')).place(x=290,y=20)
        l = Label(self, text="Search By",bg='gray', font=("Courier new", 15, 'bold')).place(x=60, y=96)
        def insertinto(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))
        def g_b():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+g.get())
            elif g.get() == 'Book Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='password')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where name LIKE %s",['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insertinto(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Name is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something went wrong")
            elif g.get() == 'Author Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='password')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where author LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insertinto(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Author Name not found")
                except Error:
                    messagebox.showerror("Error","Something went wrong")
            elif g.get() == 'Book Id':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='password')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where book_id LIKE %s", ['%'+f.get()+'%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insertinto(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Id is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error","Something went wrong")
        b=Button(self,text="Find",width=15,bg='gray',font=("Courier new",10,'bold'),command=g_b).place(x=460,y=135)
        c=ttk.Combobox(self,textvariable=g,values=["Book Name","Author Name","Book Id"],width=40,state="readonly").place(x = 180, y = 100)
        en = Entry(self,textvariable=f,width=43).place(x=180,y=155)
        la = Label(self, text="Enter",bg='gray', font=("Courier new", 15, 'bold')).place(x=100, y=150)



        self.listTree = ttk.Treeview(self, height=13,columns=('Book Name', 'Book Author', 'Availability'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Book ID', anchor='center')
        self.listTree.column("#0", width=120, anchor='center')
        self.listTree.heading("Book Name", text='Book Name')
        self.listTree.column("Book Name", width=200, anchor='center')
        self.listTree.heading("Book Author", text='Book Author')
        self.listTree.column("Book Author", width=200, anchor='center')
        self.listTree.heading("Availability", text='Availability')
        self.listTree.column("Availability", width=200, anchor='center')
        self.listTree.place(x=40, y=200)
        self.vsb.place(x=763,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Courier new', 15))#Times new Roman

Search().mainloop()