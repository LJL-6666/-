import turtle as t

def infoPrt():
    print('coordinate: ' + str(t.pos()))
    print('angle: ' + str(t.heading()))

t.pensize(3)
t.hideturtle()
t.colormode(255)
t.color("black")
t.setup(700, 650)
t.speed(10)
t.st()
#t.dot()
t.pu()
#t.goto(-150,100)
t.goto(-210,86)
t.pd()
infoPrt()

# 头
print('头')
t.seth(85)
t.circle(-100,50)
#t.seth(78)
#t.circle(-100,25)
infoPrt()

t.seth(25)
t.circle(-170,50)
infoPrt()

# 右耳
print('右耳')
t.seth(40)
#t.circle(-250,52)
t.circle(-250,30)
infoPrt()
# 右耳尖
t.begin_fill()
# 左
t.circle(-250,22)
#t.fillcolor("pink")
# 右
t.seth(227)
t.circle(-270, 15)

prePos = t.pos()
infoPrt()
# 尾巴
t.pu()
t.setpos(p_tail)
t.pd()

t.begin_fill()
t.seth(50)
t.fd(25)
t.seth(-50)
t.fd(30)
p_tail1=t.pos
t.seth(-140)
t.fd(36)
t.end_fill()
t.seth(39)

# 右尾和h1
t.fd(72)

# 右尾和v1
t.seth(125)
t.fd(48)

# 右尾和h2
t.seth(40)
t.fd(53)

# 右尾和v2
t.seth(88)
t.fd(45)

# 右尾和h3
t.seth(35)
t.fd(105)
# 右尾和v3
t.seth(105)
t.circle(850, 8)
#t.fd(105)
t.seth(215)
#t.fd(125)
t.circle(850, 11)
t.seth(280)
t.fd(110)
t.seth(220)
t.fd(50)
t.seth(309)
t.fd(56)
