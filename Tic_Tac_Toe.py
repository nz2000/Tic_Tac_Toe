'''
Author: Noel Zacharia
Objective: Recreation of the popular game TicTacToe
'''

import sys

#Setting up the base of the game i.e. the game matrix
game = [[0,0,0],[0,0,0],[0,0,0]]

def game_board(player,row,column):
    
    if player != 0:
        game[row][column]=player
    print("   a  b  c")
    for count,row in enumerate(game):
        print(count,row)
    play(game)
    
#determines the present status of the game to see if anyone has won
def play(game_map):

#horizontal checker:

    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"congrats player{row[0]},you have won")
            sys.exit()

#vertical checker:

    for col in range(len(game)):
        checker = []
        for row in game:
            checker.append(row[col])
        if checker.count(checker[0]) == len(checker) and checker[0] != 0:
            print(f"congrats player{checker[0]},you have won")
            sys.exit()

#diagonal checker:
          
    diag = []
    for diagonal in range(len(game)):
        diag.append(game[diagonal][diagonal])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
            print(f"congrats player{diag[0]},you have won")
            sys.exit()
            
    dia = []
    for check,diagon in enumerate(reversed(range(len(game)))):
        dia.append(game[check][diagon])
    if dia.count(dia[0]) == len(dia) and dia[0] != 0:
            print(f"congrats player{dia[0]},you have won")
            sys.exit()

game_board(0,0,0) 

#Registers input values to determine playing conditions
while True:
    players = int(input("plz input your player number:"))
    rows = int(input("which row?"))
    columns = int(input("which columns?"))
    game_board(players,rows,columns)