from tkinter import *
import random

window  = Tk()
window.title("KM to ML")
window.minsize(210,150)
window.maxsize(210,150)

Label = Label(text="Freedom unite converter",fg="black",font=("Arial",10))
Label.pack(side="top")
def Convert():
    miles.delete("1.0", "end")
    KILO =kl.get()
    KILO = int(KILO)
    KILO *= 0.62
    miles.insert(INSERT,"%.2f" % KILO)




kl = Entry(bd=5,width=13)
kl.place(x=66,y=40)

km_text = Text(bd=5,width=3,height=1)
km_text.place(x=20,y=40)
km_text.insert(INSERT,"KM")
km_text.config(state='disabled')

miles=Text(bd=5,width=10,height=1)
miles.place(x=66,y=80)

mil_text = Text(bd=5,width=3,height=1)
mil_text.place(x=20,y=80)
mil_text.insert(INSERT,"MIL")
mil_text.config(state='disabled')



b2 = Button(text="Convert",command=Convert,bd=4)
b2.place(x=80,y=110)



window.mainloop()
