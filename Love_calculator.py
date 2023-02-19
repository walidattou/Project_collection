his_name = input("whats his name : ").lower()
her_name = input("whats her name : ").lower()

love_his_name = his_name.count("l") + his_name.count("o") + his_name.count("v")+his_name.count("e")
true_his_name = his_name.count("e")+his_name.count("t")+his_name.count("r")+his_name.count("u")

love_her_name = his_name.count("l") + his_name.count("o") + his_name.count("v")+his_name.count("e")
true_her_name = his_name.count("e")+his_name.count("t")+his_name.count("r")+his_name.count("u")

p_love = love_his_name + love_her_name
p_true = true_his_name + true_her_name
concat = (f"{p_love}{p_true}")
int_concat = int(concat)

if int_concat < 10 or int_concat > 90 :
    print(f"your score is {int_concat}% , you go toghether like cooky")
elif int_concat < 40 and int_concat > 50 :
    print(f"your score is {int_concat}% , you are all right")
else :
    print(f"your score is {int_concat}% , you should break up at this point")    

