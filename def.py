def location_1():
    print("""
Ты спустился по леснице в подвал, долгое время блуждал по нему.
И перед тобой появились 2 двери""")
    print("1 – Винный погреб.\n2 – Дверь без надписи.")
    user_choise = int(input("Куда пойдем? "))
    if user_choise == 1:
        print("""Ты открываешь дверь и перед тобой появляются винный залижи.
С роду ты не видел такого количества вина, и поэтом ты решил напиться до отвала.
Но эта была не самая лучшая идея, ведь после ты сразу уснул.
Проснулся ты когда тебя уже тащили по коредору.
Тебя посадили в темный подвал, где ты и провел остаток своих дней.""")
    elif user_choise == 2:
        print("""У тебя сломалась отмычка, и тебе ничего не остается как открыть другую дверь, может она не закрыта ведь отмычек у тебя больше нет.
Ты открываешь дверь и перед тобой появляются винный залижи.
С роду ты не видел такого количества вина, и поэтом ты решил напиться до отвала.
Но эта была не самая лучшая идея, ведь после ты сразу уснул.
Проснулся ты когда тебя уже тащили по коредору.
Тебя посадили в темный подвал, где ты и провел остаток своих дней.""")
    else:
    	location_1()


def location_2():
    print("""
Я думаю эта была не самая лучшая идея идти к тем кто тебя схвавит и превалок в это ужасное место.
А ты теперь даже не вернешься назад, сзади доносятся шаги и крики. 
Походу они обнаружили, что ты сбежал.
Ты начинаешь бежать и упераешься в 2 двери. """)
    print("1 – Казарма\n2 – Кладовая\nНе тяни с выбором а то тебя схватят")
    user_choise = int(input("Твой выбор? "))
    if user_choise == 1:
        print("""
Ты открываешь дверь...
А в помещении если его можно так назвать, стоит кромешная тьма.
Ты пытаешься пробраться через комнату в поиске выхода но случайно задеваешь чью-то ногу.
Тебя тут же замечают и убивают на месте.
А я тебе говорил эта плохая была идея :)""")
    elif user_choise == 2:
        print("""
Ты заходишь в кладовую, но здесь негде спрятаться и отсюда только один выход через который ты пришел.
Тебе преходиться вернуться назад.
 """)
        location_2()
    else:
    	location_2()


def location_3():
    print("""Ты идешь по коредору.
Перед тобой из-за угла появляются два бандита.
Ты пытаешься от них убежать, но они тебя все равно поймали.
Тебя куда-то тащат.
Мне это не нравится, и тебе я думаю тоже2.
Тут два выбора: """)
    print("1 – Бездействовать.\n2 – Выхватить у одного из бандитов пистолет, и попытаться выйти отсюда живым.")
    user_choise = int(input("Твой выбор: "))
    if user_choise == 1:
        print("""Тебя посадили в темный подвал, где ты и провел остаток своих дней.
Они были очень однообразный.""")
    elif user_choise == 2:
    	print("""У тебя получилось выхватить пистолет и даже убить одного из бандитов.
Но его напарник успел выстрелить тебе в грудь.
Ты упал на холодныйя, каменный пол, а через несколько минут умер.""")
    else:
    	location_3()


def location_nachalo():
    print("""
Ты попали в плен к разбойникам, они забрали у тебя все денньги и посадили в камеру.
Но к твоему ссчастью они забыли закрыть дверь на замок, и ты с легкостью выбрался из камеры.
В твоем арсенале только нож и одна отмычка.
Перед тобой 3 пути.
1 – Первый путь ведет в подвал.    
2 – Второй путь ведет в казарму разбойников.
3 – Третий путь ведет в сокровищницу.""")
    user_choise = int(input("Куда пойдем? ")) #пустой ответ не интуется!
    if user_choise == 1:
    	location_1()
    elif user_choise == 2:
    	location_2()
    elif user_choise == 3:
    	location_3()

location_nachalo()
