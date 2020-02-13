Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> names = ["tom","smith","john","harry","will"]
>>> for name in names:
	print(name)

	
tom
smith
john
harry
will
>>> for i in range(len(names)):
	print(names[i])

	
tom
smith
john
harry
will
>>> for i, name in enumerate(names):
	print(i,name)

	
0 tom
1 smith
2 john
3 harry
4 will
>>> data = [names,["delhi","pune","mumbai","chennai","noida"],["hr","it","it","sales","hr"]]
>>> data
[['tom', 'smith', 'john', 'harry', 'will'], ['delhi', 'pune', 'mumbai', 'chennai', 'noida'], ['hr', 'it', 'it', 'sales', 'hr']]
>>> for i,items in enumerate(data):
	print(i,items)

	
0 ['tom', 'smith', 'john', 'harry', 'will']
1 ['delhi', 'pune', 'mumbai', 'chennai', 'noida']
2 ['hr', 'it', 'it', 'sales', 'hr']
>>> for i,items in enumerate(data):
	print(items[i])

	
tom
pune
it
>>> for i,items in enumerate(data):
	print(data[i])

	
['tom', 'smith', 'john', 'harry', 'will']
['delhi', 'pune', 'mumbai', 'chennai', 'noida']
['hr', 'it', 'it', 'sales', 'hr']
>>> for i,names,city,dept in enumerate(data):
	print(names)

	
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    for i,names,city,dept in enumerate(data):
ValueError: not enough values to unpack (expected 4, got 2)
>>> data = {"name":"Tom","city":"pune","dept":"IT"}
>>> for i,item in enumerate(data):
	print(i,item)

	
0 name
1 city
2 dept
>>> for i,item in enumerate(data):
	print(i,data[item])

	
0 Tom
1 pune
2 IT
>>> for i,item in enumerate(data):
	print(i,item,data[item])

	
0 name Tom
1 city pune
2 dept IT
>>> for i,item in enumerate(data,start=1):
	print(i,item,data[item])

	
1 name Tom
2 city pune
3 dept IT
>>> names
['tom', 'smith', 'john', 'harry', 'will']
>>> city = ["pune","delhi","mumbai","chennai"]
>>> dept = ["IT","HR","IT","HR","SALES"]
>>> for i in range(len(names)):
	print(names[i],city[i])

	
tom pune
smith delhi
john mumbai
harry chennai
Traceback (most recent call last):
  File "<pyshell#37>", line 2, in <module>
    print(names[i],city[i])
IndexError: list index out of range
>>> zip(names,city)
<zip object at 0x0000020A1EAB72C8>
>>> list(zip(names,city))
[('tom', 'pune'), ('smith', 'delhi'), ('john', 'mumbai'), ('harry', 'chennai')]
>>> for name,c in zip(names,city):
	print(name,c)

	
tom pune
smith delhi
john mumbai
harry chennai
>>> import itertools
>>> list(itertools.zip_longest(names,city))
[('tom', 'pune'), ('smith', 'delhi'), ('john', 'mumbai'), ('harry', 'chennai'), ('will', None)]
>>> for name,c in itertools.zip_longest(names,city):
	print(name,c)

	
tom pune
smith delhi
john mumbai
harry chennai
will None
>>> for name,c,d in itertools.zip_longest(names,city,dept):
	print(name,c,d)

	
tom pune IT
smith delhi HR
john mumbai IT
harry chennai HR
will None SALES
>>> for i,name,c,d in enumerate(itertools.zip_longest(names,city,dept)):
	print(i,name,c,d)

	
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    for i,name,c,d in enumerate(itertools.zip_longest(names,city,dept)):
ValueError: not enough values to unpack (expected 4, got 2)
>>> index = [1,2,3,4,5]
>>> for i,name,c,d in itertools.zip_longest(index,names,city,dept):
	print(i,name,c,d)

	
1 tom pune IT
2 smith delhi HR
3 john mumbai IT
4 harry chennai HR
5 will None SALES
>>> 9/5 * 34.5 + 32
94.1
>>> 9/5 * [34.5,36.1,29.8] + 32
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    9/5 * [34.5,36.1,29.8] + 32
TypeError: can't multiply sequence by non-int of type 'float'
>>> lambda
SyntaxError: invalid syntax
>>> lambda x,y : x + y
<function <lambda> at 0x0000020A1EADAD90>
>>> func = lambda x,y : x + y
>>> func(12,33)
45
>>> def myMap(func):
	return func(4,5)

>>> def myMap(func,x,y):
	return func(x,y)

>>> myMap(lambda x,y : x + y)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    myMap(lambda x,y : x + y)
TypeError: myMap() missing 2 required positional arguments: 'x' and 'y'
>>> myMap(lambda x,y : x + y,10,12)
22
>>> func = lambda x,y : x + y, x - y
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    func = lambda x,y : x + y, x - y
NameError: name 'x' is not defined
>>> func = lambda x,y : (x + y, x - y)
>>> func(3,4)
(7, -1)
>>> num = 9
>>> num > 5
True
>>> num % 2 == 0
False
>>> def counter():
	x = 0
	while True:
		return x + 1

	
>>> counter()
1
>>> counter()
1
>>> def counter():
	x = 0
	while True:
		return x + 1
		print("hello")

		
>>> counter()
1
>>> def counter():
	x = 0
	while True:
		yield x + 1
		print("hello")

		
>>> counter()
<generator object counter at 0x0000020A1EA63CF0>
>>> num = counter()
>>> num
<generator object counter at 0x0000020A1EAC8A98>
>>> next(num)
1
>>> next(num)
hello
1
>>> next(num)
hello
1
>>> def counter():
	x = 0
	while True:
		yield x += 1
		
SyntaxError: invalid syntax
>>> 
>>> def counter():
	x = 0
	while True:
		yield x + 1

		
>>> num = counter()
>>> 
>>> next(num)
1
>>> next(num)
1
>>> def counter():
	x = 0
	while True:
		x = x + 1
		yield x

		
>>> num = counter()
>>> next(num)
1
>>> next(num)
2
>>> next(num)
3
>>> next(num)
4
>>> next(num)
5
>>> x = [i for i in range(1,10)]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x = (i for i in range(1,10))
>>> x
<generator object <genexpr> at 0x0000020A1EA63CF0>
>>> next(x)
1
>>> next(x)
2
>>> next(x)
3
>>> 
