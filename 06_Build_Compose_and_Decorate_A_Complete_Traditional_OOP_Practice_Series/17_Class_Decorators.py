# Class decorator definition
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Shakir Hussain")
print(p.greet())
