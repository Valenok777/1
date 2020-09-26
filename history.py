name = input("Здравствуйте!\nКак вас зовут? ")
nam = 0
while nam not in (1,2,3) :
    print(name, """
    Перед тобой 3 двери.
    Тебе нужно выбрать одну из дверей.
    1-Знакомство с другом.
    2-Смерть.
    3-Богатство.
    """)
    nam = int(input("Какую откроешь дверь? ")) #пусто не интуется
    if nam == 1:
        print("Da")
    elif nam == 2:
        print("No")
    elif nam == 3:
        print("XX")

input("")