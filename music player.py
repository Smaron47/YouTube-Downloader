'''import playsound 
from tkinter import *

playsound.playsound("obosthan.mp4")


window=Tk()
window.title("SPlayer")
window.geometry("400x400")



from pytube import YouTube
youtube_link = 'https://www.youtube.com/watch?v=RCO1NWm3_eI'
y = YouTube(youtube_link)
t = y.streams.filter(only_audio=True,file_extension="mp3").all()
t.download()
from pytube import YouTube
import os
from playsound import playsound


playsound(new_file)


'''



from tkinter import *
#from PIL import Image, ImageTk
import requests
import os 
import pygame
#import youtube_dl
import requests
from pytube import YouTube
from threading import * 
pygame.init()


window = Tk()
window.geometry("400x400")
#set size permanently   #or you can use window.resizabld(false, false)
window.minsize(500, 500)
#window.maxsize(500, 500)
window.title("Smaron")

#window.iconbitmap("E:\\downloads\\icon.ico")

lbal=Listbox(window,  
                  bg = "white",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "black",
                  height=14)

lbal.grid(row=1,column=1, padx=0,pady=80)
playlist=[]
k=0
for i in os.listdir('/home/smaron/Desktop/songs'):
    if i.endswith(".mp3"):
        playlist.append(i)
        lbal.insert(k, i)
        
        k=k+1
#-----list----
def update():
    k=0
    for i in os.listdir('/home/smaron/Desktop/songs'):
        if i.endswith(".mp3"):
            playlist.append(i)
            lbal.insert(k, i)
            print(k,i)
            k=k+1
    label1 = Label(window, text = 5*"\t"+"\n"*3, fg = "gray", wraplength=300,font = ("new times roman",  16, "bold"))
    label1.place(x = 200, y = 100)
    label1 = Label(window, text = " Updated", fg = "gray", wraplength=300,font = ("new times roman",  26, "bold"), bg="black")
    label1.place(x = 200, y = 100)
#-----list----

                
             


def playall():
    pygame.mixer.init()
    s=lbal.curselection()[0]

    for file in os.listdir("/home/smaron/Desktop/songs"):
        if file.endswith('.mp3'):
            print("Playing file:", playlist[s])
            pygame.mixer_music.load(f'/home/smaron/Desktop/songs/{playlist[s]}')
            pygame.mixer_music.play()
            lbal.selection_set(s)
            # Wait for the music to play before exiting 
            while pygame.mixer.music.get_busy():   
                pygame.time.Clock().tick(5)
            

#---------------------------------------------------------------------------------------------------------------
    #first get the picture then save it in pic and set as background



def play_music():
    
    global b
    b = lbal.curselection()[0]
    global n
    n=lbal.curselection()[0]
    print(b,n)
    global paused
    t=len(playlist)
    
    if paused:
        pygame.mixer_music.unpause()
        paused = FALSE
    else:
        stop_music()
        pygame.mixer_music.load(f'/home/smaron/Desktop/songs/{playlist[b]}' )
        print(playlist[b])
        pygame.mixer_music.play()
        
        
    button1 = Button(window, text = "Pause ", fg = "black", bg = "white", relief = "raised", font = ("arial", 10, "bold"), command = pause_music)
    button1.place(x = 305, y = 250)
    label1 = Label(window, text = playlist[b], fg = "gray", wraplength=300,font = ("new times roman",  16, "bold"), bg="black")
    label1.place(x = 200, y = 100)

def stop_music():
    pygame.mixer_music.stop()
    lbal.selection_clear(0,END)


paused = FALSE


