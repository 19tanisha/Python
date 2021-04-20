import tkinter as tk
from compressmodule import compress,decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir = '/', title = 'Select File')
    return filename

def compression(i,o):
    compress(i,o)

window = tk.Tk()

window.title("Compression Window")
window.geometry('600x400')



button1 = tk.Button(window, text = "Compress", command = lambda : compression(open_file(), 'sakshi.txt'))


button1.grid(row = 2, column = 1)

window.mainloop()