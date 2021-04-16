
from gtts import gTTS
import os


text = "I want to celebrate my birthday"
output = gTTS(text=text, lang='en', slow=False)
output.save('output.mp3')
os.system('start output.mp3')    #for mac start replaced by afplay

