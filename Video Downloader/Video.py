from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

def get_path():
    path = filedialog.askdirectory()
    label3.config(text = path)


def download():
    video_path = entry1.get()
    file_path = label3.cget('text')
    print('Downloading....')
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    #mp3
    audio_clip = video_clip.audio
    audio_clip.write_audiofile('audio.mp3')
    audio_clip.close()
    shutil.move('audio.mp3', file_path )
    #mp3
    video_clip.close()
    shutil.move(mp4, file_path)
    print('Download Completed')



root = Tk()
root.title("Video downloader")

canvas = Canvas(root, height = 400, width = 400)
canvas.pack()

label1 = Label(root, text = 'Video Downloader', fg ='blue', font = ('bold', 30))
canvas.create_window(200, 100, window = label1)

label2 = Label(root, text = 'Enter URL')
canvas.create_window(200, 150, window = label2)

entry1 = Entry(root)
canvas.create_window(200, 170, window = entry1)

label3 = Label(root, text = 'Select Location')
canvas.create_window(200, 210, window = label3)

button1 = Button(root, text = 'Select', command = get_path)
canvas.create_window(200, 230, window = button1)

button2 = Button(root, text = 'Download', command = download)
canvas.create_window(200, 300, window = button2)

root.mainloop()