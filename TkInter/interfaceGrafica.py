from tkinter import *

def intGrafica():

    window = Tk()

    window.title("Meu programa")

    entry_text = Entry(window, width = 30)
    entry_text.pack()
    entry_text.focus_set()

    def click_button():
        print(entry_text.get())

    btn = Button(window, text='Clique aqui', width=20, command=click_button)
    btn.pack()

    window.geometry('300x150')
    window.mainloop()
