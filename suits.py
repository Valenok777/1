Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> suits = ["бубен", "червей", "крестей", "пик"]
>>> values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
>>> for value in values:
	for suit in suits:
		print(value, suit)

		
2 бубен
2 червей
2 крестей
2 пик
3 бубен
3 червей
3 крестей
3 пик
4 бубен
4 червей
4 крестей
4 пик
5 бубен
5 червей
5 крестей
5 пик
6 бубен
6 червей
6 крестей
6 пик
7 бубен
7 червей
7 крестей
7 пик
8 бубен
8 червей
8 крестей
8 пик
9 бубен
9 червей
9 крестей
9 пик
10 бубен
10 червей
10 крестей
10 пик
11 бубен
11 червей
11 крестей
11 пик
12 бубен
12 червей
12 крестей
12 пик
13 бубен
13 червей
13 крестей
13 пик
>>>  for value in values:
	for suit in suits:
		
SyntaxError: unexpected indent
>>> print(values)
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
>>> 
>>> 
>>> 
>>> mydick = {"name"  : "Василий", "age" : 60, "occupation" : "президент"}
>>> mydick.get("name")
'Василий'
>>> 
>>> 
>>> syudents = {"name :
