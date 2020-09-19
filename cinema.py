age = int(input("Сколько вам лет? "))
if age < 14:
    print("Вам меньше 14 лет, приходите через", 14 - age, "года")
else:
    money = int(input("Билет стоит 400 рублей, сколько у вас денег? "))
    if money < 400:
        print("У вас не хватает", 400 - money, "рублей")
    elif money == 400:
        print("Ваш билет ")
    else:
        print("Сдача", money - 400)




input("Для выхода нажмите ENTER")