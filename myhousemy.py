import turtle as t

def draw_house(x: int, y: int, height: int, width: int):
    """ 
        Рисует дом в координатах X и Y;
        X и Y – координаты нижней средней точки фундамента;
        height – полная выстоа дома (с фундаментом, стенами и крышей) 
    """
    t.shape("turtle")
    t.speed("fastest")
    t.penup()

    #фундамент
    foundation_line_color = "#000"
    foundation_fill_color = "#B8B799"
    foundation_height = height * 0.05
    #стены
    wall_line_color = "#000"
    wall_fill_color = "#999950"
    wall_plus_roof_height = height * 0.95
    wall_height = wall_plus_roof_height * 0.62
    #крыша
    roof_height = wall_plus_roof_height * 0.38
    roof_width = width / 2 * 1.1
    roof_line_color = "#000"
    roof_fill_color = "#593315"
    #Дверь
    door_line_color = "#000"
    door_fill_color = "#52442C"
    door_width = width * 0.2
    door_height = wall_height * 0.8
    #Окно
    window_line_color = "#000"
    window_fill_color = "#F0F8FF"
    window_height = door_height / 2 
    window_width = door_width * 1.1
    # считаем параметры
    heights_of_wall_and_foundation = wall_height + foundation_height

    print(f"Дом нарисован в X {x} и Y {y} высотой {height} и шириной {width}")

    def draw_recktangle(x, y, width, height, foundation_line_color, foundation_fill_color):
        """
            TODO
        """
        t.color(foundation_line_color, foundation_fill_color)
        t.pendown()
        t.begin_fill()
        t.fd(width / 2)
        t.lt(90)
        t.fd(height)
        t.lt(90)
        t.fd(width)
        t.lt(90)
        t.fd(height)
        t.lt(90)
        t.fd(width / 2)
        t.end_fill()
        t.penup()

    def draw_foundation():
        # TODO Выделить цвета в переменные
        t.goto(x, y)
        draw_recktangle(0, 0, width, foundation_height, foundation_line_color, foundation_fill_color)

        print(f"Нарисовал фундамент в X {x} и Y {y} \n высотой {foundation_height}")

    def draw_walls():
        t.goto(x, y + foundation_height)
        draw_recktangle(0, 0, width, wall_height, wall_line_color, wall_fill_color)

        print(f"Нарисовал фундамент в X {x} и Y {y + foundation_height} \n высотой {wall_height}")

    def draw_door():
        draw_recktangle(0, 0, door_width, door_height, door_line_color, door_fill_color)

    def draw_roof():
        t.color(roof_line_color,roof_fill_color)
        t.goto(x, y + heights_of_wall_and_foundation)
        t.pendown()
        t.begin_fill()
        t.fd(roof_width)
        t.goto(x, y + foundation_height + wall_height + roof_height)
        t.goto(x - roof_width, y + foundation_height + wall_height)
        t.goto(x, y + heights_of_wall_and_foundation)
        t.end_fill()
        t.penup()
  
    def draw_window():
        t.color(window_line_color, window_fill_color)
        t.goto(x + door_width * 0.8, y + door_height * 0.6)
        t.pendown()
        t.begin_fill()
        t.fd(door_width * 1.5)
        t.lt(90)
        t.fd(door_height * 0.4)
        t.lt(90)
        t.fd(door_width * 1.5)
        t.lt(90)
        t.fd(door_height * 0.4)
        t.penup()
        t.goto(x - door_width * 0.8, y + door_height * 0.6)
        t.pendown()
        t.lt(-90)
        t.fd(door_width * 1.5)
        t.lt(-90)
        t.fd(door_height * 0.4)
        t.lt(-90)
        t.fd(door_width * 1.5)
        t.lt(-90)
        t.fd(door_height * 0.4)
        t.end_fill()
        t.penup()


    draw_foundation()
    draw_walls()
    draw_door()
    draw_roof()
    draw_window()

draw_house(0, -200, 300, 500)
t.mainloop()