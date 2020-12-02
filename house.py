import turtle as t
import math

def draw_street():
    def draw_house_row(intial_x, house_shift):
        for x in range(house_number):
            draw_house(-100, -100, 50, 60)

    def draw_house_row()

def draw_house(x: int, y: int, width: int, height: int):
    """ 
        Рисует дом в координатах X и Y;
        X и Y – координаты нижней средней точки фундамента;
        height – полная выстоа дома (с фундаментом, стенами и крышей) 
    """
    t.shape("turtle")
    t.speed("fastest")
    t.penup()

    # фундамент
    foundation_height = height * 0.05
    foundation_line_color = "#000"
    foundation_fill_color = "#6B6B69"
    # стены
    wall_plus_roof_height = height * 0.95
    wall_height = wall_plus_roof_height * 0.62
    wall_line_color = "#000"
    wall_fill_color = "#ffa54f"
    # дверь
    door_width = width * 0.2
    door_height = wall_height * 0.8
    door_line_color = "#000"
    door_fill_color = "red"
    #jryj
    # крыша
    roof_height = wall_plus_roof_height * 0.38
    roof_width = width / 2 * 1.3
    roof_line_color = "#000"
    roof_fill_color = "#a0522d"

    print(f"Дом нарисован в X {x} и Y {y} высотой {height} и шириной {width}")

    def draw_rectangle(x, y, width, height, line_color, fill_color):
        """
        TODO написать документ-строку
        """
        t.color(line_color, fill_color)
        t.goto(x, y)
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
        draw_rectangle(x, y, width, foundation_height, foundation_line_color, foundation_fill_color)
        
    def draw_walls():
        draw_rectangle(x, y + foundation_height, width, wall_height, wall_line_color, wall_fill_color)

    def draw_door():
    	draw_rectangle(x, y + foundation_height, door_width, door_height, door_line_color, door_fill_color)

    def draw_roof():
        t.color(roof_line_color, roof_fill_color)
        t.goto(x, y + foundation_height + wall_height)
        t.pendown()
        t.begin_fill()
        t.fd(roof_width)
        t.goto(x, y + foundation_height + wall_height + roof_height)
        t.goto(x - roof_width, y + foundation_height + wall_height)
        t.fd(roof_width)
        t.end_fill()
        t.penup()

    draw_foundation()
    draw_walls()
    draw_door()
    draw_roof()

draw_street(5, -100, 100)

t.mainloop()
