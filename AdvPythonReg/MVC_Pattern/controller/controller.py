import sys
sys.path.append("../")

from model import model

def addEmpController(name,email,pwd,dept):
    empObj = model.addEmpModel(name,email,pwd,dept)
    return empObj