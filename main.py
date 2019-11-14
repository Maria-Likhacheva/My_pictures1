import turtle

def sguare(x, y, size, colour, angle)
    # TODO: (Maria)
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.right(angle)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()
    turtle.up()
    turtle.home()
    pass

def triangle(x, y, size, colour, angle)
    # TODO: (Irina)
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.up()
    turtle.goto(x, y)
    turtlr.down()
    turtle.right(angle)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.end_fill()
    turtle.up()
    turtle.home()
    pass

def main():
    # TODO: (Maria) Figure 1
    square(-250, 150, 100, 'orange', 0)
    pass
    # TODO: (Maria) Figure 2
    square(-250, 0, 50, 'violet', 0)
    square(-250, 50, 50, 'slateblue', 0)
    square(-200, 0, 50, 'slateblue', 0)
    square(-200, 50, 50, 'violet', 0)
    square(-150, 90, 40, 'orange', 0)
    triangle(-200, 50, 40, 'orange', 225)
    triangle(-150, 0, 40, 'orange', 345)
    triangle(-200, -50, 40, 'orange', 75)
    triangle(-250, 0, 40, 'orange', 135)
    
    pass
    # TODO: (Maria) Figure 3
    pass
    # TODO: (Irina) Figure 1
    triangle(150, 150, 100, 'purple', 0)
    pass
    # TODO: (Irina) Figure 2
    pass
    # TODO: (Irina) Figure 3
    pass
