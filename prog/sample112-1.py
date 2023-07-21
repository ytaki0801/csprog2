from tkinter import Tk, Frame, Label, Button, StringVar

root = Tk()

text = StringVar()
text.set('0')

label = Label(root, textvariable=text) 
label.pack(pady=10)

def bclicked():
    text.set(str(int(text.get())+1))

button = Button(root, text='Click!', command=bclicked)
button.pack(pady=10)

root.mainloop()
