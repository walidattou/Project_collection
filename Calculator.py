import customtkinter as CT


CT.set_appearance_mode("dark")
c = 0
window = CT.CTk()
window.title("Calculator")
window.geometry("300x360")
window.maxsize(300,360)
window.minsize(300,360)

class Calculator():
    def __init__(self):
        pass
   

    def B(arg,px,py,com):
        B = CT.CTkButton(master=window,text=str(arg),corner_radius=0,width=80,command=com)
        B.place(x = px,y = py)
    
    def p():
        Entry.insert(999,string=".")
    def p0():
            Entry.insert(999,string="0")
    def p1():
            Entry.insert(999,string="1")
    def p2():
            Entry.insert(999,string="2")
    def p3():
            Entry.insert(999,string="3")   
    def p4(): 
            Entry.insert(999,string="4") 
    def p5():
            Entry.insert(999,string="5") 
    def p6():
          Entry.insert(999,string="6") 
    def p7():
          Entry.insert(999,string="7") 
    def p8():
          Entry.insert(999,string="8") 
    def p9():
          Entry.insert(999,string="9") 
   
      

    def res():
        user_inpute = Entry.get()
        Entry.delete(0,999)

    
        R = eval(user_inpute)
        
        Entry.insert(999,string=R) 

    def round ():
         user_inpute = Entry.get()
         Entry.delete(0,999)
         R = eval(user_inpute)
         R = round(R)
         Entry.insert(999,string=R) 

    def delete():
        Entry.delete(0,100)
    def iraze():
        C = Entry.get()
        Entry.delete(len(C)-1,100)
    def plus():
        Entry.insert(999,string="+") 

    def Multi():
        Entry.insert(999,string="*")
    def minus():
        Entry.insert(999,string="-")
    def div():
        Entry.insert(999,string="/")
    def pow():
        Entry.insert(999,string="^")
    def Remi():
        Entry.insert(999,string="%")
    
          
        
        

            

            




Entry = CT.CTkEntry(master=window,width=250,height=50,corner_radius=0,font=('Georgia ',20,"bold"))
Entry.place(x=150,y=56,anchor = "c" )



#nums butttons
dot= Calculator.B(".",26,313,Calculator.p)
b0 = Calculator.B(0,110,313,Calculator.p0)
b1 = Calculator.B(1,26,280,Calculator.p1)
b2 = Calculator.B(2,110,280,Calculator.p2)
b3 = Calculator.B(3,194,280,Calculator.p3)
b4 = Calculator.B(4,26,247,Calculator.p4)
b5 = Calculator.B(5,110,247,Calculator.p5)
b6 = Calculator.B(6,194,247,Calculator.p6)
b7 = Calculator.B(7,26,214,Calculator.p7)
b8 = Calculator.B(8,110,214,Calculator.p8)
b9 = Calculator.B(9,194,214,Calculator.p9)
#function buttons
res =Calculator.B("=",194,313,Calculator.res)
Delete = Calculator.B("Delete",194,115,Calculator.delete)
ira = Calculator.B("Iraze",110,115,Calculator.iraze)
Round =Calculator.B("round",26,115,Calculator.round) 

#operations
plus = Calculator.B("+",194,148,Calculator.plus)
mines = Calculator.B("-",110,148,Calculator.minus)
mult=Calculator.B("*",26,148,Calculator.Multi)
div = Calculator.B('/',194,181,Calculator.div)
reminder = Calculator.B("%",110,181,Calculator.Remi)
power = Calculator.B("^",26,181,Calculator.pow)


window.mainloop()
