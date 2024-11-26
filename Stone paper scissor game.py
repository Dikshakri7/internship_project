from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.geometry("400x400")
root.title("Stone, Paper, Scissor Game")
root.configure(bg="#2C3E50")
root.resizable(False, False)

# Variables
choice_list = ["Stone", "Paper", "Scissor"]
player = 0
computer = 0

# Functions
def result():
    global player, computer
    choice = choice_var.get()
    player_choice_label.config(text=choice)
    computer_choice = random.choice(choice_list)
    computer_choice_label.config(text=computer_choice)
    
    if choice == computer_choice:
        result_label.config(text="It's a Tie!", fg="#F39C12")
    elif (choice == "Stone" and computer_choice == "Scissor") or \
         (choice == "Paper" and computer_choice == "Stone") or \
         (choice == "Scissor" and computer_choice == "Paper"):
        result_label.config(text="You Win!", fg="#2ECC71")
        player += 1
    else:
        result_label.config(text="You Lose!", fg="#E74C3C")
        computer += 1
    
    player_score_label.config(text=f"Player: {player}")
    computer_score_label.config(text=f"Computer: {computer}")

def new_game():
    global player, computer
    choice_var.set("")
    player_choice_label.config(text="---")
    computer_choice_label.config(text="---")
    result_label.config(text="", fg="white")
    player = 0
    computer = 0
    player_score_label.config(text="Player: 0")
    computer_score_label.config(text="Computer: 0")

# Header
header = Label(root, text="Stone, Paper, Scissor Game", font=("Arial Bold", 16), bg="#34495E", fg="white")
header.pack(fill=X, pady=10)

# Scoreboard
score_frame = Frame(root, bg="#2C3E50")
score_frame.pack(pady=10)

player_score_label = Label(score_frame, text="Player: 0", font=("Arial", 12), bg="#2C3E50", fg="white")
player_score_label.grid(row=0, column=0, padx=20)

computer_score_label = Label(score_frame, text="Computer: 0", font=("Arial", 12), bg="#2C3E50", fg="white")
computer_score_label.grid(row=0, column=1, padx=20)

# Choice Section
choice_frame = LabelFrame(root, text="Make Your Choice", font=("Arial", 12), bg="#34495E", fg="white", bd=2, relief="groove")
choice_frame.pack(pady=10, fill=X, padx=20)

choice_var = StringVar()

stone_button = ttk.Radiobutton(choice_frame, text="Stone", value="Stone", command=result, variable=choice_var)
stone_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = ttk.Radiobutton(choice_frame, text="Paper", value="Paper", command=result, variable=choice_var)
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissor_button = ttk.Radiobutton(choice_frame, text="Scissor", value="Scissor", command=result, variable=choice_var)
scissor_button.grid(row=0, column=2, padx=10, pady=5)

# Choices Display
choices_display_frame = Frame(root, bg="#2C3E50")
choices_display_frame.pack(pady=10)

Label(choices_display_frame, text="Player's Choice:", font=("Arial", 12), bg="#2C3E50", fg="white").grid(row=0, column=0, padx=10)
player_choice_label = Label(choices_display_frame, text="---", font=("Arial", 12, "bold"), bg="#2C3E50", fg="#3498DB")
player_choice_label.grid(row=0, column=1, padx=10)

Label(choices_display_frame, text="Computer's Choice:", font=("Arial", 12), bg="#2C3E50", fg="white").grid(row=1, column=0, padx=10)
computer_choice_label = Label(choices_display_frame, text="---", font=("Arial", 12, "bold"), bg="#2C3E50", fg="#E74C3C")
computer_choice_label.grid(row=1, column=1, padx=10)

# Result Section
result_label = Label(root, text="", font=("Arial Bold", 14), bg="#2C3E50", fg="white")
result_label.pack(pady=10)

# Buttons
button_frame = Frame(root, bg="#2C3E50")
button_frame.pack(pady=20)

newgame_button = ttk.Button(button_frame, text="New Game", command=new_game)
newgame_button.grid(row=0, column=0, padx=10)

exit_button = ttk.Button(button_frame, text="Exit", command=root.quit)
exit_button.grid(row=0, column=1, padx=10)

root.mainloop()
