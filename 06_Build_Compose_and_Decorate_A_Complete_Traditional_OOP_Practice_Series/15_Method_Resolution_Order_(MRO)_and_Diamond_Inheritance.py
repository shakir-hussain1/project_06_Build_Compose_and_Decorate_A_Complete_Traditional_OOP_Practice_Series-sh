class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")

class D(B, C):  # Multiple inheritance
    pass

# Create an object of D and call show()
d = D()
d.show()

# Print MRO to observe resolution order
print("\nMethod Resolution Order (MRO):")
for cls in D.__mro__:
    print(cls.__name__)
