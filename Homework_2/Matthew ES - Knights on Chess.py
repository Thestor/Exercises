# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:14:06 2019

@author: Matthew
"""
import string

alphabet = list(string.ascii_uppercase)
size_of_board = eval(input("Size of the board (a number, max 26): "))
position_of_knight = input("The current position of the knight: ")

def create_board(size):
    board = []
    for number in range(size):
        temp_list = []
        for number2 in range(size):
            temp_list.append("-")
        board.append(temp_list)
    return board

def determine_moves(board, position):
    
    for a in alphabet:
        if position[0] == a:
            indexed_position = alphabet.index(a)
    if len(position) >= 3:
        number_position = eval(position[1] + position[2]) - 1
    else:
        number_position = eval(position[1]) - 1
    board[number_position][indexed_position] = "O"
    
    possible_moves = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, -2], [1, 2], [-1, -2], [-1, 2]]
    for x, y in possible_moves:
        
        if indexed_position + x < 0 or number_position + y < 0 or indexed_position + x > len(board) - 1 or number_position + y > len(board) - 1:
            pass
        else:
            board[number_position + y][indexed_position + x] = "+"
    
    board.reverse()
    return board
        

theboard1 = create_board(size_of_board)
theboard2 = determine_moves(theboard1, position_of_knight)

for row in theboard2:
    print(" ".join(map(str, row)))
    
