import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create a GUI window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget for adding tasks
task_entry = tk.Entry(root, font=("Helvetica", 16))
task_entry.pack(pady=10)

# Create buttons to add, remove, and clear tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack()

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, font=("Helvetica", 16), selectmode=tk.SINGLE)
task_listbox.pack()

root.mainloop()
