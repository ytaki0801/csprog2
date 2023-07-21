from tkinter import Tk, Frame, Label, Button, StringVar

class App(Tk):
    def __init__(self):
        super().__init__()

        self.__text = StringVar()
        self.__text.set('0')

        self.__label = Label(self, textvariable=self.__text)
        self.__label.pack(pady=10)

        self.__button = Button(self, text='Click!')
        self.__button.bind('<ButtonPress>', self.incNum)
        self.__button.pack(pady=10)

    def incNum(self, e):
        self.__text.set(str(int(self.__text.get())+1))

root = App()

root.mainloop()
