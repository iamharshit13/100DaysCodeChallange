import time
import turtle

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=500, height=500)
window.title("Ohh a Clock")
window.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

def display_clock(h , m , s , pen):
    pen.up()
    pen.goto(0,200)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(200)

    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):

        pen.fd(180)
        pen.pendown()
        pen.fd(15)
        pen.penup()

        pen.goto(0,0)
        pen.rt(30)

    #HOUR
    pen.penup()
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle = h*30
    pen.rt(angle)
    pen.pendown()
    pen.fd(80)

    #MINUTE
    pen.penup()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)
    angle = m * 6
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    #SECONG
    pen.penup()
    pen.goto(0, 0)
    pen.color("green")
    pen.setheading(90)
    angle = s * 6
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)


while True:
    h= int(time.strftime("%I"))
    m= int(time.strftime("%M"))
    s= int(time.strftime("%S"))

    display_clock(h,m,s,pen)
    window.update()
    time.sleep(1)
    pen.clear()

window.mainloop()
