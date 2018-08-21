import turtle
from tkinter import*
import math
import random
import sys
import time
speed=3
score=-1

class screen(object):
    wn=turtle.Screen()
    def __init__(self):
        self.wn.title("game")
        self.wn.bgcolor("yellow")
        #self.wn.bgpic('new.gif')
    
    
class game(screen):
    #for border
    scr_turtle=turtle.Turtle()
    border=turtle.Turtle()
    def __init__(self):
        self.border.penup()
        self.border.hideturtle()
        self.border.color("white")
        self.border.setposition(-350,-350)
        self.border.shape("turtle")
        self.border.pensize(5)
        self.border.speed(0)
        #wn.bgpic("tumblr_mduqruzbIc1qktq7uo1_500.gif")self.border.bgpic("turtle.gif")
        self.border.color("green")
        for self.border.side in range (4):
           
           self.border.forward(700)
           self.border.left(90)
     #for player
class players(game):
    score=-1
    achive=turtle.Turtle()
    def __init__(self):
        self.achive.shape("triangle")
        self.achive.pensize(5)
        self.achive.speed(0)
        self.achive.penup()
        self.achive.forward(100)
        game.scr_turtle.hideturtle()
        game.scr_turtle.penup()
        game.scr_turtle.setposition(-340,310)
        game.scr_turtle.write(score)
        
    hurdle=turtle.Turtle()
    def hurdles1(self):
        self.hurdle.penup()
        self.hurdle.setposition(-210,210)
        self.hurdle.color("grey")
        self.hurdle.shape("square")
        self.hurdle.pensize(10)
        
        #self.time.sleep(5)
        #self.hurdle.setposition(random.randint(-310,310),random.randint(-310,310))
    player=turtle.Turtle()
    title=turtle.Turtle()
    title.hideturtle()
    title.penup()
    def ply(self):
        self.player.penup()
        self.player.shape("turtle")
        self.player.pensize(5)
        self.player.speed(1)
        
        
        while True:
            #FOR ACHIVEMENT MOVEMENT
            self.achive.forward(3)
            self.hurdle.backward(2)
            if self.achive.xcor()> 320 or self.achive. xcor() < -320:
                self.achive.right(random.randint(0,90))
                
            if self.achive.ycor()> 320 or self.achive.ycor() < -320:
                self.achive.right(random.randint(0,90))

            if self.hurdle.xcor()> 320 or self.hurdle. xcor() < -320:
                self.hurdle.right(random.randint(0,90))
                
            if self.hurdle.ycor()> 320 or self.hurdle.ycor() < -320:
                self.hurdle.right(random.randint(0,90))

            #FOR PLAYER MOVEMENT
            self.player.forward(speed)
            
            if self.player.xcor()> 330 or self.player. xcor() < -330:
                #self.player.right(90)
                self.title.hideturtle()
                self.player.hideturtle()
                self.achive.hideturtle()
                self.hurdle.hideturtle()
                self.title.write("game over",align="center", font=("classic", 100, "bold"))
                self.title.write("press C to playagain",align="center", font=("arial", 20, "bold italic"))
            
            if self.player.ycor()> 330 or self.player.ycor() < -330:
                #self.player.right(90)
                
                self.player.hideturtle()
                self.achive.hideturtle()
                self.hurdle.hideturtle()
                self.title.write("game over ",align="center", font=("classic", 100, "bold"))
            d = math.sqrt(math.pow(self.player.xcor()-self.achive.xcor(),2)+math.pow(self.player.ycor()-self.achive.ycor(),2))
            if d<10:
                
                players.score+=1
                game.scr_turtle.undo()
                game.scr_turtle.write(players.score)
                
                self.achive.setposition(random.randint(-310,310),random.randint(-310,310))
            k = math.sqrt(math.pow(self.player.xcor()-self.hurdle.xcor(),2)+math.pow(self.player.ycor()-self.hurdle.ycor(),2))
            if k<15:
                players.score-=1
                game.scr_turtle.undo()
                game.scr_turtle.write(players.score)
                self.achive.setposition(random.randint(-310,310),random.randint(-310,310))
                self.hurdle.setposition(random.randint(-310,310),random.randint(-310,310))
                
                
class keys(game):
    def left():
        players.player.left(45)
    screen.wn.onkey(left, "Left")
    screen.wn.listen()
    def right():
        players.player.right(45)
    screen.wn.onkey(right, "Right")
    screen.wn.listen()
    def up():
        global speed
        speed+=2
    screen.wn.onkey(up, "Up")
    screen.wn.listen()
    def down():
        global speed
        speed-=1
        screen.wn.onkey(down, "Down")
    screen.wn.listen()
    def stop():
        global speed
        speed-=speed
        screen.wn.onkey(stop, "a")
    screen.wn.listen()
    def resume():
        import bothmoving
        screen.wn.onkey(resume,'Down')
    screen.wn.listen()
time1=30
label=Label(text= "time",font=20,bg='yellow')
label.pack(fill=X)
btn_destroy=Button(text='Exit', relief="raised",font=("arial black", 10), command=lambda:screen.wn.bye())
btn_destroy.pack(fill=X)
##btn_resume=Button(text='play again', relief="raised",font=("arial black", 10), command=resume)
##btn_resume.pack()
def timer():
    tur=turtle.Turtle()
    tur.penup()
    tur.hideturtle()
    tur.setposition(-290,290)
    
    global time1
    if time1!=0:
        time1-=1
        label.config(text=time1)
        
    elif time1==0:
        y1.title.write("time over ",align="center", font=("classic", 100, "bold"))
        y1.player.hideturtle()
        y1.achive.hideturtle()
        y1.title.undo()

    label.after(1000,timer)
    
a=screen()
screen.wn.exitonclick()
timer()
x=game()
y1=players()
y1.hurdles1()
y1.ply()
y1.title()
