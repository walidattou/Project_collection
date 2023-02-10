import random

names = input("what is your names ")
names_list = names.split(" ")

names_count = len(names_list) - 1
chosen_one = random.randint(0,names_count)

print("the person that gonna pay is : " + names_list[chosen_one])
