import my_test_2_0 as t

def main():
    global player
    player = t.Player("Иван", "Иван", 1, 100, 2)
    player.print_stats()
    
    def fight():
        def create_enemy():
            global enemy
            enemy = t.Enemy(1)
            enemy.print_stats()
            
        def battle(player, enemy):
            while player.hp > 0 or enemy.hp > 0:
                enemy.change_stats(player.attack)
                print (enemy.name, enemy.surname,)

        create_enemy()
        battle(player, enemy)
    fight()

main()