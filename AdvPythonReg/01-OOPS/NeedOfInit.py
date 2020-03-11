class Emp:
    id = None
    name = None
    sal = None
    dept = 'IT'
    company = 'HCL'
    data = []

    def storeEmp(self):
        self.data.append([self.id,self.name,self.sal,self.dept,self.company])
        # print(self.data)

    def showEmp(self):
        return self.data

obj = Emp()
obj.id = 101
obj.name = 'Tom'
obj.sal = 35000
obj.dept = "HR"
obj.storeEmp()

obj_2 = Emp()
obj_2.id = 102
obj_2.name = 'Smith'
obj_2.sal = 39000
obj_2.storeEmp()

print(obj.showEmp())