import tkinter as tk
import random
import string

def generate_password():
    length = int(length_var.get())
    if length < 6:
        password_result.set("Password should be at least 6 characters long.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_result.set(password)

# Create a GUI window
root = tk.Tk()
root.title("Password Generator")

# Create a label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()

# Create a button to generate a password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Create a label to display the generated password
password_result = tk.StringVar()
password_label = tk.Label(root, textvariable=password_result)
password_label.pack()

root.mainloop()