def pause_music():
    global n
    n=lbal.curselection()[0]
    global paused
    paused = TRUE
    pygame.mixer_music.pause()
    button1 = Button(window, text = "  Play  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 10, "bold"), command = play_music)
    button1.place(x = 305, y = 250)


"""NEED THIS"""
def nxt():
    global b
    b += 1
    #pygame.mixer.pre_init(44100,-16,2, 1024)
    pygame.init()
    pygame.mixer_music.load(f'/home/smaron/Desktop/songs/{playlist[b]}' )
    pygame.mixer_music.play()
    lbal.selection_set(b)
    label1 = Label(window, text = 5*"\t"+"\n"*3, fg = "gray", wraplength=300,font = ("new times roman",  16, "bold"))
    label1.place(x = 200, y = 100)
    label1 = Label(window, text = playlist[b], fg = "gray", wraplength=300,font = ("new times roman",  16, "bold"), bg="black")
    label1.place(x = 200, y = 100)
def prev():
    global b 
    b -= 1
    #pygame.mixer.pre_init(44100,-16,2, 1024)
    pygame.init()
    pygame.mixer_music.load(f'/home/smaron/Desktop/songs/{playlist[b]}' )
    print(playlist[b])
    pygame.mixer_music.play()
    label1 = Label(window, text = playlist[b], fg = "gray", wraplength=300,font = ("new times roman",  16, "bold"), bg="black")
    label1.place(x = 200, y = 100)

def dwn( ):
   label2 = Label(window, text = "Name :", font = ("arial", 16, "bold"))
   label2.place(x = 20, y = 450)
   link = StringVar()
   textBox1 = Entry(window, text="hi", textvar = link, width = 30, font = ("arial", 16, "bold"))
   textBox1.place(x = 120, y = 450)
   def mp3():
      s=link.get()
      s.replace('play','')
      s.replace(' ','+')
      r=requests.get(f"https://www.youtube.com/results?search_query={s}").text
      k=r.find('watch?v=')         
      yt = YouTube(f'https://www.youtube.com/{r[k:k+19]}')
      video = yt.streams.filter(only_audio=True).first()
      downloaded_file = video.download("/home/smaron/Desktop/songs/")
      new_file = s + '.mp3'
      os.rename(downloaded_file, new_file)
      label1 = Label(window, text = "   Download Done\nClick UPdate for add                                                   ", fg = "gray", wraplength=300,font = ("new times roman",  16, "bold"), bg="black")
      label1.place(x = 200, y = 100)
      labl=Label(text=6*'\t'+'\n'*6,font = ("arial", 16, "bold"))
      labl.place(x=20,y=390)
   def mp():
      s=link.get()
      s.replace('play','')
      s.replace(' ','+')
      r=requests.get(f"https://www.youtube.com/results?search_query={s}").text
      k=r.find('watch?v=')         
      yt = YouTube(f'https://www.youtube.com/{r[k:k+19]}')
      video = yt.streams.filter().first()
      video.download("/home/smaron/Desktop/songs")
      label1 = Label(window, text = "                            Download Done\nClick UPdate for add                                                   ", fg = "gray", wraplength=300,font = ("new times roman",  16, "bold"), bg="black")
      label1.place(x = 200, y = 100)
      labl=Label(text=6*'\t'+'\n'*6,font = ("arial", 16, "bold"))
      labl.place(x=135,y=390)
   button2 = Button(window, text = "   MP3   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = mp3)
   button1 = Button(window, text = "   MP4   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = mp)
   button2.place(x = 150, y = 400)
   button1.place(x = 250, y = 400)


def  volup():
    vol=pygame.mixer_music.get_volume()
    pygame.mixer_music.set_volume(vol+0.2)
    print(pygame.mixer_music.get_volume())
def  voldown():
    vol=pygame.mixer_music.get_volume()
    pygame.mixer_music.set_volume(vol-0.2)
    print(pygame.mixer_music.get_volume())

def exit():
    window.destroy()
label1 = Label(window, text = "Smaron Player", fg = "gray", font = ("new times roman",  36, "bold"), bg="black")
label1.place(x = 70, y = 0)

#---- but-----
button2 = Button(window, text = "   Download  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = dwn)
button2.place(x = 180, y = 350)




button1 = Button(window, text = "  Previus  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 10, "bold"), command = prev)
button1.place(x = 200, y = 250)
button3 = Button(window, text = "  Play ", fg = "black", bg = "white", relief = "raised", font = ("arial", 10, "bold"), command = play_music)
button3.place(x = 305, y = 250)
button4 = Button(window, text = "  Next  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 10, "bold"), command = nxt)
button4.place(x = 395, y = 250)
button5 = Button(window, text = "  Volume Up  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 10, "bold"), command = volup)
button5.place(x = 200, y = 300)
button6 = Button(window, text = "Volume Down", fg = "black", bg = "white", relief = "raised", font = ("arial", 10, "bold"), command = voldown)
button6.place(x = 370, y = 300)
button3 = Button(window, text = "  Stop ", fg = "black", bg = "white", relief = "raised", font = ("arial", 10, "bold"), command = stop_music)
button3.place(x = 305, y = 300)



button1 = Button(window, text = "   Play all   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = playall)
button1.place(x = 0, y = 350)

button1 = Button(window, text = "  Update  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = update)
button1.place(x = 350, y = 350)
button1 = Button(window, text = "  X  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = exit)
button1.place(x = 0, y = 400)
#display window

window.mainloop()
