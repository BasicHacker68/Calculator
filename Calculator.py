import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set the background color to a dark color (e.g., dark gray)
root.configure(bg="#333333")

# Create an entry widget for input with a dark background
entry = tk.Entry(root, width=30, bg="#444444", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Define and create number buttons on the left side
number_buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('.', 4, 0)  # Swapped positions for '0' and '.'
]

for (text, row, col) in number_buttons:
    button = tk.Button(root, text=text, padx=10, pady=10, command=lambda t=text: button_click(t), bg="#555555", fg="white")
    button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

# Define and create operator buttons on the right side
operator_buttons = [
    ('/', 1, 3), ('*', 2, 3), ('-', 3, 3), ('+', 4, 3),
    ('C', 4, 0), ('=', 4, 2)  # Removed 'Off' and adjusted '=' position
]

for (text, row, col) in operator_buttons:
    button = tk.Button(root, text=text, padx=10, pady=10, command=lambda t=text: button_click(t) if t != 'C' else clear(), bg="#555555", fg="white")
    if text == '=':
        button.config(command=evaluate)  # Set the '=' button to call evaluate function
    button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

# Make the entry widget expand when the window is resized
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Start the main loop
root.mainloop()
