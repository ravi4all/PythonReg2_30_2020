Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> x = 10,
>>> x
(10,)
>>> x = 10,21,45,22,6,3
>>> x
(10, 21, 45, 22, 6, 3)
>>> x = (10,21,45,22,6,3)
>>> x
(10, 21, 45, 22, 6, 3)
>>> x[0]
10
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
