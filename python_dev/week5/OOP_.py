class Superhero:
    def __init__(self, name, superpower, city):
        self.name = name
        self.superpower = superpower
        self.city = city

    def introduce(self):
        return f"I am {self.name}, the superhero of {self.city} with the power of {self.superpower}!"

    def save_the_day(self):
        return f"{self.name} is saving the day!"

# Example of creating a Superhero object
hero = Superhero("Captain Python", "code manipulation", "Code City")
print(hero.introduce())
print(hero.save_the_day())


class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def move(self):
        return "Running 🐕"

class Cat(Animal):
    def move(self):
        return "Jumping 🐈"

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Function to demonstrate polymorphism
def demonstrate_movement(movers):
    for mover in movers:
        print(mover.move())

# Create instances
dog = Dog()
cat = Cat()
car = Car()
plane = Plane()

# Demonstrate movement
movers = [dog, cat, car, plane]
demonstrate_movement(movers)
