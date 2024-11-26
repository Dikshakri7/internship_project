from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.geometry("400x300")
root.title("Password Generator")
root.config(bg="#1E2A38")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TLabel", background="#1E2A38", foreground="white", font=("Arial", 12))

# Functions
def generate():
    characters = [
        'r', ')', 'l', 'S', 'y', '*', 'e', 'q', '3', 'W', '@', 'N', '1', 'P', 'H', '6', 
        'A', '7', 'm', 'i', 'g', 'C', 'J', '$', '%', 'Z', 'x', 'p', 'd', '9', 'B', 'U', 
        'j', 'b', 'R', 'V', 'h', 't', 'D', 'K', '2', '0', 'T', 'M', 'x', 's', 'F', 'v', 
        '4', '&', 'Q', 'f', 'G', 'X', 'L', '#', '5', 'E', 'c', 'Y', 'O', 'w', 'n', '!', 
        'u', 'o', 'k', '(', 'a', 'I', '8'
    ]
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError
        password = ''.join(random.choices(characters, k=length))
        password_label.config(text=password, fg="#58D68D")
    except ValueError:
        password_label.config(text="Invalid length", fg="#E74C3C")

def copy():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))
    root.update()  # Keeps clipboard updated
    copy_status_label.config(text="Password copied!", fg="#58D68D")

# Header
header_label = Label(root, text="Password Generator", font=("Arial Bold", 16), bg="#1E2A38", fg="#F5B041")
header_label.pack(pady=20)

# Input Frame
input_frame = Frame(root, bg="#1E2A38")
input_frame.pack(pady=10)

length_label = Label(input_frame, text="Enter Password Length:", font=("Arial", 12))
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_length = ttk.Entry(input_frame, font=("Arial", 10), width=15)
entry_length.grid(row=0, column=1, padx=10, pady=5)

# Button Frame
button_frame = Frame(root, bg="#1E2A38")
button_frame.pack(pady=10)

generate_button = ttk.Button(button_frame, text="Generate Password", command=generate, width=20)
generate_button.grid(row=0, column=0, padx=10)

copy_button = ttk.Button(button_frame, text="Copy Password", command=copy, width=20)
copy_button.grid(row=0, column=1, padx=10)

# Output Frame
output_frame = Frame(root, bg="#1E2A38")
output_frame.pack(pady=10)

password_text_label = Label(output_frame, text="Generated Password:", font=("Arial", 12))
password_text_label.grid(row=0, column=0, padx=10, pady=5)

password_label = Label(output_frame, text="", font=("Arial", 12, "bold"), fg="white", bg="#1E2A38")
password_label.grid(row=0, column=1, padx=10, pady=5)

copy_status_label = Label(output_frame, text="", font=("Arial", 10), bg="#1E2A38", fg="white")
copy_status_label.grid(row=1, column=0, columnspan=2, pady=5)

root.mainloop()
