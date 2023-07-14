from tkinter import Tk, Frame, Label, Button, Canvas
from tkinter import PhotoImage
from tkinter import W, Entry, StringVar, LEFT

# ===== root window =====

root = Tk()
root.title('How to use tkinter')
root.geometry('500x500')

# ===== 5 frames =====

frame = [None] * 5

frame[0] = Frame(root, width=250, height=100, borderwidth=2, relief='solid')
frame[1] = Frame(root, width=250, height=100, borderwidth=2, relief='solid')
frame[2] = Frame(root, width=500, height=200, borderwidth=2, relief='solid')
frame[3] = Frame(root, width=250, height=200, borderwidth=2, relief='solid')
frame[4] = Frame(root, width=250, height=200, borderwidth=2, relief='solid')

for i in range(5): frame[i].propagate(False)

frame[0].grid(row=0, column=0)
frame[1].grid(row=0, column=1)
frame[2].grid(row=1, column=0, columnspan=2)
frame[3].grid(row=2, column=0)
frame[4].grid(row=2, column=1)

# ===== 2 labels in frame[0] =====

f0label = [None] * 2

f0label[0] = Label(frame[0], text='String', font=('', 14), fg='white', bg='red')
f0label[0].pack(padx=5, pady=10)

f0label[1] = Label(frame[0], text='Left Alignment', font=('System', 14))
f0label[1].pack(anchor=W)

# ===== button in frame[1] =====

def click_f1button1(): f1button1['text'] = 'Clicked'
f1button1 = Button(frame[1], text='Change Button Name', command=click_f1button1)
f1button1.pack(padx=5, pady=10)

# ===== entry, button and label in frame[1] =====

f1entry = Entry(frame[1], width=14)
text = StringVar()
def click_f1entry(): text.set(f1entry.get())

f1button2 = Button(frame[1], text='Copy String', command=click_f1entry)
f1label = Label(frame[1], textvariable=text, font=('System', 14))

f1entry.pack(side=LEFT)
f1button2.pack(side=LEFT)
f1label.pack(side=LEFT)

# ===== PhotoImage in frame[2] =====

image=PhotoImage(file='./python_logo.png')
f2label = Label(frame[2], image=image)
f2label.pack(pady=20)

# ===== Canvas in frame[3] =====

f3canvas = Canvas(frame[3], width=250, height=200)
f3canvas.pack()

# ===== buttons in frame[4] to draw and delete in frame[3] =====

def click_draw(): f3canvas.create_rectangle(10, 10, 140, 140, tag='rect')
f4button1 = Button(frame[4], text='Draw', width=15, command=click_draw)
f4button1.pack(padx=5, pady=10)

def click_delete(): f3canvas.delete('rect')
f4button2 = Button(frame[4], text='Delete', width=15, command=click_delete)
f4button2.pack(padx=5, pady=10)

root.mainloop()

