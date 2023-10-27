import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("To-Do List Application")

# Create a label for the title in green
title_label = tk.Label(app, text="To-Do List", font=("Helvetica", 20), fg="green")
title_label.pack(pady=10)

# Create a frame to hold the text entry and submit button
entry_frame = tk.Frame(app)
entry_frame.pack()

# Create a text entry field for tasks
task_entry = tk.Entry(entry_frame, width=30)
task_entry.pack(side=tk.LEFT)

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Create a "Submit" button in the same row as the text entry
submit_button = tk.Button(entry_frame, text="Submit", width=10, command=add_task)
submit_button.pack(side=tk.LEFT, padx=5)

# Create a listbox to display tasks
task_list = tk.Listbox(app, height=10, width=30)
task_list.pack()

# Function to remove a selected task from the list
def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        pass

# Function to edit a selected task in the list
def edit_task():
    try:
        selected_task = task_list.curselection()[0]
        edited_task = task_entry.get()
        task_list.delete(selected_task)
        task_list.insert(selected_task, edited_task)
    except IndexError:
        pass

# Create buttons to add, remove, and edit tasks
edit_button = tk.Button(app, text="Edit Task", width=10, command=edit_task)
delete_button = tk.Button(app, text="Delete Task", width=10, command=remove_task)

edit_button.pack(side=tk.LEFT, padx=5)
delete_button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter main loop
app.mainloop()
