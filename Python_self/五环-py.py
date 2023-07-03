#奥运五环
import turtle
wuhuan_yanse = {'lan' : 'blue', 'hei' : 'black', 'hong' : 'red', 'huang' : 'yellow', 'lu' : 'green'}
turtle.setup(1.0,1.0) #设置窗口大小
turtle.title("奥运五环")
#蓝圆
turtle.penup()
turtle.right(90)
turtle.forward(-50)
turtle.left(90)
turtle.forward(-200)
turtle.pendown()
turtle.pensize(10)
turtle.color(wuhuan['lan'])
turtle.circle(100)
#黑圆
turtle.penup()
turtle.forward(250)
turtle.pendown()
turtle.pensize(10)
turtle.color(wuhuan['hei'])
turtle.circle(100)
#红圆
turtle.penup()
turtle.forward(250)
turtle.pendown()
turtle.pensize(10)
turtle.color(wuhuan['hong'])
turtle.circle(100)
#黄圆
turtle.penup()
turtle.forward(-275)
turtle.right(-90)
turtle.pendown()
turtle.pensize(10)
turtle.color(wuhuan['huang'])
turtle.circle(100)
#绿圆
turtle.penup()
turtle.left(-90)
turtle.forward(50)
turtle.right(90)
turtle.pendown()
turtle.pensize(10)
turtle.color(wuhuan['lu'])
turtle.circle(100)

turtle.done()#保存画布