import turtle

wn = turtle.Screen()
wn.title("Pong by @_adam.stark_")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("white")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)

#Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("white")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Courier", 20, "bold"))

#Functions
def player_a_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)

def player_a_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)

def player_b_up():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)

def player_b_down():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)

#Keyboard binds
wn.listen()
wn.onkeypress(player_a_up, "w")

wn.listen()
wn.onkeypress(player_a_down, "s")

wn.listen()
wn.onkeypress(player_b_up, "Up")

wn.listen()
wn.onkeypress(player_b_down, "Down")  

#Main game loop
while True:
    wn.update()
    
    #Ball movement
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy) 
    
    #Top and Bottom border
    if ball.ycor() > 290:            
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    #Left and Right border
    if ball.xcor() > 380:            
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))

    #Player collisions
    if ball.xcor() < -340 and (ball.ycor() < player_a.ycor() + 40 and ball.ycor() > player_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
    if ball.xcor() > 340 and (ball.ycor() < player_b.ycor() + 40 and ball.ycor() > player_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1