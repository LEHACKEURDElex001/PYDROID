import turtle

a = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
a.speed(0)
a.hideturtle()

a.color('cyan')

for x in range(200):
    a.forward(x)
    a.left(x - 1)

a.penup()
a.goto(-200, 150)
a.pendown()

a.color('cyan')
a.write("Votre texte ici", font=("Arial", 26, "bold"))

turtle.done()