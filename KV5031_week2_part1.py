class BADAnimal:
    def __init__(self, name: str, is_dog: bool, is_cat: bool, breed_or_color: str):
        self.name = name
        self.is_dog = is_dog # Boolean flag: True if dog, False if cat or tortoise
        self.is_cat = is_cat # Boolean flag: True if cat, False if dog or tortoise
        self.breed_or_color = breed_or_color # Either breed for dog, or color for cat and tortoise

    def speak(self):
        if self.is_dog:
            return "Woof!"
        elif self.is_cat:
            return "Meow!"
        else:
            return "sigh!"

    def display_info(self):
        if self.is_dog:
            print(f"Name: {self.name}, Species: Dog, Breed: {self.breed_or_color}")
        elif self.is_cat:
            print(f"Name: {self.name}, Species: Cat, Color: {self.breed_or_color}")
        else:
            print(f"Name: {self.name}, Species: Tortoise, Color: {self.breed_or_color}")

# Example usage:
dog = BADAnimal("Buddy", True, False ,"Golden Retriever")
cat = BADAnimal("Whiskers", False, True, "Black")
tortoise = BADAnimal("Tortoise", False, False, "Brown")

# Display information and speak
dog.display_info() # Output: Name: Buddy, Species: Dog, Breed: Golden Retriever
print(dog.speak()) # Output: Woof!
print("---")
cat.display_info() # Output: Name: Whiskers, Species: Cat, Color: Black
print(cat.speak()) # Output: Meow!
print("---")
tortoise.display_info() # Output: Name: Tortoise, Species: Tortoise, Color: Brown
print(tortoise.speak()) # Output: Sigh!