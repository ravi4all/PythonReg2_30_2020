Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {}
>>> type(data)
<class 'dict'>
>>> data = {'name':'Tom','age':34,'sal':45000,'dept':'IT'}
>>> data
{'name': 'Tom', 'age': 34, 'sal': 45000, 'dept': 'IT'}
>>> data.keys()
dict_keys(['name', 'age', 'sal', 'dept'])
>>> data.values()
dict_values(['Tom', 34, 45000, 'IT'])
>>> data['name']
'Tom'
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data[0]
KeyError: 0
>>> data[0:2]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data[0:2]
TypeError: unhashable type: 'slice'
>>> data['address'] = 'Delhi'
>>> data
{'name': 'Tom', 'age': 34, 'sal': 45000, 'dept': 'IT', 'address': 'Delhi'}
>>> data['name'] = 'Jerry'
>>> data
{'name': 'Jerry', 'age': 34, 'sal': 45000, 'dept': 'IT', 'address': 'Delhi'}
>>> data = {"names":['x','y','z'],"age":[4,5,7],"sal":[2,7,9]}
>>> data['names']
['x', 'y', 'z']
>>> data['names'][0]
'x'
>>> data = {"name":"Sachin","matches":{"odi":[200],"test":[248],"t20":[100],"ipl":[100]}}
>>> data
{'name': 'Sachin', 'matches': {'odi': [200], 'test': [248], 't20': [100], 'ipl': [100]}}
>>> data.keys()
dict_keys(['name', 'matches'])
>>> data['matches']
{'odi': [200], 'test': [248], 't20': [100], 'ipl': [100]}
>>> matches = data['matches']
>>> matches
{'odi': [200], 'test': [248], 't20': [100], 'ipl': [100]}
>>> matches['test']
[248]
>>> data = {"name":"Sachin","matches":{"odi":{"100":51,"50":95},"test":{"100":49,"50":90},"t20":{"100":0,"50":10}}}
>>> data
{'name': 'Sachin', 'matches': {'odi': {'100': 51, '50': 95}, 'test': {'100': 49, '50': 90}, 't20': {'100': 0, '50': 10}}}
>>> data['matches']
{'odi': {'100': 51, '50': 95}, 'test': {'100': 49, '50': 90}, 't20': {'100': 0, '50': 10}}
>>> data['matches']['t20']
{'100': 0, '50': 10}
>>> data['matches']['t20']['50']
10
>>> data = [{"name":"Sachin","matches":{"odi":{"100":51,"50":95},"test":{"100":49,"50":90},"t20":{"100":0,"50":10}}},{"name":"Kohli","matches":{"odi":{"100":51,"50":95},"test":{"100":49,"50":90},"t20":{"100":0,"50":10}}},{"name":"Yuvraj","matches":{"odi":{"100":51,"50":95},"test":{"100":49,"50":90},"t20":{"100":0,"50":10}}}]
>>> data[0]
{'name': 'Sachin', 'matches': {'odi': {'100': 51, '50': 95}, 'test': {'100': 49, '50': 90}, 't20': {'100': 0, '50': 10}}}
>>> data[1]
{'name': 'Kohli', 'matches': {'odi': {'100': 51, '50': 95}, 'test': {'100': 49, '50': 90}, 't20': {'100': 0, '50': 10}}}
>>> data[1]['matches']['t20']['50']
10
>>> 
