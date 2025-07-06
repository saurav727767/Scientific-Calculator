import tkinter as tk
import math

def press(symbol):
    entry.insert(tk.END, str(symbol))

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        expression = entry.get().replace("^", "**")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_scientific(func):
    try:
        expression = entry.get()
        if not expression:
            entry.insert(tk.END, "Error")
            return

        value = float(eval(expression))

        if func == "sqrt":
            result = math.sqrt(value)
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        elif func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        else:
            result = "Error"

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def insert_pi():
    press(str(math.pi))

# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief='sunken', justify='right')
entry.grid(row=0, column=0, columnspan=5, pady=20)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('log', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('ln', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('π', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^', 5, 3), ('C', 5, 4),
]

for (text, row, col) in buttons:
    if text in ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt']:
        cmd = lambda x=text: calculate_scientific(x)
    elif text == 'π':
        cmd = insert_pi
    elif text == 'C':
        cmd = clear
    elif text == '=':
        cmd = equal
    elif text == '^':
        cmd = lambda: press("^")
    else:
        cmd = lambda x=text: press(x)

    tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 12),
              command=cmd).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
