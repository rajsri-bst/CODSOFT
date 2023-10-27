import tkinter as tk
import math

# Function to update the display when a button is clicked
def button_click(number):
    if number == 'c':
        display.delete(0, tk.END)  # Clear the display
    else:
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current + str(number))

# Function to perform the calculation and update the display
def calculate():
    current = display.get()
    try:
        if '√' in current:
            operand = float(current.split('√')[1])
            result = math.sqrt(operand)
        elif '!' in current:
            operand = int(current.split('!')[0])
            result = math.factorial(operand)
        else:
            result = eval(current)
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for the display
display = tk.Entry(root, width=20)
display.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    'c', '√', '/', '<-',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '!', '0', '.', '='
]

# Create and place the calculator buttons
row = 1
col = 0
for button_text in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20, command=lambda t=button_text: button_click(t) if t != '=' else calculate()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()


