# global scope
x = 5
y = 5
# Function Definition
def add():
    # Local scope
    x = 12
    y = 20
    z = x + y
    print("Sum is",z)

def sub():
    z = x - y
    print("Sub is",z)

# Function Calling
add()
z = x * y
print(z)
