import sys
sys.path.append("../")

from controller import controller

def addEmp():
    name = input("Enter Emp Name : ")
    emailId = input("Enter Email Id : ")
    pwd = input("Enter Password : ")
    dept = input("Enter Department : ")
    empObj = controller.addEmpController(name,emailId,pwd,dept)
    print(empObj)

def searchEmp():
    pass

def delEmp():
    pass

def updateEmp():
    pass

def main():
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