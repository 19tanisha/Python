#pip install pypng
#pip install pyqrcode
#pip install pillow


import pyqrcode
from tkinter import *
from PIL import ImageTk, Image  


def generate():
   link_name = linkname_entry.get()
   link = url_entry.get()
   file_name = link_name+".png"
   url = pyqrcode.create(link)
   url.png(file_name, scale = 8)
   image = ImageTk.PhotoImage(Image.open(file_name))
   img_label = Label(image=image)
   img_label.image = image
   canvas.create_window(200, 300, window = img_label)


root = Tk()

canvas = Canvas(root, height = 600, width = 400)
canvas.pack()

qr_name = Label(root, text = "QR Code Generator", fg = "red", font = ('Arial', 30))
canvas.create_window(200, 50, window = qr_name)

link_name = Label(root , text = "Link name" ,fg = "blue")
canvas.create_window(200, 100, window = link_name)

url_name = Label(root , text = "Link URL", fg = "blue")
canvas.create_window(200, 160, window = url_name)

linkname_entry = Entry(root)
canvas.create_window(200, 120, window = linkname_entry)

url_entry = Entry(root)
canvas.create_window(200, 180, window = url_entry)

button_gen = Button(root, text = "Generate QR code", command=generate)
canvas.create_window(200, 220, window = button_gen)




root.mainloop()