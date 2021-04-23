from tkinter import *
from credit import Card_Validity

def Validation(n):
    if len(n) == 16:
        Card_Validity(n)
    else:
        print('Error')


root = Tk()
root.title('Card Validator')
root.geometry('600x600')
label1 = Label(root, text = 'Card Number')
label1.grid(row = 0 , column = 0)

n = Entry(root)
n.grid(row = 0, column = 1)

button1 = Button(root, text = 'Validate', command = lambda : Validation(n.get()))
button1.grid(row = 2, column = 1)

root.mainloop()