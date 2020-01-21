# If Else
'''
for i in range(10):
    if i % 2 == 0:
        print("Even Number",i)
'''

# guess the number
import random

num = random.randint(1,100)

while True:
    user_num = int(input("Enter the number : "))
    # Comparison Operator -> ==, !=, >, <, >=, <=

    if user_num == num:
        print("Congrats, You guessed the number...")
        break
    elif user_num > num:
        print("Too high...")
    elif user_num < num:
        print("Too Low...")
    elif user_num < 1 or user_num > 100:
        print("Invalid number...")
        
