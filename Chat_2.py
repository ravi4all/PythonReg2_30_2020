print("Welcome",name := input("Enter your name : "))

helloIntent = ["hi","hello","hey","hi there","hello there"]

while (msg := input("Enter your message : ")) != "bye":
    if msg in helloIntent:
        print("Hello",name)
    else:
        print("I am unable to answer it...")

print("Bye",name)

