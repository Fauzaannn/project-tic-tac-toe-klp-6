from tkinter import *
import random
from tkinter import simpledialog

def get_player_names():
    global players
    players = [
        simpledialog.askstring("Input", "Masukan Nama pemain 1:"),
        simpledialog.askstring("Input", "Masukan nama pemain 2:")
    ]

def next_turn(row, column):
    global player, scores

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == 'X':
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = 'O'
                label.config(text=(players[1] + "(O) Selanjutnya"))

            elif check_winner() is True:
                label.config(text=(players[0] + "(X) Menang"))
                scores[players[0]] += 1
                update_scores()

            elif check_winner() == "Seri":
                label.config(text="Seri")

        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = 'X'
                label.config(text=(players[0] + "(X) Selanjutnya"))

            elif check_winner() is True:
                label.config(text=(players[1] + "(O) Menang "))
                scores[players[1]] += 1
                update_scores()

            elif check_winner() == "Seri":
                label.config(text="Seri")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Seri"
    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player, scores
    player = random.choice(['X', 'O'])
    label.config(text=players[0] + " Selanjutnya")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")
    update_scores()

def update_scores():
    score_label.config(text=f"Scores: {players[0]} - {scores[players[0]]}  {players[1]} - {scores[players[1]]}")


get_player_names()

window = Tk()
window.title("Tic-Tac-Toe")
player = random.choice(['X', 'O'])
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

scores = {players[0]: 0, players[1]: 0}

label = Label(text=players[0] + " Selanjutnya", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Ulang", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

score_label = Label(text=f"Scores: {players[0]} - {scores[players[0]]}  {players[1]} - {scores[players[1]]}",
                    font=('consolas', 20))
score_label.pack(side="top")

window.mainloop()
