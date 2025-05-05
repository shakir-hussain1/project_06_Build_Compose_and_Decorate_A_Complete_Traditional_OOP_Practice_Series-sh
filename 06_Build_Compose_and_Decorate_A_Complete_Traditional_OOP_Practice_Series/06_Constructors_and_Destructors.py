class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")

# Example usage
logger1 = Logger()

# Forcing deletion to see destructor message (optional)
del logger1
