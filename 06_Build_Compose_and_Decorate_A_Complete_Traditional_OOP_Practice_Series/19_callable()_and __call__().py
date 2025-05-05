class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        """Make the object callable, returning the value multiplied by the factor."""
        return value * self.factor


# Example usage
if __name__ == "__main__":
    times3 = Multiplier(3)

    # Check if the object is callable
    print("Is times3 callable?", callable(times3))  # True

    # Call the object like a function
    result = times3(10)  # Should return 30
    print("times3(10) =", result)
