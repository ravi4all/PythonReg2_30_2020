Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello everyone, this is python programming"
>>> text[0]
'h'
>>> text[0:4]
'hell'
>>> text[0:5]
'hello'
>>> text[5:14]
' everyone'
>>> text[:]
'hello everyone, this is python programming'
>>> text[0:]
'hello everyone, this is python programming'
>>> text[:10]
'hello ever'
>>> text[0:20:2]
'hloeeyn,ti'
>>> text[0:20:1]
'hello everyone, this'
>>> text[0:20:2]
'hloeeyn,ti'
>>> text[10:0]
''
>>> text[-1]
'g'
>>> text[-2]
'n'
>>> text[10:0:-1]
'yreve olle'
>>> text[10]
'y'
>>> text[10::-1]
'yreve olleh'
>>> text[::-1]
'gnimmargorp nohtyp si siht ,enoyreve olleh'
>>> text
'hello everyone, this is python programming'
>>> text[-10:-1]
'rogrammin'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[0,10]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    text[0,10]
TypeError: string indices must be integers
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.capitalize()
'Hello everyone, this is python programming'
>>> text.upper()
'HELLO EVERYONE, THIS IS PYTHON PROGRAMMING'
>>> title.lower()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    title.lower()
NameError: name 'title' is not defined
>>> text.lower()
'hello everyone, this is python programming'
>>> text.title()
'Hello Everyone, This Is Python Programming'
>>> text.swapcase()
'HELLO EVERYONE, THIS IS PYTHON PROGRAMMING'
>>> text.replace('i','z')
'hello everyone, thzs zs python programmzng'
>>> text
'hello everyone, this is python programming'
>>> text.index('i')
18
>>> text.count('i')
3
>>> text.index('i',19)
21
>>> text.index('i',22)
39
>>> text.index('i',12,20)
18
>>> text.index('i',12,15)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    text.index('i',12,15)
ValueError: substring not found
>>> text.find('i')
18
>>> text.find('i',12,20)
18
>>> text.find('i',12,16)
-1
>>> text.isnumeric()
False
>>> text.isprintable()
True
>>> text.lower()
'hello everyone, this is python programming'
>>> text.islower()
True
>>> text.isalpha()
False
>>> len(text)
42
>>> text.center(12)
'hello everyone, this is python programming'
>>> text.center(40)
'hello everyone, this is python programming'
>>> text.center(42)
'hello everyone, this is python programming'
>>> text.center(43)
' hello everyone, this is python programming'
>>> text.center(44)
' hello everyone, this is python programming '
>>> text.center(50)
'    hello everyone, this is python programming    '
>>> text.center(50,'*')
'****hello everyone, this is python programming****'
>>> text.zfill(10)
'hello everyone, this is python programming'
>>> text.zfill(50)
'00000000hello everyone, this is python programming'
>>> text.encode()
b'hello everyone, this is python programming'
>>> hex(10)
'0xa'
>>> hex(100)
'0x64'
>>> hex(10000)
'0x2710'
>>> oct(25)
'0o31'
>>> ord('h')
104
>>> ord('hello')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    ord('hello')
TypeError: ord() expected a character, but string of length 5 found
>>> chr(66)
'B'
>>> bin(12)
'0b1100'
>>> bin(104)
'0b1101000'
>>> bin(ord('h'))
'0b1101000'
>>> 
