from replit import clear


print("hello this is a secret oction")

oct_dic = {}

not_other_ppl = False

def user_data(name,price):
 oct_dic[name] = price

while not_other_ppl == False :
 name = input("whats your name : ")
 price = input("whats is your price : ")
 user_data(name,price)
 choice = input("is there other ppl ?")
 if choice == "yes" :
  clear()
  user_data(name,price)
  
 else:
  y = max(oct_dic.values())
  x = oct_dic.keys()
  u = x[y.index(max(y))]
  print(f"{x} with {u}$")
  not_other_ppl == True
  print(oct_dic)
  break
