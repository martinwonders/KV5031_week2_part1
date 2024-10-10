# Bad aggregation example for Book class
class Book:
    def __init__(self, title, author_name, author_email, author_phone,
                 publisher_name, publisher_address, publisher_email,
                 publisher_phone, isbn, num_pages):
        self.title = title
        self.author_name = author_name
        self.author_email = author_email
        self.author_phone = author_phone
        self.publisher_name = publisher_name
        self.publisher_address = publisher_address
        self.publisher_email = publisher_email
        self.publisher_phone = publisher_phone
        self.isbn = isbn
        self.num_pages = num_pages

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author_name}, Email: {self.author_email}, Phone: {self.author_phone}")
        print(f"Publisher: {self.publisher_name}, \ "
              f"Address: {self.publisher_address}, \ "
              f"Email: {self.publisher_email}, Phone: {self.publisher_phone}")
        print(f"ISBN: {self.isbn}")
        print(f"Number of Pages: {self.num_pages}")

# Creating a Book object with all details combined into one class
book = Book(
"The Great Gatsby",
"F. Scott Fitzgerald",
"fscott@example.com",
"123-456-7890",
"Scribner",
"123 Publisher Ave, New York, NY",
"contact@scribner.com",
"987-654-3210",
"9780743273565",
180
)
# Display book information
book.show_info()