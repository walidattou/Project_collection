
from turtle import Turtle , Screen
import random
import time
#vars
game_runing = True
rlist = [0.1,0.2,0.3]
x = random.randint(0,2)
Rnum = 0
Lnum = 0
ss = 0
#window opt
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("ping pong")
screen.tracer(0)


#paddel class
class Paddel(Turtle) :
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(3,1)
        self.pu()
        self.goto(x,y)
    def move_up(self):
        y = self.ycor() + 50
        self.goto(self.xcor(),y)
    def move_d(self):
        y = self.ycor() - 50
        self.goto(self.xcor(),y)



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.speed(1)
        self.pu()
        self.y_move = rlist[x]
        self.x_move = 0.2
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)
    def bounc (self):
        x = random.randint(0,2)
        self.y_move +rlist[x]
        self.y_move*= -1
    def bouncx(self):
        self.x_move*= -1
        self.x_move += -0.2


def counting():
    T = Turtle()
    T.ht()
    T.color("white")
    for i in range(0,4):
        i = str(i)
        T.speed(0.2)
        T.write(i,False,align="center",font=('Arial', 100, 'normal'))
        screen.update()
        time.sleep(1)
        T.clear()
        

c = Turtle()
c.pu()
c.ht()
c.color("white")
c.speed(0.2)
c.goto(100,250)
c.write(Rnum,False,align="center",font=('Arial',34, 'normal'))

L= Turtle()
L.pu()
L.ht()
L.color("white")
L.speed(0.2)
L.goto(-100,250)
L.write(Lnum,False,align="center",font=('Arial',34, 'normal'))
 
        
        



Rpaddel = Paddel(300,1)           
Lpaddel = Paddel(-300,1)           
sall = Ball()


screen.onkey(Rpaddel.move_up , "Up")
screen.onkey(Rpaddel.move_d , "Down")

screen.onkey(Lpaddel.move_up , "z")
screen.onkey(Lpaddel.move_d , "s")

screen.listen()

counting()

while game_runing :

    h = random.randint(1,180)
    t = random.randint(1,2)
    screen.update()
    sall.move()

    if Rpaddel.ycor() > 251  :
        Rpaddel.goto(Rpaddel.xcor(),Rpaddel.ycor()-20)
    if Rpaddel.ycor() < -251 :
        Rpaddel.goto(Rpaddel.xcor(),Rpaddel.ycor()+20)
    

    if Lpaddel.ycor() > 251  :
        Lpaddel.goto(Lpaddel.xcor(),Lpaddel.ycor()-20)
    if Lpaddel.ycor() < -251 :
        Lpaddel.goto(Lpaddel.xcor(),Lpaddel.ycor()+20)
    

    if sall.ycor() > 290 or sall.ycor() < -290 :
        sall.bounc()
    if sall.distance(Rpaddel) < 40 and sall.distance(Rpaddel.xcor(),290) :
        sall.bouncx()
        r = sall.xcor()-1
        sall.goto(r,sall.ycor())
    if sall.distance(Lpaddel) < 40 and sall.distance(Rpaddel.xcor(),-290) :
        sall.bouncx()
        r = sall.xcor()+1
        sall.goto(r,sall.ycor())
    
    if sall.xcor() > 400 :
        Rnum += 1
        c.clear()
        c.write(Rnum,False,align="center",font=('Arial',34, 'normal'))


       
        sall.goto(0,0)
        sall.bouncx()
        sall.move()
        
        print(Rnum)
        

    if sall.xcor() < -400 :
        Lnum += 1
        L.clear()
        L.write(Rnum,False,align="center",font=('Arial',34, 'normal'))

        
        sall.goto(0,0)
        sall.bouncx()
        sall.move()

 



screen.exitonclick()
