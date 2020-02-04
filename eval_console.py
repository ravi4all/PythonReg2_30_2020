Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sayHello(name):
	print("Hello",name)

	
>>> def sayBye(name):
	print("Bye",name)

	
>>> name = "Ram"
>>> greet = [sayHello(name),sayBye(name)]
Hello Ram
Bye Ram
>>> sayHello(name)
Hello Ram
>>> sayHello
<function sayHello at 0x000002210D69E598>
>>> greet = [sayHello,sayBye]
>>> greet
[<function sayHello at 0x000002210D69E598>, <function sayBye at 0x000002210B09C1E0>]
>>> greet[0]
<function sayHello at 0x000002210D69E598>
>>> greet[0](name)
Hello Ram
>>> sayHello
<function sayHello at 0x000002210D69E598>
>>> greet[0]
<function sayHello at 0x000002210D69E598>
>>> sayHello(name)
Hello Ram
>>> greet[0](name)
Hello Ram
>>> num_1 = "23"
>>> num_2 = 21
>>> num_2 = "21"
>>> num_1
'23'
>>> num_2
'21'
>>> num_1 + num_2
'2321'
>>> num_1 + "+" + num_2
'23+21'
>>> eval(num_1 + "+" + num_2)
44
>>> 
