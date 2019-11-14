import turtle

def square(x, y, size, colour, angle):
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

def triangle(x, y, size, colour, angle):
    # TODO: (Irina)
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
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
    turtle.reset()
    
    # TODO: (Maria) Figure 1
    square(-200, 300, 50, 'orange', 0)
    pass

    # TODO: (Irina) Figure 1
    triangle(150, 300, 50, 'purple', 0)
    pass

    # TODO: (Maria) Figure 2
    square(-250, 0, 50, 'violet', 0)
    square(-250, 50, 50, 'slateblue', 0)
    square(-200, 0, 50, 'slateblue', 0)
    square(-200, 50, 50, 'violet', 0)
    square(-150, 90, 45, 'orange', 0)
    triangle(-200, 50, 40, 'orange', 225)
    triangle(-150, 0, 40, 'orange', 345)
    triangle(-200, -50, 40, 'orange', 75)
    triangle(-250, 0, 40, 'orange', 135)
    pass

    # TODO: (Irina) Figure 2
    triangle(250, -75, 50, 'orangered', 270)
    square(200, -25, 50, 'darkorange', 0)
    square(150, -25, 50, 'darkorange', 0)
    triangle(150, -25, 50, 'orangered', 90)
    square(150, -25, 50, 'gold', 150)
    triangle(150, -25, 50, 'gold', 240)
    square(125, 18.3, 50, 'gold', 270)
    triangle(175, 68.3, 70, 'orangered', 180)
    pass

    # TODO: (Maria) Figure 3
    square(-250, -200, 50, 'lime', 0)
    square(-250, -150, 50, 'aqua', 0)
    square(-200, -200, 50, 'aqua', 0)
    square(-200, -150, 50, 'lime', 0)
    triangle(-150, -150, 100, 'yellow', 30)
    triangle(-250, -200, 100, 'dodgerblue', 150)
    triangle(-190, -150, 40, 'mediumspringgreen', 300)
    triangle(-190, -250, 40, 'mediumspringgreen', 0)
    pass

    # TODO: (Irina) Figure 3
    square(-250, -200, 50, 'lime', 0)
    square(-250, -150, 50, 'aqua', 0)
    square(-200, -200, 50, 'aqua', 0)
    square(-200, -150, 50, 'lime', 0)
    triangle(-150, -150, 100, 'yellow', 30)
    triangle(-250, -200, 100, 'dodgerblue', 150)
    triangle(-190, -150, 40, 'mediumspringgreen', 300)
    triangle(-190, -250, 40, 'mediumspringgreen', 0)
    pass

main()
