from os import system # для очистки экрана

user_choise = 0
level = 0

# камень
while user_choise not in (1, 2, 3):
    system('cls') # очистка экрана
    print("""
Ездил Илья по чистому полю, защищал Русь от врагов с молодых лет до старости.
Хорош был у старого добрый конь, его маленький Бурушка-Косматушка. Хвост у Бурушки трех саженей, грива до колен, а шерсть трех пядей.
Он броду не искал, перевозу не ждал, одним скоком он реки перескакивал. Он старого Илью Муромца сотни раз от смерти спасал.

Не туман с моря подымается, не белые снега в поле белеются, едет Илья Муромец по русской степи. Забелелась его головушка,
его кудрявая бородушка, затуманился его ясный взор.
- Ах ты, старость, ты, старость старая! Застала ты Илью в чистом поле, налетела черным вороном!
Ах ты, молодость, молодость молодецкая! Улетела ты от меня ясным соколом!

Подъезжает Илья к трем дорожкам, на перекрестке камень лежит, а на том камне написано:
«Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть».

Призадумался Илья Муромец:
1 – Ну, поеду теперь, где женатому быть!    
2 – Ну, поеду теперь в дорожку, где богатому быть.
3 – Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!""")
    user_choise = int(input("ваш ответ: ")) #пустой ответ не интуется!
    if user_choise == 1:
    	level = 1
    elif user_choise == 2:
    	level = 2
    elif user_choise == 3:
    	level = 3
else:
    user_choise = 0

# диагностическая печать
print("выбор юзера ", user_choise)
print("уровень ", level)
input()

#level 1 - женат
while user_choise not in (1, 2, 3) and level == 1:
    
    print("""
Сценарий женат
Призадумался Илья Муромец:
1 – Ну, поеду теперь, где женатому быть!    
2 – Ну, поеду теперь в дорожку, где богатому быть.
3 – Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!""")
    user_choise = int(input("ваш ответ: ")) #пустой ответ не интуется!
else:
    user_choise = 0

print("Конец!")
input()