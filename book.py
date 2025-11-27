class publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("publisher",self.name)
class book(publisher):
    def __init__(self,name,title,authour):
       super().__init__(name)
       self.title=title
       self.authour=authour
    def display(self):
        super().display()
        print("title", self.title)
        print("authour", self.authour)
class python(book):
    def __init__(self,name,title,authour,price,no_of_pages):
        super().__init__(name,title,authour)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        super().display()
        print("price",self.price)
        print("no_of_pages",self.no_of_pages)
name=input("enter publisher name :")
title=input("enter book title :")
authour=input("enter authour name :")
price=input("enter price of book  :")
pages=input("enter no of pages  :")
book=python(name,title,authour,price,pages)
book.display()
