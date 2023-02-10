import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
items = [rock,paper,scissors]

AIchoice = random.randint(0,2)


print("type 1 for rock , 2 for paper , 3 for scissors ")
x = int(input("your type : ")) 
print(x)




if x <= 3 :
    if x == 0 :
        print("invalide choice please try again")
    elif x == 1 :
        print("you have chosen rock : \n" + items[x- 1])
        print("computer hase chosen : \n" + items[AIchoice] )
    elif x == 2 :
        print("you have chosen paper : \n" + items[x- 1])
        print("computer hase chosen : \n" + items[AIchoice] )   
    elif x == 3 : 
        print("you have chosen scissors : \n" + items[x- 1])
        print("computer hase chosen : \n" + items[AIchoice] )
else :
    print("invalide choice please try again")
