hero0 = {
    "имя": "Василий",
    "возраст": 52,
    "здоровье": 100,
}

hero1 = {
    "имя": "Анатолий",
    "возраст": 56,
    "здоровье": 94,
}

hero2 = {
    "имя": "Ростислав",
    "возраст": 28,
    "здоровье": 85,
}

def show_hero(*kortezh_geroy) :
    for geroy in kortezh_geroy:
        print(geroy)

show_hero(hero0, hero1, hero2)