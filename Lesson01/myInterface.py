import tkinter as tk
import tkinter.messagebox

window = tk.Tk()

window.title("My first GUI APP")

window.geometry('300x300')

# https://coolors.co/palettes/trending
label = tk.Label(window, text="Class", bg='#ffc8dd', fg='#5FC')
label.pack()

entry = tk.Entry(window, width=20)
entry.pack()

def clickme():
    tkinter.messagebox.showinfo(title="提示", message="好痛")

button = tk.Button(window, text="Yes", command=clickme)
button.pack()

window.mainloop()
