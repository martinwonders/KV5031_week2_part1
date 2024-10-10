class Animal:
    def __init__(self, name: str, colour: str):
        self.name = name
        self.colour = colour


class Dog(Animal):
    def __init__(self, name: str, colour: str, breed: str):
        super().__init__(name, colour)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def display_info(self):
        print(f"Name: {self.name}, Colour: {self.colour}, Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name: str, colour: str):
        super().__init__(name, colour)

    def speak(self):
        return "Meow!"

    def display_info(self):
        print(f"Name: {self.name}, Colour: {self.colour}")

# Example usage:
dog = Dog("Buddy", "Golden", "Golden Retriever")
cat = Cat("Whiskers", "Black")

# Display information and speak
dog.display_info() # Output: Name: Buddy, Species: Dog, Breed: Golden Retriever
print(dog.speak()) # Output: Woof!
print("---")
cat.display_info() # Output: Name: Whiskers, Species: Cat, Color: Black
print(cat.speak()) # Output: Meow!