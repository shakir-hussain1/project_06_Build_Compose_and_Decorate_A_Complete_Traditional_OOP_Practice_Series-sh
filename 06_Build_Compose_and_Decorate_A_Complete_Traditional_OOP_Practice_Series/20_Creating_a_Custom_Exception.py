12# Define custom exception
class InvalidAgeError(Exception):
    """Exception raised when age is less than 18."""
    def __init__(self, age, message="Age must be at least 18."):
        self.age = age
        self.message = message
        super().__init__(f"{self.message} Given age: {self.age}")

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    print("Age is valid.")

# Example usage
if __name__ == "__main__":
    try:
        age_input = int(input("Enter your age: "))
        check_age(age_input)
    except InvalidAgeError as e:
        print("InvalidAgeError caught:", e)
    except ValueError:
        print("Please enter a valid integer for age.")
