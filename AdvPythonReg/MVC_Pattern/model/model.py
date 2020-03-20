import random
from model import readWriteEmp

class Emp:

    def __init__(self,name,email,pwd,dept):
        self.id = random.randint(1,100)
        self.name = name
        self.email = email
        self.pwd = pwd
        self.dept = dept
        self.__sal = None

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self,value):
        self.__sal = value

    # to string - convert object to printable format
    def __str__(self):
        return self.email

employees = []
def addEmpModel(name,email,pwd,dept):
    obj = Emp(name,email,pwd,dept)
    obj.sal = random.randint(10000,30000)
    employees.append(obj)
    readWriteEmp.writeEmp(obj)
    return obj

# def searchEmployee(email):
#     for i in range(len(employees)):
#         if employees[i].email == email:
#             return employees[i]

def searchEmployee(email):
    data = readWriteEmp.readEmp()
    for i in range(len(data)):
        if data[i][2] == email:
            return data[i]

def updateEmployee(email,toUpdate,updatedValue):
    data = readWriteEmp.readEmp()
    for i in range(len(data)):
        if data[i][2] == email:
            if toUpdate == "name":
                data[i][1] = updatedValue
                break
            elif toUpdate == "email":
                data[i][2] = updatedValue
                break
            elif toUpdate == "password":
                data[i][3] =  updatedValue
                break
            elif toUpdate == "department":
                data[i][4] = updatedValue
                break
            elif toUpdate == "salary":
                data[i][5] = updatedValue
                break

    readWriteEmp.updateEmp(data)
    return data
