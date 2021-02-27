"""
Password manager

create UI
    website, email/username, password entry fields
    generate random password button
        copy password to clipboard
    add button
        check if all fields are filled in
        write to data file
"""


from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [str(num) for num in range(10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# generate password
def randomPassGenerator():
    numLetters = random.randint(8, 11)
    numNumbers = random.randint(2, 4)
    numSymbols = random.randint(2, 4)

    passwordLetters = [random.choice(letters) for _ in range(numLetters)]
    passwordNums = [random.choice(numbers) for _ in range(numNumbers)]
    passwordSymbols = [random.choice(symbols) for _ in range(numSymbols)]

    passwordChars = passwordLetters + passwordNums + passwordSymbols

    random.shuffle(passwordChars)

    password = "".join(passwordChars)

    passwordEntry.insert(0, password)
    pyperclip.copy(password)


# save password to .txt file
def save():
    if len(websiteEntry.get()) > 0 and len(passwordEntry.get()) > 0 and len(emailUserEntry.get()) > 0:
        isOK = messagebox.askokcancel(title=websiteEntry.get(),
                                      message=f"These are the details entered: \nEmail: {emailUserEntry.get()}\n"
                                              f"Password: {passwordEntry.get()}")
        if isOK:
            with open("data.txt", "a") as data:
                data.write(f"{websiteEntry.get()} | {emailUserEntry.get()} | {passwordEntry.get()}\n")
                websiteEntry.delete(0, END)
                passwordEntry.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Some fields are incomplete.")


# create UI
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lockPhoto = PhotoImage(file="logo.gif")
canvas.create_image(150, 100, image=lockPhoto)
canvas.grid(column=1, row=0)

websiteLabel = Label(text="Website:")
websiteLabel.grid(column=0, row=1)

websiteEntry = Entry(width=35)
websiteEntry.grid(column=1, row=1, columnspan=2)

emailUserLabel = Label(text="Email/Username:")
emailUserLabel.grid(column=0, row=2)

emailUserEntry = Entry(width=35)
emailUserEntry.grid(column=1, row=2, columnspan=2)
emailUserEntry.insert(0, "yourmostcommonemail@email.com")

passwordLabel = Label(text="Password:")
passwordLabel.grid(column=0, row=3)

passwordEntry = Entry(width=20)
passwordEntry.grid(column=1, row=3)

generatePassword = Button(text="Generate Password", command=randomPassGenerator)
generatePassword.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
