class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn        # Private variable

# Create an Employee object
emp = Employee("Shakir Hussain", 75000, "123-45-6789")

# Access public variable
print("Name:", emp.name)

# Access protected variable
print("Salary (protected):", emp._salary)

# Try to access private variable directly
try:
    print("SSN (private):", emp.__ssn)
except AttributeError as e:
    print("Cannot access __ssn directly:", e)

# Access private variable using name mangling
print("SSN (accessed via name mangling):", emp._Employee__ssn)
