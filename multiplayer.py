import turtle
import math
import random
import sys
speed=1
'''screen = turtle.Screen()
screen.setup(600,400)
screen.bgpic('turtle.gif')
'''
class game(object):
    #for border
    border=turtle.Turtle()
    def __init__(self):
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
class player(game):
    x=4
    
    achive=[]
    def __init__(self):
        for self.count in range(self.x):
            self.achive.append(turtle.Turtle())
            self.achive[self.count].shape("triangle")
            self.achive[self.count].pensize(5)
            self.achive[self.count].speed(0)
            self.achive[self.count].penup()
            self.achive[self.count].forward(100)
    hurdle=turtle.Turtle()
    def hurdles(self):
        self.hurdle.penup()
        self.hurdle.color("grey")
        self.hurdle.shape("square")
        self.hurdle.pensize(10)
        self.hurdle.forward(30)
        self.hurdle.setposition(random.randint(-310,310),random.randint(-310,310))
    player=turtle.Turtle()
    
    def ply(self):
        self.player.penup()
        self.player.shape("turtle")
        self.player.pensize(5)
        self.player.speed(1)
    
        
        while True:
            #FOR ACHIVEMENT MOVEMENT
            self.achive[self.count].forward(1.5)
            if self.achive[self.count].xcor()> 330 or self.achive[self.count]. xcor() < -330:
                 self.achive[self.count].right(random.randint(0,90))
            if self.achive[self.count].ycor()> 330 or self.achive[self.count].ycor() < -330:
                self.achive[self.count].right(random.randint(0,90))

            #FOR PLAYER MOVEMENT
            self.player.forward(speed)
            
            if self.player.xcor()> 330 or self.player. xcor() < -330:
                 self.player.right(90)
            if self.player.ycor()> 330 or self.player.ycor() < -330:
                self.player.right(90)
            
            d = math.sqrt(math.pow(self.player.xcor()-self.achive[self.count].xcor(),2)+math.pow(self.player.ycor()-self.achive[self.count].ycor(),2))
            if d<10:
                self.achive[count].setposition(random.randint(-310,310),random.randint(-310,310))

def left():
        player.player.left(45)

    
x=game()

y=player()
y.hurdles()
y.ply()

