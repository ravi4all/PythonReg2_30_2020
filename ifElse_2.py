print("Welcome",name := input("Enter your name : "))

'''
while True:
    msg = input("Enter your message : ")
    if msg == "hello":
        print("Hello",name)
    elif msg == "bye":
        print("Bye",name)
        break
    else:
        print("I am unable to answer it...")
'''

while (msg := input("Enter your message : ")) != "bye":
    if msg == "hello":
        print("Hello",name)
    else:
        print("I am unable to answer it...")

print("Bye",name)
