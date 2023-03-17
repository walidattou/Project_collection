from turtle import Turtle , Screen
import random

Tom = Turtle()
game = True
Tom.color("DarkSlateGray1")
colors = ["red","green","yellow","brown","purple","black","DarkSlateGray1"]
class Tortue :
    def __init__(self,name):
        self.name = name
    def circle(self,degrees):
        while game is True:
            self.name.fd(10)
            self.name.color("black")
            degrees =- 20
            self.name.speed(20)
            self.name.circle(100)
            self.name.lt(degrees)
            self.name.fd(3)
            print(degrees)
            self.name.fd(3)
  

print(Tom.pos())
Tom = Tortue(Tom)
Tom.circle(360)

screen = Screen()
screen.exitonclick()
