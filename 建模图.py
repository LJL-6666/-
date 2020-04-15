import turtle
def goto(x,y):
    turtle.penup()
    turtle.goto(x,y)
def yuan():
    turtle.color("#D1C185","#839F26")
    goto(0,-200)
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()
def huabian():
    goto(0,0)
    turtle.color("#839F26")
    for _ in range(10):
         turtle.right(36)
         turtle.begin_fill()
         turtle.forward(200)
         turtle.circle(40,180)
         turtle.goto(0,0)
         turtle.right(180)
         turtle.end_fill()

if __name__ == '__main__':
    turtle.speed(10)
    huabian()
    yuan()
   
turtle.done()
