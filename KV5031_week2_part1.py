# Student class with name, home address, and term-time address as simple attributes
class Student:
    def __init__(self, name, home_street, home_city, home_postal_code, term_street, term_city, term_postal_code):
        self.name = name
        self.home_street = home_street
        self.home_city = home_city
        self.home_postal_code = home_postal_code
        self.term_street = term_street
        self.term_city = term_city
        self.term_postal_code = term_postal_code

    def show_info(self):
        print(f"Student Name: {self.name}")
        print("Home Address:")
        print(f"{self.home_street}, {self.home_city}, {self.home_postal_code}")
        print("Term-Time Address:")
        print(f"{self.term_street}, {self.term_city}, {self.term_postal_code}")

# Creating a Student object with home and term-time addresses as simple attributes
student = Student(
"John Doe",
"123 Main Street", "Hometown", "12345", # Home address
"456 College Ave", "University City", "67890" # Term-time address
)
# Display student information
student.show_info()