class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"The {self.brand} car is starting.")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable and method from outside the class
print("Car Brand:", my_car.brand)
my_car.start()
