employees = []

def login():
    email = input("Enter email : ")
    pwd = input("Enter password : ")
    for i in range(len(employees)):
        if employees[i]['email'] == email and employees[i]['pwd'] == pwd:
            print("Employee login success...")
            break
    else:
        print("Login Failed...")

def register():
    name = input("Enter name : ")
    emailId = input("Enter email : ")
    pwd = input("Enter password : ")
    dept = input("Enter dept : ")
    sal = input("Enter salary : ")
    user = {"name" : name, "email":emailId, "pwd":pwd, "dept":dept,
            "sal":sal}
    employees.append(user)
    print(user)

def main():
    while True:
        print("""
        1. Login
        2. Register
        """)

        ch = input("Enter your choice : ")
        operations = {"1" : login, "2" : register}
        operations.get(ch)()