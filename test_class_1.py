class Zombie():
    def __init__(self, name = "Неизвестный"):
        self.hp = 100
        self.name = name

    def show(self):
        print(self.hp, self.name, self.is_alive, sep = "\n")


class Player():
    def __init__(self, name = "Неизвестный"):
        self.hp = 100
        self.name = name

    def show(self):
        print(self.hp, self.name, self.is_alive, sep = "\n")


enemy1 = Zombie("Вася")
enemy1 = show()

player1 = Player("Иван")
player1 = show()


