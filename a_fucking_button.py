import tkinter as tk
from time import sleep

def write_words():
    print('congratulations, you pressed a button.')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def quit1():
    print('so you cant read huh? dumbass.')
    sleep(30)
    exit
    

button = tk.Button(frame, text="fuck off", fg="black",command=quit1)

button.pack(side=tk.LEFT)
var = tk.Button(frame, text="press this button", command = write_words)
var.pack(side=tk.LEFT)
root.mainloop()
