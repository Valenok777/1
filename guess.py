import random

number = random.randint(1,3)

guess = int(input("Угадай число от 1 до 3 "))
if number == guess:
	print("Угадал")
else :
	print("Не угадал")
input("")
