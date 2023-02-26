import random
from replit import clear

Jack = 10
Queen = 10
King = 10
Ace = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, "King", "Queen", "Jack", 10]
T = 0
game_over = False

card = ""
Dcard = []
Ycard = []
Hide_Dcard = []
dis_Ycard = []
dis_Dcard = []

print("Hello this is black jack")

def finding_special_cards(list):
 global total_Dcard
 global total_Ycard
 if "King" in list :
  n = list.index("King")
  list.pop(n)
  list.insert(n ,10)
 if "Queen" in list:
  n = list.index("Queen")
  list.pop(n)
  list.insert(n ,10)
 if "Jack" in list :
  n = list.index("Jack")
  list.pop(n)
  list.insert(n ,10)
 
   
def Ace(list,total):
 if 11 in list :
  n = list.index(11)
  list.pop(n)
  if total < 21 :
   list.insert(n ,10)
  elif total > 21 :
   list.insert(n ,1)
 else:
  return
  
  

 
def add_card(total,list,llist):
 if total < 17:
  card = random.choice(cards)
  finding_special_cards(list)
  list.append(card)
  llist.append(card)
  print("card add to dealer ")
  
  




def cardsfill(Ycard,Dcard):
 clear()
 

 global card

 for stuff in range(0,2):
  card = random.choice(cards)
  Ycard.append(card)
  dis_Ycard.append(card)



 for i in range(0,2):
  card = random.choice(cards)
  Dcard.append(card)
  Hide_Dcard.append(card)
  dis_Dcard.append(card)

 Hide_Dcard[1] = "*"

 
 print(f"dealer cards : {Hide_Dcard}")
 print(f"your cards : {dis_Ycard}")

 finding_special_cards(Dcard)
 finding_special_cards(Ycard)

 total_Dcard = sum(Dcard)
 total_Ycard = sum(Ycard)

 choice = input("Stand or Hit : ").lower()

 clear()
 

 

 if choice == "stand":
  add_card(total_Dcard,dis_Dcard,Dcard)
  Ace(dis_Dcard,total_Dcard)
  Ace(dis_Ycard,total_Ycard)
  T = sum(Dcard)
  print(f"your cards : {dis_Ycard} / total = {total_Ycard}")
  print(f"dealer cards : {dis_Dcard} / total = {T}")

  if total_Dcard > 21 and total_Ycard > 21:
   print("Draw")

  elif total_Ycard > total_Dcard and total_Ycard <= 21 :
   print("you win")

  elif total_Dcard > total_Ycard and total_Dcard <= 21 :
   print("Dealer win")
  
  elif total_Ycard > total_Dcard and total_Dcard <= 21 :
   print("Dealer win")

  elif total_Dcard == total_Ycard :
   print("Draw")

 
 elif choice == "hit" :
  card = random.choice(cards)
  dis_Ycard.append(card)
  finding_special_cards(dis_Ycard)
  print("card add to you ")
  Ace(dis_Dcard,total_Dcard)
  Ace(dis_Ycard,total_Ycard)
  total_Ycard = sum(dis_Ycard)
  print(f"your cards : {dis_Ycard} / total = {total_Ycard}")
  print(f"dealer cards : {dis_Dcard} / total = {total_Dcard}")

  if total_Dcard > 21 and total_Ycard > 21:
   print("Draw")

  elif total_Ycard > total_Dcard and total_Ycard <= 21 :
   print("you win")

  elif total_Dcard > total_Ycard and total_Dcard <= 21 :
   print("Dealer win")

  elif total_Ycard > total_Dcard and total_Dcard <= 21 :
   print("Dealer win")
   
  elif total_Dcard == total_Ycard :
   print("Draw")
   
 else:
  print("syntacs erorr try again")


cardsfill(Ycard,Dcard)
