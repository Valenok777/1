money = int(input("Билет стоит 400 рублей, сколько у вас денег? "))
if money < 400:
    print("У вас не хватает средств")
else:
    print("Сдача ",money - 400)

input("Для выхода нажмите ENTER")