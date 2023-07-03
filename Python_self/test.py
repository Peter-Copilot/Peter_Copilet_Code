import turtle

def main(n,size):
    
    pen = turtle.Pen()
    pen.up()
    pen.goto(-size*6,-size*6)
    pen.down()
    pen.lt(135)
    for _ in range(n):
        pen.forward(size)
        pen.right(360/n)
    turtle.done() 


main(96, 5)
