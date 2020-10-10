def location_rich():
    print("Вы собираетесь разбогатеть")
    user_answer = int(input("Куда пойти? "))
    if user_answer == 1:
        location_stone()
    else:
    	location_rich()

def location_stone():
    print("Вы у трех дорог")
    user_answer = int(input("Куда пойти? "))
    if user_answer == 1:
        location_rich()
    else:
    	location_stone()

location_stone()