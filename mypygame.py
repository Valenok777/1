import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#
WIDTH_RECT = 120
HEIGHT_RECT = 100

# Создаем игру и окно
pygame.init() # инициализация игры
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # создал экран
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Цикл игры
run = True
while run:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get(): # event - событие 
        # check for closing window
        if event.type == pygame.QUIT:
            run = False

    # Рендеринг
    screen.fill(RED)
    pygame.draw.rect(screen, GREEN, ((WIDTH - WIDTH_RECT) / 2, (HEIGHT - HEIGHT_RECT) / 2, WIDTH_RECT, HEIGHT_RECT)) # параметры: где рисовать, какого цвета, координаты. 1 - X, 2 - Y, 3 - ширина, 4 - высота.
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()