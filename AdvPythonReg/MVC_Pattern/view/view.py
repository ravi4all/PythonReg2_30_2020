import sys
sys.path.append("../")

from controller import controller

def addEmp():
    name = input("Enter Emp Name : ")
    emailId = input("Enter Email Id : ")
    pwd = input("Enter Password : ")
    dept = input("Enter Department : ")
    empObj = controller.addEmpController(name,emailId,pwd,dept)
    print(empObj,"Stored Successfully...")

def searchEmp():
    emp = input("Enter Employee Email : ")
    data = controller.searchEmp(emp)
    if not data:
        print("No records found")
    else:
        print(data)

def delEmp():
    pass

def updateEmp():
    emp = input("Enter Employee Email : ")
    data = controller.searchEmp(emp)
    if not data:
        print("No records found")
    else:
        print(data)
        toUpdate = input("What do you want to update : ")
        updatedValue = input("Enter Updated {} : ".format(toUpdate))
        data = controller.updateEmp(emp, toUpdate, updatedValue)


def main():
    while True:
        print("""
        1. Add Emp
        2. Search Emp
        3. Delete Emp
        4. Update Emp
        """)

        operations = {
            "1" : addEmp,
            "2" : searchEmp,
            "3" : delEmp,
            "4" : updateEmp
        }

        ch = input("Enter your choice : ")
        operations.get(ch)()

main()