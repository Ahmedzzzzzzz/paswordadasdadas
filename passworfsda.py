import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)
    if length == 0:
        result.config(text="Enter a password")
    elif length < 5:
        result.config(text="Weak")
    elif length < 10:
        result.config(text="Medium")
    else:
        result.config(text="Strong")

root = tk.Tk()
root.title("Password Strength")

label = tk.Label(root, text="Enter Password:")
label.pack()

entry = tk.Entry(root, show="*")
entry.pack()

btn = tk.Button(root, text="Check Strength", command=check_strength)
btn.pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()
