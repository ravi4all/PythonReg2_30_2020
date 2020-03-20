import sys
sys.path.append("../")

from model import model

def addEmpController(name,email,pwd,dept):
    empObj = model.addEmpModel(name,email,pwd,dept)
    return empObj

def searchEmp(email):
    data = model.searchEmployee(email)
    return data

def updateEmp(email,toUpdate,updatedValue):
    data = model.updateEmployee(email,toUpdate,updatedValue)
    return data