import turtle
import math

# Define points
p1 = (-50, 50)
p2 = (50, -50)

# Calculate midpoint
midpoint = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Calculate distance between points
distance = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Set up turtle
t = turtle.Turtle()
t.speed('fastest')
t.penup()

# Draw first point
t.goto(p1)
t.dot(5, 'black')
t.write(f'({p1[0]}, {p1[1]})', align='right')

# Draw second point
t.goto(p2)
t.dot(5, 'black')
t.write(f'({p2[0]}, {p2[1]})', align='left')

# Draw midpoint
t.goto(midpoint)
t.dot(5, 'red')
t.write(f'({midpoint[0]}, {midpoint[1]})', align='center')

# Draw line connecting points
t.goto(p1)
t.pendown()
t.goto(p2)

# Write distance between points
t.penup()
t.goto(midpoint[0], midpoint[1] - 20)
t.write(f'Distance = {distance:.2f}', align='center')

# Exit on click
turtle.exitonclick()
