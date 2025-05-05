class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof woof!")

# Example usage
dog1 = Dog("Tommy", "Golden Retriever")
dog1.bark()
