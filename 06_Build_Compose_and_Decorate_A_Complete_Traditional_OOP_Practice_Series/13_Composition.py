class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Access Engine's method through Car

# Example usage
engine1 = Engine()
my_car = Car(engine1)

my_car.start_car()
