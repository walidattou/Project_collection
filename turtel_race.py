from turtle import Turtle , Screen
import random

colors = ["red","orange","yellow","green","blue","purple"]
Tnames = ["walid","rima","sara","nasrin","nabile","akila"]
m = -120
race = False



#window int
screen = Screen()
screen.bgcolor("black")
screen.setup(900,500)
bet = screen.textinput("bet","who is gonna win the race ?")


#turtel movments

def starting_pos(self,m):
    self.pu()
    self.goto(x =-400,y = m)
    self.pd()


#player int 
for i in range(0,len(colors)):
    Tnames[i] = Turtle(shape="turtle")
    Tnames[i].color(colors[i])
    starting_pos(Tnames[i],m)
    m += 50


#racist time

if bet:
    race = True
while race:
    for t in Tnames:
     if t.xcor() > 350:
        w = t.pencolor()
        race = False
        print(f"winning turtel is : {w}")
        if w == bet:
           print("you won congrats , now go do something better with your life ")
        else:
            print("you lost")
    
            
     t.fd(random.randint(0,10))



screen.exitonclick()
