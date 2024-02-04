from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text = "Player " + players[1] + "'s turn", font=('Courier', 36), fg="purple", bg="#bfb8da")

            elif check_winner() is True:
                label.config(text = "Player " + players[0] + " wins", font=('Courier', 36), fg="#ffffff", bg="#bfb8da")

            elif check_winner() == "Tie":
                label.config(text = "Tie!", font=('Courier', 36), fg="purple", bg="#bfb8da")
                
        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text = "Player " + players[0] + "'s turn", font=('Courier', 36), fg="purple", bg="#bfb8da")

            elif check_winner() is True:
                label.config(text = "Player " + players[1] + " wins", font=('Courier', 36), fg="#ffffff", bg="#bfb8da")

            elif check_winner() == "Tie":
                label.config(text = "Tie!", font=('Courier', 36), fg="#a5678e", bg="#bfb8da")


def check_winner():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "" :
            buttons[row][0].config(bg="#bcf5bc")
            buttons[row][1].config(bg="#bcf5bc")
            buttons[row][2].config(bg="#bcf5bc")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "" :
            buttons[0][column].config(bg="#bcf5bc")
            buttons[1][column].config(bg="#bcf5bc")
            buttons[2][column].config(bg="#bcf5bc")
            return True
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "" :
            buttons[0][0].config(bg="#bcf5bc")
            buttons[1][1].config(bg="#bcf5bc")
            buttons[2][2].config(bg="#bcf5bc")
            return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "" :
            buttons[0][2].config(bg="#bcf5bc")
            buttons[1][1].config(bg="#bcf5bc")
            buttons[2][0].config(bg="#bcf5bc")
            return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#FFE4B5")
        return "Tie"

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

    global player

    player = random.choice(players)

    label.config(text = "Player " + player + "'s turn", font=('Courier', 36), bg="#bfb8da", fg="purple") 

    for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="", bg="#F0F0F0")
 

window = Tk()
window.config(bg="#bfb8da")
window.title("Tic-Tac-Toe")
players = ["X","O"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


label = Label(text = "Player " + player + "'s turn", font=('Courier', 36), bg="#bfb8da", fg="purple")

label.pack(side="top")


reset_button = Button(text = "Restart", font=('Courier', 20), bg="#a5678e", fg="#ffffff", command = new_game)
reset_button.place(x=615, y=600)

frame = Frame(window)
frame.place(x=425, y=80)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font=('Courier', 40),
                                      width = 5, height = 2, command = lambda row = row, column = column: next_turn(row,column))

        buttons[row][column].grid(row=row, column=column)


window.mainloop()
