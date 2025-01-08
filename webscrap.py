 
from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup 
  

myurl = 'http://books.toscrape.com/index.html'
  
uClient = uReq(myurl) 
  
page_html = uClient.read() 
uClient.close() 
  
page_soup = soup(page_html, "html.parser")

class webscrap(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("web books")
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

        bookshelf = page_soup.findAll( 
                                "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"}) 
  

        filename = ("Books.csv") 
        f = open(filename, "w") 
  
        headers = "Book title, Price\n"
        f.write(headers) 
        list_books=[]
        for books in bookshelf: 
  
    
            book_title = books.h3.a["title"]
            list_books.append(book_title)
            
  
    
            book_price = books.findAll("p", {"class": "price_color"}) 
            price = book_price[0].text.strip() 
  
            print("Title of the book :" + book_title) 
            print("Price of the book :" + price) 
  
            f.write(book_title + "," + price+"\n") 
  
            f.close()
       insertinto(list_books)
       self.listTree = ttk.Treeview(self, height=13,columns=('Book Name'))
       self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
       self.listTree.configure(yscrollcommand=self.vsb.set)
       self.listTree.heading("#0", text='Sno.', anchor='center')
       self.listTree.column("#0", width=120, anchor='center')
       self.listTree.heading("Book Name", text='Book Name')
       self.listTree.column("Book Name", width=200, anchor='center')
       self.listTree.place(x=40, y=200)
       self.vsb.place(x=763,y=200,height=287)
       ttk.Style().configure("Treeview", font=('Courier new', 15))
webscrap().mainloop()
