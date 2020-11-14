import turtle
turtle.shape("turtle")
turtle.speed("fast")
turtle.penup()
turtle.goto(0, -270)
turtle.pendown()


def drow_circle(circles:int, first_radius:int, first_color:int):
    first_color = 21
    for i in range(circles):
        turtle.colormode(255)
        turtle.color(0, 0, first_color)
        turtle.begin_fill()
        turtle.circle(first_radius)
        turtle.penup()
        turtle.lt(90)
        turtle.fd(first_radius * 2)
        turtle.rt(90)
        turtle.pendown()
        first_radius = first_radius * 0.75
        first_color = first_color + 30
        turtle.end_fill()
    #turtle.rt(90)
    #turtle.fd(first_radius / 2)
    #turtle.lt(90)
    turtle.fd(first_radius)
    turtle.lt(110)
    turtle.fd(first_radius * 1.5)
    turtle.lt(70)
    turtle.fd(first_radius)
    turtle.lt(70)
    turtle.fd(first_radius * 1.5)
    turtle.lt(110)
    turtle.fd(first_radius)
drow_circle(3, 100, 90)
turtle.mainloop()