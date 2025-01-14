"""
Implement a Vehicle base class with attributes like brand and year. Inherit
Car and Bike classes that add specific attributes (e.g., num_doors for Car and
gear_count for Bike).
"""

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

class Bike(Vehicle):
    def __init__(self, brand, year, gear_count):
        super().__init__(brand, year)
        self.gear_count = gear_count

# Example usage:
car = Car("Toyota", 2011, 4)
bike = Bike("Yamaha", 2019, 6)
print(car.brand, car.num_doors)
print(bike.brand, bike.gear_count)
