import random
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
    return obj