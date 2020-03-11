class Emp:
    # Data Members
    id = None
    name = None
    sal = None
    dept = 'IT'
    company = 'HCL'

obj = Emp()
# print(Emp)
# print(Emp())
obj.id = 101
obj.name = 'Tom'
obj.sal = 35000
obj.dept = "HR"
print(obj.__dict__)


obj_2 = Emp()
obj_2.id = 102
obj_2.name = 'Smith'
obj_2.sal = 39000
print(obj_2.__dict__)

print(obj.company,obj_2.company)
