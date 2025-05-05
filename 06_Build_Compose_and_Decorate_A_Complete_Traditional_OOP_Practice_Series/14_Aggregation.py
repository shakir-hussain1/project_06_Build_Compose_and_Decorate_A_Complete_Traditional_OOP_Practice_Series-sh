class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: storing reference to an existing Employee

    def show_department_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  # Access Employee's method

# Create an Employee object independently
emp1 = Employee("Shakir Hussain", 101)

# Pass the existing Employee object to Department
dept1 = Department("Human Resources", emp1)

# Display Department and Employee details
dept1.show_department_details()
