import random
import string
from tkinter import *
import pyperclip

# Initialize the main window
root = Tk()
root.geometry("400x400")
root.title("Random Password Generator")

# Variable to store generated password and length input
output_pass = StringVar()
pass_len = IntVar()

# Password generation function
def randPassGen():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(pass_len.get()))
    output_pass.set(password)

# Copy to clipboard function
def copyPass():
    pyperclip.copy(output_pass.get())

# Layout
Label(root, text='Password Length', font='arial 12 bold').pack(pady=10)
Spinbox(root, from_=4, to_=32, textvariable=pass_len, width=24, font='arial 16').pack()

Button(root, command=randPassGen, text="Generate Password", font="Arial 10", bg='lightblue').pack(pady=20)
Label(root, text='Random Generated Password', font='arial 12 bold').pack(pady="30 10")
Entry(root, textvariable=output_pass, width=24, font='arial 16').pack()
Button(root, text='Copy to Clipboard', command=copyPass, font="Arial 10", bg='lightblue').pack(pady=20)

root.mainloop()
