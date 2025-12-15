import tkinter as tk

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Boah")
root.geometry("400x400")

task_listbox = tk.Listbox(root, width=100, height=30)
task_listbox.pack(pady=20)

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="meow")
add_button.pack(pady=5)
add_button.config(command=add_task)
root.mainloop()