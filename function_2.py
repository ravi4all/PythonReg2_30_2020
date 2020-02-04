# Making of global variables
def emp():
    global name
    name = "Ram"
    sal = 34000
    global dept
    dept = "IT"
    print("Details of {} are : ".format(name))
    print("Salary is",sal)

emp()
print("Dept is",dept)