class Emp:

    def __init__(self):
        self.id = 101      # public
        self._name = 'Ram' # protected
        self.__sal = 34000 # private

    def showEmp(self):
        print("Emp details : ")
        print(self.id,self._name,self.__sal)

obj = Emp()
obj.__sal = 20000
obj.showEmp()
