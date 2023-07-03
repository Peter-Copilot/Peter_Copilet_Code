from turtle import *
from datetime import *

def skip(step):
    penup()
    forward(step)
    pendown()

def mkhand(name,length):
    #注册turtle形状，建立表针turtle
    reset()
    skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handform=get_poly()
    register_shape(name,handform)

def init():
    global sechand,minhand,hurhand,printer
    mode("logo")
    #重置turtle指向北
    #建立三个表针turtle并初始化
    mkhand("sechand",160)
    mkhand("minhand",130)
    mkhand("hurhand",90)
    sechand=Turtle()
    sechand.shape("sechand")
    minhand=Turtle()
    minhand.shape("minhand")
    hurhand=Turtle()
    hurhand.shape("hurhand")
    for hand in sechand,minhand,hurhand:
        hand.shapesize(1,1,3)
        hand.speed(0)
    #建立输出文字turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()

def setupclock(radius):
    #建立表的外框
    reset()
    pencolor('black')
    pensize(10)
    for i in range(60):
        skip(radius)
        if i %5==0:
            forward(20)
            skip(-radius-20)
        else:
            dot(5)
            skip(-radius)
        right(6)

def week(t):
    week=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
    return week[t.weekday()]

def date(t):
    y=t.year
    m=t.month
    d=t.day
    return "%s %d %d" %(y,m,d)

def tick():
    #绘制表针的动态显示
    t=datetime.today()
    second=t.second+t.microsecond*0.000001
    minute=t.minute+second/60.0
    hour=t.hour+minute/60.0
    sechand.setheading(6*second)
    minhand.setheading(6*minute)
    hurhand.setheading(30*hour)
    tracer(False)
    printer.forward(65)
    printer.write(week(t),align="center",font=("Courier",20,"bold"))
    printer.back(130)
    printer.write(date(t),align="center",font=("Courier",20,"bold"))
    printer.home()
    tracer(True)
    ontimer(tick,100)#100ms后继续调用tick

def main():
    tracer(False)
    init()
    setupclock(250)
    tracer(True)
    tick()
    mainloop()
main()
