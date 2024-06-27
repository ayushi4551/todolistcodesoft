import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # GUI Elements
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame,
            width=50,
            height=10,
            bd=0,
            selectbackground="#a6a6a6"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, font=("Helvetica", 24), width=26)
        self.entry.pack(pady=20)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        self.add_task_button = tk.Button(
            self.button_frame,
            text="Add Task",
            command=self.add_task
        )
        self.add_task_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.delete_task_button = tk.Button(
            self.button_frame,
            text="Delete Task",
            command=self.delete_task
        )
        self.delete_task_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.load_tasks()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.tasks.pop(task_index)
            self.update_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)
        self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                self.tasks = [task.strip() for task in tasks]
                self.update_tasks()
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
