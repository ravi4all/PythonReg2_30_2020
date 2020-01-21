'''
name = input("Enter your name : ")
print("Hello",name)
'''

# walrus operator
print("Hello",name := input("Enter your name : "))

msg = input("Enter your message : ")
if msg == "hello":
    print("Hello",name)
elif msg == "bye":
    print("Bye",name)
else:
    print("I am unable to answer it...")
