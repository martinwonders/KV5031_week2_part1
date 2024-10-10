#Address class represents an address with street, city, and postal code
class Address:
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def get_address(self):
        return f"{self.street}, {self.city}, {self.postal_code}"


# Student class with name, home address, and term-time address as simple attributes
class Student:
    def __init__(self, name, home_address, term_address):
        self.name = name
        self.home_address = home_address # Aggregation: student Has a home address
        self.term_address = term_address # Aggregation: student Has a term address


    def show_info(self):
        print(f"Student Name: {self.name}")
        print("Home Address:")
        print(self.home_address.get_address())
        print("Term-Time Address:")
        print(self.term_address.get_address())

#Create separate Address objects for home and term-time addresses
home_address = Address("123 Main Street", "Hometown", "12345")
term_address = Address("456 College Ave", "University City", "67890")

# Creating a Student object with home and term-time addresses as object instances
student = Student("John Doe", home_address, term_address)

# Display student information
student.show_info()