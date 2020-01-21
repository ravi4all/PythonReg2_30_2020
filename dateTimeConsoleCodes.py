>>> import time
>>> time.time
<built-in function time>
>>> time.time()
1579601734.2453094
>>> time.time()
1579601740.5149906
>>> time.time()
1579601742.0832515
>>> time.time()
1579601763.1320133
>>> time.ctime()
'Tue Jan 21 15:46:13 2020'
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2020, 1, 21, 15, 46, 44, 737849)
>>> datetime.datetime.now().time()
datetime.time(15, 46, 49, 474832)
>>> datetime.datetime.now().date()
datetime.date(2020, 1, 21)
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2020, 1, 21, 15, 47, 51, 442578)
>>> t = datetime.now().time()
>>> print(t)
15:48:11.263550
>>> d = datetime.now().date()
>>> print(d)
2020-01-21
>>> d.strftime("%d/%m/%y,%a")
'21/01/20,Tue'
>>> t.strftime("%H:%M:%S,%p")
'15:48:11,PM'
>>> d.strftime("%d/%m/%y,%A")
'21/01/20,Tuesday'
>>> t.strftime("%H:%M:%S,%P")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t.strftime("%H:%M:%S,%P")
ValueError: Invalid format string
>>> t.strftime("%d:%m:%y,%p")
'01:01:00,PM'
>>> d.strftime("%H/%M/%S,%A")
'00/00/00,Tuesday'
>>> 
