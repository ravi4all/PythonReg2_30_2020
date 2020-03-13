class Emp:

    def __init__(self):
        self.id = 101      # public
        self._name = 'Ram' # protected

    @property
    def salary(self):
        print("Getter Called")
        return self.__salary

    @salary.setter
    def salary(self,value):
        print("Setter Called, Salary set")
        self.__salary = value

    def showEmp(self):
        print("Emp details : ")
        print(self.id,self._name,self.__salary)

obj = Emp()
obj.salary = 35000
obj.showEmp()
print(obj.salary)