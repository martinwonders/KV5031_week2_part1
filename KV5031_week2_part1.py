class Product:
    def __init__(self, title, year, price):
        self.title = title
        self.year = year
        self.price = price

class Book(Product):
    def __init__(self, title, author, year, price, ISBN):
        super().__init__(title, year, price)
        self.author = author
        self.ISBN = ISBN

    def print_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")
        print(f"ISBN: {self.ISBN}")


class DVD(Product):
    def __init__(self, title, year, price, duration):
        super().__init__(title, year, price)
        self.duration = duration

    def print_details(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")
        print(f"Duration: {self.duration}")

aBook = Book("The Big Book", "John Smith", "1981", "12.75", "1927323023299")
aDVD= DVD("The Shawshank Redemption", "1994", "10:00",  "2h:22m")

aBook.print_details()
print("-----------------")
aDVD.print_details()





