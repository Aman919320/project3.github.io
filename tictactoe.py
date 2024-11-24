import tkinter as tk
from tkinter import messagebox

def check_winner():
    for row in board:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
            highlight_winner(row)
            return True
    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != "":
            highlight_winner([board[i][col] for i in range(3)])
            return True
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        highlight_winner([board[i][i] for i in range(3)])
        return True
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        highlight_winner([board[i][2-i] for i in range(3)])
        return True
    return False

def highlight_winner(buttons):
    for button in buttons:
        button.config(bg="lightgreen")
    global game_active
    game_active = False

def is_draw():
    for row in board:
        for button in row:
            if button['text'] == "":
                return False
    return True

def button_click(row, col):
    global turn
    if game_active and board[row][col]['text'] == "":
        board[row][col]['text'] = turn
        if check_winner():
            messagebox.showinfo("Game Over", f"{turn} wins!")
            return
        if is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            return
        turn = "O" if turn == "X" else "X"
        status_label.config(text=f"{turn}'s Turn")

def reset_game():
    global turn, game_active
    turn = "X"
    game_active = True
    for row in board:
        for button in row:
            button.config(text="", bg="SystemButtonFace")
    status_label.config(text="X's Turn")

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game variables
turn = "X"
game_active = True
board = []

# Status label
status_label = tk.Label(root, text="X's Turn", font=("Helvetica", 16))
status_label.pack(pady=10)

# Game board
frame = tk.Frame(root)
frame.pack()
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(frame, text="", font=("Helvetica", 20), width=5, height=2,
                           command=lambda r=i, c=j: button_click(r, c))
        button.grid(row=i, column=j)
        row.append(button)
    board.append(row)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), command=reset_game)
reset_button.pack(pady=10)

# Run the application
root.mainloop()
