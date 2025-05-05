# Decorator definition
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Apply decorator to say_hello
@log_function_call
def say_hello():
    print("Hello!")

# Example usage
say_hello()
