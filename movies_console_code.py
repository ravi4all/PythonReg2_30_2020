Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonReg_2-30\movie_recommendation_part-1.py 
{'action': 38.46, 'comedy': 30.0, 'thriller': 7.69, 'biopic': 10.0, 'horror': 0.0}
>>> simScore
{'action': 38.46, 'comedy': 30.0, 'thriller': 7.69, 'biopic': 10.0, 'horror': 0.0}
>>> simScore.items()
dict_items([('action', 38.46), ('comedy', 30.0), ('thriller', 7.69), ('biopic', 10.0), ('horror', 0.0)])
>>> simScore.keys()
dict_keys(['action', 'comedy', 'thriller', 'biopic', 'horror'])
>>> simScore.values()
dict_values([38.46, 30.0, 7.69, 10.0, 0.0])
>>> for item in simScore:
	print(item)

	
action
comedy
thriller
biopic
horror
>>> for item in simScore:
	print(simScore[item])

	
38.46
30.0
7.69
10.0
0.0
>>> for item in simScore:
	print(item,simScore[item])

	
action 38.46
comedy 30.0
thriller 7.69
biopic 10.0
horror 0.0
>>> max(simScore)
'thriller'
>>> max(simScore.items())
('thriller', 7.69)
>>> def show(x):
	return x[1]

>>> max(simScore.items(), key = show)
('action', 38.46)
>>> cat = max(simScore.items(), key = show)
>>> cat[0]
'action'
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonReg_2-30\movie_recommendation_part-1.py 
{'action': 38.46, 'comedy': 30.0, 'thriller': 7.69, 'biopic': 10.0, 'horror': 0.0}
Traceback (most recent call last):
  File "C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonReg_2-30\movie_recommendation_part-1.py", line 24, in <module>
    cat = max(simScore.items(), key = show)
NameError: name 'show' is not defined
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonReg_2-30\movie_recommendation_part-1.py 
{'action': 38.46, 'comedy': 30.0, 'thriller': 7.69, 'biopic': 10.0, 'horror': 0.0}
Traceback (most recent call last):
  File "C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonReg_2-30\movie_recommendation_part-1.py", line 28, in <module>
    recommended = movies[cat] - user
KeyError: ('action', 38.46)
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonReg_2-30\movie_recommendation_part-1.py 
{'action': 38.46, 'comedy': 30.0, 'thriller': 7.69, 'biopic': 10.0, 'horror': 0.0}
Traceback (most recent call last):
  File "C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonReg_2-30\movie_recommendation_part-1.py", line 28, in <module>
    recommended = movies[cat[0]] - user
TypeError: unsupported operand type(s) for -: 'list' and 'set'
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonReg_2-30\movie_recommendation_part-1.py 
{'action': 38.46, 'comedy': 30.0, 'thriller': 7.69, 'biopic': 10.0, 'horror': 0.0}
Recommended Movies are {'baahubali', 'spiderman', 'batman', 'kaala', 'ironman', 'junglee'}
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonReg_2-30\movie_recommendation_part-1.py 
{'action': 28.57, 'comedy': 44.44, 'thriller': 7.69, 'biopic': 10.0, 'horror': 0.0}
Recommended Movies are {'housefull', 'dhamaal'}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonReg_2-30/movie_recommendation_part-2.py 
{'action': 23.08, 'comedy': 37.5, 'thriller': 9.09, 'biopic': 12.5, 'horror': 0.0}
>>> cat
('comedy', 37.5)
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonReg_2-30/movie_recommendation_part-2.py 
{'action': 23.08, 'comedy': 37.5, 'thriller': 9.09, 'biopic': 12.5, 'horror': 0.0}
>>> simMovies.intersection(movies[cat])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    simMovies.intersection(movies[cat])
KeyError: ('comedy', 37.5)
>>> simMovies.intersection(movies[cat[0]])
{'avengers', 'bala', 'sanju'}
>>> user_2.intersection(movies[cat[0]])
{'housefull', 'avengers', 'bala', 'sanju'}
>>> user_1.intersection(movies[cat[0]])
{'avengers', 'bala', 'sanju', 'golmaal'}
>>> user_2.intersection(movies[cat[0]]) - user_1.intersection(movies[cat[0]])
{'housefull'}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonReg_2-30/movie_recommendation_part-2.py 
{'action': 23.08, 'comedy': 37.5, 'thriller': 9.09, 'biopic': 12.5, 'horror': 0.0}
Recommended movie for user_1 {'housefull'}
Recommended movie for user_2 {'golmaal'}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonReg_2-30/movie_recommendation_part-2.py 
{'action': 15.38, 'comedy': 42.86, 'thriller': 0.0, 'biopic': 14.29, 'horror': 0.0}
Recommended movie for user_1 set()
Recommended movie for user_2 {'golmaal'}
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonReg_2-30/movie_recommendation_part-2.py 
{'action': 18.18, 'comedy': 14.29, 'thriller': 0.0, 'biopic': 0.0, 'horror': 0.0}
Recommended movie for user_1 {'junglee'}
Recommended movie for user_2 {'batman', 'kee', 'KGF'}
>>> 
