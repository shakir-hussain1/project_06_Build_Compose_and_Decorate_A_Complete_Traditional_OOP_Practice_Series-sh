class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called for: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject
        print(f"Teacher constructor called for subject: {self.subject}")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
teacher1 = Teacher("Tauqeer", "Mathematics")
teacher1.display()
