from tkinter import *
from gtts import gTTS
import os
def TextToSpeech():
    a= entry.get()
    output = gTTS(text=a, lang='en',slow = False)
    output.save('input.mp3')
    os.system('start input.mp3')
root = Tk()
canvas = Canvas(root, height =300, width = 400)
canvas.pack()
entry = Entry(canvas)
canvas.create_window(200 , 180 , window = entry)

button = Button(text = "text", command = TextToSpeech)
canvas.create_window(200 ,220 , window = button)

root.mainloop()