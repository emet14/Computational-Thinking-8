import turtle

t = turtle.Turtle()
t.speed(1000000)

t.goto(-50, -70)
t.color("cyan")

colors = ["pink", "red", "purple"]
for i in range(1000):
    t.forward( 100 + i )
    t.left( 60 )
    t.forward(100)
    t.left(60 + 1)
    t.color(colors[i%3])



turtle.exitonclick()