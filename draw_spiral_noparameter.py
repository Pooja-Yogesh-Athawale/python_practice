import turtle

def spiral():
    t = turtle.Turtle()
    t.color("cyan")
    t.width(5)
    for n in range(100):
        t.forward(n)
        t.right(20)

spiral()