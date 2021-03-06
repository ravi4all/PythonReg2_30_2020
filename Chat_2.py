from datetime import datetime

'''
name = input("Enter your name : ")
print("Welcome",name)
'''

print("Welcome",name := input("Enter your name : "))

helloIntent = ["hi","hello","hey","hi there","hello there"]
dateIntent = ["please tell me date","today's date","what's the date today","date"]
timeIntent = ["please tell me time","current time","what's the time","time"]

while (msg := input("Enter your message : ")) != "bye":
    if msg in helloIntent:
        print("Hello",name)
    elif msg in dateIntent:
        cur_date = datetime.now().date()
        print(cur_date.strftime("%d/%m/%y,%a"))
    elif msg in timeIntent:
        cur_time = datetime.now().time()
        print(cur_time.strftime('%H:%M:%S,%p'))
    else:
        print("I am unable to answer it...")

print("Bye",name)

