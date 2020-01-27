Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = []
>>> data = list()
>>> data = [4,6,8,7,2,3,6,8]
>>> data[0]
4
>>> data[-1]
8
>>> data[0:4]
[4, 6, 8, 7]
>>> data[4:8]
[2, 3, 6, 8]
>>> data.append(100)
>>> data
[4, 6, 8, 7, 2, 3, 6, 8, 100]
>>> data.append(3)
>>> data
[4, 6, 8, 7, 2, 3, 6, 8, 100, 3]
>>> data.append(3,4,7,98,3,2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    data.append(3,4,7,98,3,2)
TypeError: append() takes exactly one argument (6 given)
>>> data.append([5,7,3,3,61])
>>> data
[4, 6, 8, 7, 2, 3, 6, 8, 100, 3, [5, 7, 3, 3, 61]]
>>> data.pop()
[5, 7, 3, 3, 61]
>>> x = [5,7,3,3,61]
>>> data
[4, 6, 8, 7, 2, 3, 6, 8, 100, 3]
>>> for i in range(len(x)):
	data.append(x[i])

	
>>> data
[4, 6, 8, 7, 2, 3, 6, 8, 100, 3, 5, 7, 3, 3, 61]
>>> data.extend(10)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    data.extend(10)
TypeError: 'int' object is not iterable
>>> data.extend(10,45)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    data.extend(10,45)
TypeError: extend() takes exactly one argument (2 given)
>>> data
[4, 6, 8, 7, 2, 3, 6, 8, 100, 3, 5, 7, 3, 3, 61]
>>> data.insert(5,10)
>>> data
[4, 6, 8, 7, 2, 10, 3, 6, 8, 100, 3, 5, 7, 3, 3, 61]
>>> data.pop(6)
3
>>> data
[4, 6, 8, 7, 2, 10, 6, 8, 100, 3, 5, 7, 3, 3, 61]
>>> data.index(100)
8
>>> data.pop(8)
100
>>> data
[4, 6, 8, 7, 2, 10, 6, 8, 3, 5, 7, 3, 3, 61]
>>> data.insert(8,100)
>>> data
[4, 6, 8, 7, 2, 10, 6, 8, 100, 3, 5, 7, 3, 3, 61]
>>> data.remove(100)
>>> data
[4, 6, 8, 7, 2, 10, 6, 8, 3, 5, 7, 3, 3, 61]
>>> data.sort()
>>> data
[2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 10, 61]
>>> data.sort(reverse=True)
>>> data
[61, 10, 8, 8, 7, 7, 6, 6, 5, 4, 3, 3, 3, 2]
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 3 ** 10
59049
>>> cubes = []
>>> for i in range(1,11):
	cubes.append(i ** 3)

	
>>> cubes
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> cubes = [i**3 for i in range(1,11)]
>>> cubes
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> even = [i for i in range(1,11) if i % 2 == 0]
>>> even
[2, 4, 6, 8, 10]
>>> import math
>>> math.sqrt(8)
2.8284271247461903
>>> math.sqrt(64)
8.0
>>> 8 ** 2
64
>>> 64 ** 1/2
32.0
>>> 64 ** 1/3
21.333333333333332
>>> 64 ** 1/4
16.0
>>> 64 ** (1/2)
8.0
>>> 64 ** (1/3)
3.9999999999999996
>>> math.pow(64,1/3)
3.9999999999999996
>>> math.pow(64,1/2)
8.0
>>> data
[61, 10, 8, 8, 7, 7, 6, 6, 5, 4, 3, 3, 3, 2]
>>> data[0]
61
>>> data[0] = 16
>>> data
[16, 10, 8, 8, 7, 7, 6, 6, 5, 4, 3, 3, 3, 2]
>>> del data[3]
>>> data
[16, 10, 8, 7, 7, 6, 6, 5, 4, 3, 3, 3, 2]
>>> 
