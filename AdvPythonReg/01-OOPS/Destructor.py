class Emp:
    # constructor - object construct
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
        self.dept = 'IT'
        self.company = 'HCL'
        self.data = []

    def storeEmp(self):
        self.data.append([self.id,self.name,self.sal,self.dept,self.company])
        # print(self.data)

    def showEmp(self):
        return self.data

    # destructor - object destroy
    def __del__(self):
        print("Object {} deleted".format(self.name))

obj = Emp(101,'Ram',39000)
obj.dept = "HR"
obj.storeEmp()
print(obj.showEmp())

# del obj

obj_2 = Emp(102,'Shyam',45000)
obj_2.storeEmp()
print(obj_2.showEmp())