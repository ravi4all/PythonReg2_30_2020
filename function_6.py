def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Sub is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")
ch = input("Enter your choice: ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter first number : "))

# if ch == "1":
#     add(num_1,num_2)
# elif ch == "2":
#     sub(num_1,num_2)
# elif ch == "3":
#     div(num_1,num_2)
# elif ch == "4":
#     mul(num_1,num_2)
# else:
#     print("Invalid choice...")

# operations = [add,sub,div,mul]
# func = operations[int(ch)-1]
# func(num_1,num_2)

# operations[int(ch) - 1](num_1,num_2)

operations = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}
operations[ch](num_1,num_2)