import turtle

screen = turtle.Screen()
screen.bgcolor("black")

shiv = turtle.Turtle()
shiv.speed(5)
shiv.pensize(3)
shiv.color("white")

def draw_circle(x, y, r):
    shiv.penup()
    shiv.goto(x, y - r)
    shiv.pendown()
    shiv.circle(r)

# Face outline
draw_circle(0, 0, 100)

# Eyes
shiv.color("white")
for eye_x in [-40, 40]:
    shiv.penup()
    shiv.goto(eye_x, 30)
    shiv.setheading(0)
    shiv.pendown()
    shiv.circle(10)

# Third eye (red)
shiv.penup()
shiv.goto(0, 70)
shiv.dot(20, "red")

# Crescent Moon
shiv.penup()
shiv.goto(-20, 120)
shiv.color("gray")
shiv.begin_fill()
shiv.circle(15)
shiv.end_fill()

shiv.color("black")
shiv.goto(-10, 120)
shiv.begin_fill()
shiv.circle(15)
shiv.end_fill()

# Tilak (3 white lines)
shiv.color("white")
for i in range(3):
    shiv.penup()
    shiv.goto(-25, 90 - i*7)
    shiv.setheading(0)
    shiv.pendown()
    shiv.forward(50)

# Jata (hair bun on top)
shiv.penup()
shiv.goto(0, 130)
shiv.dot(30, "gray")

shiv.hideturtle()
turtle.done()
