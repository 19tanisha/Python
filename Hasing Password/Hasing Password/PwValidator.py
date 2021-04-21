from tkinter import *
import bcrypt

def Validate(password):
    hash = b'$2b$12$2tHyGe5vUtzBh0KJft9EF.dsX4HqBYYp8nwxPu817NRkfFAzjwU0S'
    password = bytes(password, encoding = 'utf-8')
    if bcrypt.checkpw(password, hash):
        print('Login Successful')
    else:
        print('Invalid Password')


root = Tk()
root.geometry('300x300')

entry1 = Entry(root)
entry1.pack()

button1 = Button(root, text = 'Validate', command = lambda:Validate(entry1.get()))
button1.pack()




root.mainloop()