import turtle as t
import random

# настройка черепахи
t.setup(width = 1.0, height = 1.0)
t.speed(0)
t.penup()

user_rows = int(input("Введите количество рядов, но количество рядов должно быть больше нуля и меньше шести "))
user_columns = int(input("Введите количество домов, но количество домов должно быть больше нуля и меньше шести "))
user_initial_x = int(input("Введите начальный X(-300) "))
user_initial_y = int(input("Введите начальный Y(-300) "))

def draw_house(x: int, y: int, width: int, height: int, line_color, foundation_fill_color, walls_fill_color, door_fill_color, roof_fill_color):
    """
        Рисует дом из нижней центральной точки x и y
        width – ширина дома
        height – полная высота дома (с фундаментом, стенами и крышей)
        foundation_fill_color – шестнадцатиричный цвет заливки фундамента (например, #00ff00)
        walls_fill_color – цвет заливки стен
        door_fill_color – цвет заливки двери
        roof_fill_color – цвет заливки крыши
        TODO сделать правила проверки аргументов
    """
    # фундамент
    foundation_height = height * 0.05

    # стены
    walls_height = height * 0.618

    # дверь
    door_width = width * 0.3
    door_height = walls_height * 0.7

    # крыша
    roof_width = width * 1.2
    roof_height = height * 0.382

    def draw_rectangle(x: int, y: int, width: int, height: int, line_color: str, fill_color: str):
        """
            Рисует прямоугольник из центральной нижней точки в координатах x и y
            width ширина прямоугольника
            height высота прямоугольника
            line_color шестнадцатиричный цвет контура прямоугольника (например #ffffff)
            fill_color шестнадцатиричный цвет заливки прямоугольника (например #ffffff)
        """
        t.goto(x, y)
        t.setheading(0)
        t.color(line_color, fill_color)
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
        """ Рисует фундамент """
        draw_rectangle(x, y, width, foundation_height, line_color, foundation_fill_color)

    def draw_walls():
        """ Рисует стены """
        draw_rectangle(x, y + foundation_height, width, walls_height, line_color, walls_fill_color)
        
    def draw_door():
        """ Рисует дверь """
        draw_rectangle(x, y + foundation_height, door_width, door_height, line_color, door_fill_color)

    def draw_roof():
        """ Рисует крышу """
        # TODO посчитать гипотенузу и нижний угол крыши
        # roof_diagonal_length = math.sqrt((width / 2) ** 2 + roof_height ** 2)
        t.goto(x, y + foundation_height + walls_height)
        t.setheading(0)
        t.color(line_color, roof_fill_color)
        t.pendown()
        t.begin_fill()
        t.fd(roof_width / 2)
        t.goto(x, y + foundation_height + walls_height + roof_height)
        t.goto(x - roof_width / 2, y + foundation_height + walls_height)
        t.fd(roof_width / 2)
        t.end_fill()
        t.penup()

    def draw_summary():
        """ Рисует отчет в правом нижнем углу фундамента """
        t.goto(x + (width / 2) + 20, y)
        t.color("#000")
        t.write(f"нарисован дом в \n X {x}, Y {y} \n высота {height}, ширина {width}")

    draw_foundation()
    draw_walls()
    draw_door()
    draw_roof()
    # draw_summary()


def draw_street(rows: int, columns: int, initial_x: int, initial_y: int):
    foundation_color_list = ["#5F1D2B", "#551A26", "#6F3340", "#4C1722", "#7F4A55"]
    walls_color_list = ["#cdac79", "#b89a6c", "#d2b486", "#a48960", "#d7bc93"]
    door_color_list = ["#9D7E68", "#8d715d", "#7d6453", "#a68a77", "#b09786"]
    roof_color_list = ["#bba37d", "#a89270", "#958264", "#c1ac8a", "#c8b597"]
    def choose_color(list):
        return list[random.randrange(0, len(list))]

    if rows < 0:
        print("Количество рядов должно быть больше нуля")
    if rows > 6:
        print("Количество рядов должно быть меньше шести")
    if columns < 0:
        print("Количество домов должно быть больше нуля")
    if columns > 6:
        print("Количество домов должно быть меньше шести") 
    if initial_x != -300:
        print("Начальный X должен быть -300")
    if initial_y != -300:
        print("Начальный Y должен быть -300")  
    else:
        for i in range(rows):
            for i in range(columns):
                draw_house(initial_x, initial_y, 100, 100, "#000", choose_color(foundation_color_list), choose_color(walls_color_list), choose_color(door_color_list), choose_color(roof_color_list))
                initial_x += 150
            initial_x = -300
            initial_y += 130

        print("Количество рядов должно быть больше нуля и меньше шести")

draw_street(user_rows, user_columns, user_initial_x, user_initial_y)

# ts = t.getscreen()
# ts.getcanvas().postscript(file="street.eps")

t.mainloop()