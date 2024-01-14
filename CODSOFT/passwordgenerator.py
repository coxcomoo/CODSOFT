import random
import tkinter as tk

def passwordgeneration(length, e):
    password = ""
    characters = '0123456789abcdefghjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_?<>~`:;,.'
    for i in range(length):
        password += random.choice(characters)
    e.delete(0, tk.END)  
    e.insert(0, password)  

def main():
    root = tk.Tk()
    root.title("Random Password Generator")
    label = tk.Label(root, text="Enter the desired length of the password: ")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entry_password = tk.Entry(root)
    entry_password.pack()
    button = tk.Button(root, text="Generate Password", command=lambda: passwordgeneration(int(entry.get()), entry_password))
    button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
