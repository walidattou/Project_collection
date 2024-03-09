import customtkinter as tkinter
from PIL import ImageTk, Image
import math
from pygame import mixer

bprsed = False
r = None
T = False
Paustext = None


mixer.init()
#ui
tkinter.set_appearance_mode("dark")
window = tkinter.CTk()
window.geometry("1024x640")
window.maxsize(1024,640)
window.minsize(1024,640)
window.title("Pomodoro Timer")



Canvas = tkinter.CTkCanvas(width=1024,height=1024)
mytext = Canvas.create_text(510,300,text="00:00",font=("Helvetica",100,"bold"),fill="black")
Paustext = Canvas.create_text(510,160,text="Study time",font=("Helvetica",100,"bold"),fill="green")
sound = mixer.Sound("X2Download.app - SHY Martin _ One Hour _ Feelings (128 kbps).mp3")
sound.set_volume(0.1)
sound.play()
alarm = mixer.Sound("X2Download.app - Alarm Sound Effect (128 kbps).mp3")
def rest():

    window.after_cancel(r)
    Canvas.itemconfig(mytext,text = f"00:00")
    

def timer(S=10):
    global r
    Canvas.itemconfig(Paustext,text = "Study time")
    min = math.floor(S / 60)
    sec = round(S%60)
    Canvas.itemconfig(mytext,text = f"{min}:{sec}")
    if S > 0 :
        r = window.after(1000,timer,S-1)
    elif S == 0 :
        alarm.play()
        pause()
        
def pause(S=300):
    min = math.floor(S / 60)
    sec = round(S%60)
    Canvas.itemconfig(Paustext,text = "Rest time")
    Canvas.itemconfig(mytext,text = f"{min}:{sec}")
    if S > 0 :
        r = window.after(1000,pause,S-1)
    elif S == 0 :
        alarm.play()
        timer()



    
        

rrb = tkinter.CTkButton(master=window,font=("DOCKTRIN",30),text="Start Timer",height=20,width=50,bg_color="black",border_color="black",fg_color="black",command=timer)
rrb.place(x=430,y=400)

rrrb = tkinter.CTkButton(master=window,font=("DOCKTRIN",30),text="Stop Timer",height=20,width=50,bg_color="black",border_color="black",fg_color="black",command=rest)
rrrb.place(x=440,y=460)

music_button = tkinter.CTkButton(master=window,font=("DOCKTRIN",30),text="Mute Music",height=20,width=50,bg_color="black",border_color="black",fg_color="black",command=sound.stop)
music_button.place(x=760,y=550)


Canvas.pack()



window.mainloop()
