from gtts import gTTS
import os
text = open("demo.txt", 'r').read()
language = 'en'
output = gTTS(text =text, lang=language ,slow=False)
output.save('file.mp3')
os.system('start file.mp3')

#for language code search google speech language code 