Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> b = 22
>>> c = a + b
>>> print(c)
34
>>> print("Sum is",c)
Sum is 34
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_1.py ==============
34
>>> a = 101
>>> type(a)
<class 'int'>
>>> a = "hello"
>>> type(a)
<class 'str'>
>>> a = 10.5
>>> type(a)
<class 'float'>
>>> msg =
SyntaxError: invalid syntax
>>> msg = "hello eveyone..."
>>> msg.encode()
b'hello eveyone...'
>>> msg = "हेलो सब कैसे हो ?"
>>> msg.encode()
b'\xe0\xa4\xb9\xe0\xa5\x87\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\xb8\xe0\xa4\xac \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x8b ?'
>>> enc = msg.encode()
>>> enc.decode()
'हेलो सब कैसे हो ?'
>>> names = "ram","shyam","sumit","namit","gaurav"
>>> names
('ram', 'shyam', 'sumit', 'namit', 'gaurav')
>>> type(names)
<class 'tuple'>
>>> names[2]
'sumit'
>>> a = 12
>>> b = 21
>>> c = a + b
>>> print("Sum is",c)
Sum is 33
>>> print("Sum of a and b is c")
Sum of a and b is c
>>> print("Sum of", a ,"and", b, "is", c)
Sum of 12 and 21 is 33
>>> name = "Ram"
>>> sal = 34000
>>> msg = "Hello " + name
>>> msg
'Hello Ram'
>>> msg = "Hello " + name + " your salary is " + sal
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    msg = "Hello " + name + " your salary is " + sal
TypeError: can only concatenate str (not "int") to str
>>> 12 + "12"
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    12 + "12"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> msg = "Hello {}, Your salary is {}".format(name,sal)
>>> msg
'Hello Ram, Your salary is 34000'
>>> print("Sum of {} and {} is {}".format(a,b,c))
Sum of 12 and 21 is 33
>>> print(f"Sum of {a} and {b} is {c}")
Sum of 12 and 21 is 33
>>> msg = f"Hello {name}, Your salary is {sal}"
>>> msg
'Hello Ram, Your salary is 34000'
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_2.py ==============
Enter your name : Ravi
Hello Ravi
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_2.py ==============
Enter your name : Ram
Hello Ram
Enter first number : 12
Enter second number : 44
Sum is 1244
>>> num_1
'12'
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_2.py ==============
Enter your name : Ravi
Hello Ravi
Enter first number : 22
Enter second number : 55
Sum is 77
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
	print(i)

	
0
1
2
3
>>> for i in range(4):
	t.forward(200)
	t.left(90)

	
>>> t.reset()
>>> for i in range(40):
	t.forward(4*i)
	t.left(90)

	
>>> t.reset()
>>> for i in range(40):
	t.forward(4*i)
	t.left(45)

	
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_3.py ==============
0
1
2
3
4
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_3.py ==============
0
1
2
3
4
=============
1
2
3
4
5
6
7
8
9
10
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_3.py ==============
0
1
2
3
4
=============
1
2
3
4
5
6
7
8
9
10
=============
2
4
6
8
10
12
14
16
18
20
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_3.py ==============
0
1
2
3
4
=============
1
2
3
4
5
6
7
8
9
10
=============
2
5
8
11
14
17
20
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_3.py ==============
0
1
2
3
4
=============
1
2
3
4
5
6
7
8
9
10
=============
2
4
6
8
10
12
14
16
18
20
==============
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_3.py ==============
0
1
2
3
4
=============
1
2
3
4
5
6
7
8
9
10
=============
2
4
6
8
10
12
14
16
18
20
==============
10
9
8
7
6
5
4
3
2
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_4.py ==============
Even Number 0
Even Number 2
Even Number 4
Even Number 6
Even Number 8
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_4.py ==============
>>> num
43
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_4.py ==============
Enter the number : 45
Too Low...
>>> 
============== RESTART: C:/Users/asus/Desktop/Code_1/code_4.py ==============
Enter the number : 50
Too high...
Enter the number : 40
Too high...
Enter the number : 30
Too Low...
Enter the number : 33
Too Low...
Enter the number : 35
Congrats, You guessed the number...
>>> 
