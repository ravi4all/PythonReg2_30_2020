# by default python return input in string format
name = input("Enter your name : ")
print("Hello",name)

# so we need to type cast / convert the input() into int()
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
result = num_1 + num_2
print("Sum is",result)
