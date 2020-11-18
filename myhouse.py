import turtle as t 

def draw_house(x: int, y: int, height: int, width: int):
    """
        turtle - это модуль
        Рисует дом в координатах X и Y
        X и Y - координаты нижней средней точки фундамента
        Height - полная высота дома (с фундаментом, стенами и крышей)
    """
    print(f"Дом нарисовон в X {x} и Y {y} высотой {height} и шириной {width}")
    def draw_foundation():
        foundation_height = height * 0.05
        t.shape("turtle")
        t.speed("fast")
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fd(width / 2)
        t.lt(90)
        t.fd(foundation_height)
        t.lt(90)
        t.fd(width)
        t.lt(90)
        t.fd(foundation_height)
        t.lt(90)
        t.fd(width / 2)
        t.mainloop()
        print(f"Нарисовал фундамент в X {x} и Y {y} высотой {foundation_height}")
    def draw_walls():
        pass
    def draw_roof():
        pass
    draw_foundation()

draw_house(0, 0, 300, 500)