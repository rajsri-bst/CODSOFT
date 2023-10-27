import random
import string
import tkinter as tk
from tkinter import Entry, Label, Button, Text

def generate_password():
    length = int(length_entry.get())
    username = username_entry.get()
    complexity = 'medium'  # You can adjust this as needed

    if length < 6:
        result_text.config(state="normal")
        result_text.delete(1.0, "end")
        result_text.insert("end", "Password length must be at least 6 characters")
        result_text.config(state="disabled")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Clear the text box and display only the generated password
    result_text.config(state="normal")
    result_text.delete(1.0, "end")
    result_text.insert("end", password)
    result_text.config(state="disabled")

def accept_password():
    generated_password = result_text.get("1.0", "end-1c")
    # Implement what you want to do with the generated password here
    print(f"Accepted Password: {generated_password}")

def reset_form():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    result_text.config(state="normal")
    result_text.delete(1.0, "end")
    result_text.config(state="disabled")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Heading Label (Password Generator)
heading_label = Label(window, text="Password Generator", font=("Helvetica", 14, "bold", "underline"), fg="blue")
heading_label.grid(row=0, column=1, columnspan=2, pady=(10, 0))

# Username Label and Entry (positioned on the right)
username_label = Label(window, text="Username:")
username_label.grid(row=1, column=1)
username_entry = Entry(window)
username_entry.grid(row=1, column=2, pady=10)

# Password Length Label and Entry (positioned on the right)
length_label = Label(window, text="Password Length:")
length_label.grid(row=2, column=1)
length_entry = Entry(window)
length_entry.grid(row=2, column=2, pady=10)

# Label for the result Text Box
result_label = Label(window, text="Generated Password:")
result_label.grid(row=3, column=1, pady=10)

# Result Text Box (positioned to the right of the label)
result_text = Text(window, height=1, width=20)
result_text.grid(row=3, column=2, pady=10)

# Disable text box to prevent user editing
result_text.config(state="disabled")

# Generate Password Button (positioned on the right)
generate_button = Button(window, text="Generate Password", command=generate_password, fg="blue", underline=0)
generate_button.grid(row=4, column=2, pady=(0, 10))

# Accept Button (positioned above the Reset button) in blue
accept_button = Button(window, text="Accept", command=accept_password, fg="blue", pady=10)
accept_button.grid(row=5, column=2, pady=(0, 10))

# Reset Button (positioned on the right) in blue
reset_button = Button(window, text="Reset", command=reset_form, fg="blue", pady=10)
reset_button.grid(row=6, column=2, pady=10)

# Start the GUI event loop
window.mainloop()
