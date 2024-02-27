import tkinter as tk

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get()) # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda char=button_text: button_click(char))
    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", padx=30, pady=10, command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Bind the "=" button to the calculate function
equal_button = tk.Button(root, text="=", padx=20, pady=10, command=calculate)
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
