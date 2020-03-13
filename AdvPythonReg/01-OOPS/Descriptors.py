# class Emp:
#
#     def __init__(self):
#         self.__name = ""
#
#     def __get__(self, instance, owner):
#         name = self.__name
#         print("Name is",name)
#         return name
#
#     def __set__(self, instance, value):
#         self.__name = value
#         print("Setter called for",self.__name)

class Emp:

    @property
    def name(self):
        print("Getter Called")
        return self.__name

    @name.setter
    def name(self,value):
        print("Setter Called")

obj = Emp()