import turtle
def spiral(sides,turn,color,width):
    
  t = turtle.Turtle()
  t.color(color)
  t.width(width)
  for n in range(sides):
    t.forward(n)
    t.right(turn)
spiral(40,30,'green',8)