import customtkinter as ctk
import tkinter as tk
import json
from tkinter import messagebox

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title('To Do List')
window.geometry('500x400')

tasks = [] 


def load_task():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for t in tasks:
                listbox.insert(tk.END, t)
    except FileNotFoundError:
        pass


def save_task():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def add_task():
    new_task = entry.get()

    if new_task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
    else:
        tasks.append(new_task)
        listbox.insert(tk.END, new_task)
        entry.delete(0, tk.END)
        save_task()


def del_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
        save_task()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")


def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()

        if new_task == "":
            messagebox.showwarning("Warning", "Enter new task!")
        else:
            listbox.delete(selected)
            listbox.insert(selected, new_task)
            tasks[selected] = new_task
            entry.delete(0, tk.END)
            save_task()
    except:
        messagebox.showwarning("Warning", "Select a task to update!")


entry = ctk.CTkEntry(window, width=3000, text_color="white", fg_color="pink", justify = "left", font = ("Arial", 24))
entry.pack(pady=10)

ctk.CTkButton(window, text="Add Task", width=15, height=2, fg_color = 'green', command=add_task).pack(pady=5)
ctk.CTkButton(window, text="Delete Task", width=15, height=2, fg_color = 'red', command=del_task).pack(pady=5)
ctk.CTkButton(window, text="Update Task", width=15, height=2, fg_color = 'yellow',command=update_task).pack(pady=5)

listbox = tk.Listbox(window, width=40, height=15, fg="white", bg="black", justify = "left", font = ("Arial", 14))
listbox.pack(pady=10)

load_task()

window.mainloop()