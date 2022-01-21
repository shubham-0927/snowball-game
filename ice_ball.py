import turtle as t
import random
window = t.Screen()
window.title("snow_ball")
window.bgcolor("skyblue")
window.setup(width=800,height=600)
window.tracer(0)

#creating snow ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(5)
ball.penup()
ball.goto(0,-220)
ball_red=0.2

#creating rain snow
whitesnow=t.Turtle()
whitesnow.speed(0)
whitesnow.shape("circle")
whitesnow.color("white")
whitesnow.shapesize(1)
whitesnow.penup()
whitesnow.goto(random.randint(-250, 250),300)

blacksnow=t.Turtle()
blacksnow.speed(0)
blacksnow.shape("circle")
blacksnow.color("black")
blacksnow.shapesize(1)
blacksnow.penup()
blacksnow.goto(ball.xcor(),350)

#creating pen for scorecard
pen=t.Turtle()
pen.speed()
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("game starting !! ENJOY ;)", align="center",font=('Arial',24,'normal'))


def toright():
    x = ball.xcor()
    x= x+10
    ball.setx(x)

def toleft():
    x = ball.xcor()
    x = x-10
    ball.setx(x)

window.listen()
window.onkeypress(toright,"Right")
window.onkeypress(toleft,"Left")

pre= 5
count = 1
score = 0
life =3
while True:
    window.update()
    if count>=3:
        blacksnow.sety(blacksnow.ycor() - 0.1)
    whitesnow.sety(whitesnow.ycor() - 0.1)


    if (whitesnow.ycor()-ball.ycor()<pre*10) and (whitesnow.xcor()-ball.xcor()<pre *10):
        pre = pre + 0.3
        ball.shapesize(pre)
        count = count + 1
        score +=1
        whitesnow.goto(random.randint(-250, 250), 350)
        pen.clear()
        pen.write("            SCORE: {}    ❤ x {}  ".format(score,life),align='center', font=('Arial',20))

    elif whitesnow.ycor()<-350:
        count = count + 1
        whitesnow.goto(random.randint(-250, 250), 350)


    if (blacksnow.ycor()-ball.ycor()<pre*10-5) and (blacksnow.xcor()-ball.xcor()<pre*10-5):
        life = life- 1
        pre = pre - 2
        ball.shapesize(pre)
        pen.clear()
        pen.write("            SCORE: {}    ❤ x {}  ".format(score, life), align='center', font=('Arial', 20))
        blacksnow.goto(random.randint(-250, 250), 350)
        count = 1
    elif blacksnow.ycor()<-350:
        count = 1
        blacksnow.goto(random.randint(-250, 250), 350)
    if life ==0:
        t.Screen().bye()
