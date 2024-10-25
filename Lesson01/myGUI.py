import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("My First GUI Program")
window.geometry("300x300")

label = tk.Label(window, text="hello world")
label.pack()

entry = tk.Entry(window, width=20)
entry.pack()

def clickme():
    tkinter.messagebox.showinfo("Message", "You clicked me!")

button = tk.Button(window, text="Click me!", command=clickme)
button.pack()

window.mainloop()
