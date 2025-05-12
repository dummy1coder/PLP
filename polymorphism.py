# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclasses with different implementations
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling ")

# Using polymorphism
def show_movement(vehicles):
    for v in vehicles:
        v.move()

# Create objects
car = Car()
plane = Plane()
boat = Boat()
bike = Bicycle()

# Show movement
vehicles = [car, plane, boat, bike]
show_movement(vehicles)
