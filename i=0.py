i = 0
while  i < 100:
    i += 1
    if i == 7:
        print("Игнорируем семерку")
        continue
    if i == 20:
        break
    print(i)
else:
    print("Цикл завершен успешно")
print("Цикл не завершен!")





#answer = input("Ваш ответ")
#while answer in (yes,no):