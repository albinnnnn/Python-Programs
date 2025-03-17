import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by 0 is not possible."
    else:
        return x / y

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
tk.Label(root, text="First Number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

operations_frame = tk.Frame(root)
operations_frame.grid(row=2, column=0, columnspan=2)

add_button = tk.Button(operations_frame, text="+", command=lambda: calculate('Add'))
add_button.grid(row=0, column=0)

subtract_button = tk.Button(operations_frame, text="-", command=lambda: calculate('Subtract'))
subtract_button.grid(row=0, column=1)

multiply_button = tk.Button(operations_frame, text="x", command=lambda: calculate('Multiply'))
multiply_button.grid(row=0, column=2)

divide_button = tk.Button(operations_frame, text="/", command=lambda: calculate('Divide'))
divide_button.grid(row=0, column=3)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
