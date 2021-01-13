from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d


# создаю экземпляры классов
app = Ursina()

player = player_controller = PlatformerController2d(
	position = (0, 0),
	collision = True,
	)

surface = Entity(
    position = (0, -2),
    model = 'quad',
    collider = 'box',
    scale=(50,1),
	)

camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=40))

def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt


def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)


# start running the game
app.run()