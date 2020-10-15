import turtle
myPen =turtle.Pen()
for i in range(4):
    for j in range(3):
        myPen.forward(100)
        myPen.dot(5)
    myPen.goto(0,0)
    myPen.left(90)
myPen.dot(5)
myPen.hideturtle()
turtle.done()