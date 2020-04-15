import turtle
def drawSnake(rad,angle,len,neckrad):
    color = ['blue','green','red','pink']
    for i in range(len):
        turtle.pencolor(color[i])
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

