class Address:
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def return_address(self):
        return f"{self.street}, {self.city}, {self.postal_code}"


class Author:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def return_info(self):
        return f"{self.name}, {self.email}, {self.phone}"

class Publisher:
    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

    def return_info(self):
        return f"{self.name}, {self.address.return_address()}, {self.email}, {self.phone}"


# Good aggregation example for Book class
class Book:
    def __init__(self, title, author, publisher, isbn, num_pages):

        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.num_pages = num_pages

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author.return_info()}")
        print(f"Publisher: {self.publisher.return_info()}")
        print(f"ISBN: {self.isbn}")
        print(f"Number of Pages: {self.num_pages}")

#Create and Address object for the publisher
publisher_address = Address("123 Publisher Ave", "New York", "NY")
#Create a publisher object and use the address
publisher = Publisher("Scribner", publisher_address, "contact@scribner.com", "987-654-3210")
#Create an Author object
author = Author("F. Scott Fitzgerald", "fscott@example.com", "123-456-7890")

# Creating a Book object with the author and publisher objects
book = Book( "The Great Gatsby", author, publisher, "9780743273565", 180)

# Display book information
book.show_info()