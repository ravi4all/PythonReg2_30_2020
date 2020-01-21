print("Welcome",name := input("Enter your name : "))

while (msg := input("Enter your message : ")) != "bye":
    if msg == "hello" or msg == "hi" or msg == "hey" or msg == "hello there":
        print("Hello",name)
    else:
        print("I am unable to answer it...")

print("Bye",name)
