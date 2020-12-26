import random

class Humanoid():
    def __init__(self):
        self.name = "Def"
        self.surname = "TTT"
        self.levle = 1
        self.hp = 100
        self.attack = 0

    def print_stats(self):
        print(self.name)
        print(self.surname)
        print(self.levle)
        print(self.hp)

    def change_stats(self, hp_damage):
        self.hp -= hp_damage


class Player(Humanoid):
    def __init__(self, name, surname, levle, hp, attack):
        super().__init__()
        self.name = name
        self.surname = surname
        self.levle = levle
        self.hp = hp


class Enemy(Humanoid):
    def __init__(self, levle):
        super().__init__()
        self.name = random.choice(("Грэг", "Аргк", "Хемс"))
        self.surname = random.choice(("Дерзкий", "Алчный", "Зловонный"))
        self.levle = levle
        self.hp = 100
        self.attack = 1

