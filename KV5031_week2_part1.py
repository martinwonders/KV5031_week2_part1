class BADAnimal:
    def __init__(self, name: str, is_dog: bool, breed_or_color: str):
        self.name = name
        self.is_dog = is_dog # Boolean flag: True if dog, False if cat
        self.breed_or_color = breed_or_color # Either breed for dog, or color for cat

    def speak(self):
        if self.is_dog:
            return "Woof!"
        else:
            return "Meow!"

    def display_info(self):
        if self.is_dog:
            print(f"Name: {self.name}, Species: Dog, Breed: {self.breed_or_color}")
        else:
            print(f"Name: {self.name}, Species: Cat, Color: {self.breed_or_color}")

# Example usage:
dog = BADAnimal("Buddy", True, "Golden Retriever")
cat = BADAnimal("Whiskers", False, "Black")

# Display information and speak
dog.display_info() # Output: Name: Buddy, Species: Dog, Breed: Golden Retriever
print(dog.speak()) # Output: Woof!
print("---")
cat.display_info() # Output: Name: Whiskers, Species: Cat, Color: Black
print(cat.speak()) # Output: Meow!