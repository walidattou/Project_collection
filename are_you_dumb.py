import tkinter
import random

window  = tkinter.Tk()
window.title("ANSWER")
window.minsize(400,300)


Label = tkinter.Label(text="ARE YOU DUMB",fg="black", bg="white",font=("Arial",25))
Label.pack(side="top")



def answer():
    
    x = random.randint(100,700)
    y = random.randint(100,700)
    window.geometry(f"200x100+{x}+{y}")
    
def yes():
    window.destroy()


b = tkinter.Button(text="No",command=answer)
b.pack()

b2 = tkinter.Button(text="YES",command=yes)
b2.pack()

window.mainloop()
