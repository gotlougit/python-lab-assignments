import turtle

# Set up turtle
t = turtle.Turtle()
t.speed('fastest')
t.penup()

# Draw five circles with different radii
radii = [50, 40, 30, 20, 10]
for r in radii:
    t.goto(0, -r)
    t.pendown()
    t.circle(r)
    t.penup()

# Exit on click
turtle.exitonclick()

