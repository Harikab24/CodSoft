import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring  # Correct import for simpledialog

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(root)
        self.tasks_listbox.pack(padx=10, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            removed_task = self.tasks.pop(task_index)
            self.tasks_listbox.delete(task_index)
            messagebox.showinfo("Task Removed", f"Task '{removed_task}' removed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def edit_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            current_task = self.tasks[task_index]

            new_task = askstring("Edit Task", f"Edit task '{current_task}':")
            if new_task:
                self.tasks[task_index] = new_task
                self.tasks_listbox.delete(task_index)
                self.tasks_listbox.insert(task_index, new_task)
        else:
            messagebox.showwarning("Warning", "Please select a task to edit.")

def main():
    root = tk.Tk()
    todo_app = ToDoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
