class Student:
    def __init__(self, name, marks):
        self.name = name       # Initialize name using self
        self.marks = marks     # Initialize marks using self

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Shakir", 90)
student1.display()
