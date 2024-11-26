from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.geometry("400x450")
root.resizable(False, False)
root.config(bg="#1C2833")

# Styling
style = ttk.Style()
style.configure("TLabel", background="#1C2833", foreground="white", font=("Arial", 12))
style.configure("TRadiobutton", background="#1C2833", foreground="white", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10), padding=5)

def calculate():
    operator = choice_val.get()
    try:
        a = float(first_entry.get())
        b = float(second_entry.get())
        result.config(state="normal")
        result.delete(0, END)
        if operator == "+":
            result.insert(0, a + b)
        elif operator == "-":
            result.insert(0, a - b)
        elif operator == "*":
            result.insert(0, a * b)
        elif operator == "/":
            if b == 0:
                result.insert(0, "Cannot divide by 0")
            else:
                result.insert(0, a / b)
        result.config(state="readonly")
    except ValueError:
        result.config(state="normal")
        result.delete(0, END)
        result.insert(0, "Invalid input")
        result.config(state="readonly")

def clear():
    result.config(state="normal")
    result.delete(0, END)
    first_entry.delete(0, END)
    second_entry.delete(0, END)
    result.config(state="readonly")

# Header
header = Label(root, text="Calculator", font=("Arial Bold", 16), bg="#1C2833", fg="#F5B041")
header.pack(pady=20)

# Input Section
input_frame = Frame(root, bg="#1C2833")
input_frame.pack(pady=10)

first_number_label = ttk.Label(input_frame, text="First Number:")
first_number_label.grid(row=0, column=0, padx=10, pady=10)
first_entry = ttk.Entry(input_frame, font=("Arial", 10), width=20)
first_entry.grid(row=0, column=1, padx=10, pady=10)

second_number_label = ttk.Label(input_frame, text="Second Number:")
second_number_label.grid(row=1, column=0, padx=10, pady=10)
second_entry = ttk.Entry(input_frame, font=("Arial", 10), width=20)
second_entry.grid(row=1, column=1, padx=10, pady=10)

result_label = ttk.Label(input_frame, text="Result:")
result_label.grid(row=2, column=0, padx=10, pady=10)
result = ttk.Entry(input_frame, state="readonly", font=("Arial", 10), width=20)
result.grid(row=2, column=1, padx=10, pady=10)

# Operations Section
operation_frame = LabelFrame(root, bg="#34495E", fg="white", text="Operations", font=("Arial Bold", 12), padx=10, pady=10)
operation_frame.pack(pady=20)

choice_val = StringVar()

add_btn = ttk.Radiobutton(operation_frame, text="Add (+)", value="+", variable=choice_val)
add_btn.grid(row=0, column=0, padx=10, pady=5)
sub_btn = ttk.Radiobutton(operation_frame, text="Subtract (-)", value="-", variable=choice_val)
sub_btn.grid(row=0, column=1, padx=10, pady=5)
mul_btn = ttk.Radiobutton(operation_frame, text="Multiply (x)", value="*", variable=choice_val)
mul_btn.grid(row=1, column=0, padx=10, pady=5)
div_btn = ttk.Radiobutton(operation_frame, text="Divide (/)", value="/", variable=choice_val)
div_btn.grid(row=1, column=1, padx=10, pady=5)

# Action Buttons
button_frame = Frame(root, bg="#1C2833")
button_frame.pack(pady=20)

calculate_btn = ttk.Button(button_frame, text="Calculate", command=calculate, width=15)
calculate_btn.grid(row=0, column=0, padx=15, pady=10)
clear_btn = ttk.Button(button_frame, text="Clear", command=clear, width=15)
clear_btn.grid(row=0, column=1, padx=15, pady=10)

root.mainloop()
