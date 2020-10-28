hero0 = {
    "имя": "Василий",
    "возраст": 52,
    "здоровье": 70,
}

hero1 = {
    "имя": "Ярик",
    "возраст": 85,
    "здоровье": 10,
}

def xp_geroya(*geroyi) : #словарь в кортеж
    for hero in geroyi : #достаем одно из кучи
        hero["здоровье"] = 100

xp_geroya(hero0, hero1)

print(hero0, hero1)