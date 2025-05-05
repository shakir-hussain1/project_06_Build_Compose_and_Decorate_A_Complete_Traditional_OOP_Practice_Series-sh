class Counter:
    count = 0  # Class variable to keep track of number of instances

    def __init__(self):
        Counter.count += 1  # Increment count each time an object is created

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()
