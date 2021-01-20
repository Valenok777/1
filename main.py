import random
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d


# создаю экземпляры классов
app = Ursina()

window.fullscreen = True

player = player_controller = PlatformerController2d(
	position = (0, 0),
	collision = True,
	)

tile_shift_x = 0
for i in range(50):
    tile_shift_y = -3
    kolichestvo_kybikov_po_y = random.randint(2, 3)
    for j in range(kolichestvo_kybikov_po_y):
        tile = Entity(
        position = (tile_shift_x, tile_shift_y),
        model = 'quad',
        collider = 'box',
        scale=(1,1),
        color = color.green,
        )
        tile_shift_y += 1
    tile_shift_x += 1


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