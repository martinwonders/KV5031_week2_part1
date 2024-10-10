class Car():
    def __init__(self, make, model, year, number_of_wheels, number_of_doors):
        self.make = make
        self.model = model
        self.year = year
        self.number_of_wheels = number_of_wheels
        self.number_of_doors = number_of_doors

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Number of wheels: {self.number_of_wheels}")
        print(f"Number of Doors: {self.number_of_doors}")

class Truck(Car):
    def __init__(self, make, model, year, number_of_wheels ,number_of_doors, payload_capacity):
        super().__init__(make, model, year, number_of_wheels, number_of_doors)
        self.payload_capacity = payload_capacity

    def display_info(self):
        super().display_info()
        print(f"Payload Capacity: {self.payload_capacity} tons")

car:Car = Car("Toyota", "Corolla", 2022, 4, 4)
a_truck:Truck = Truck("Ford", "F-150", 2023, 4, 3, 3.3 )
car.display_info()
print("----------------")
a_truck .display_info()

