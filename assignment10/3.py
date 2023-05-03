import turtle
import math

t = turtle.Turtle()

size = 200

colors = ["red", "yellow", "orange", "lightgreen", "purple"]
t.speed(1)
for i in range(5):
    t.color(colors[i])
    t.begin_fill()
    t.color(colors[i])
    t.goto(0, 0)
    t.goto(size * 0.5 * math.cos(i * 2 * math.pi / 5),
    size * 0.5 * math.sin(i * 2 * math.pi / 5))
    t.goto(size * 0.5 * math.cos((i + 1) * 2 * math.pi / 5),
    size * 0.5 * math.sin((i + 1) * 2 * math.pi / 5))
    t.goto(0, 0)
    t.end_fill()

t.hideturtle()

turtle.mainloop()
