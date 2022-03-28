# Program name : connect 4 game
# last modification date : 3/5/2022
# Alialdin muhammad mostafa hanafy
from sys import exit
from os import system, name
import sys

def clear():
    if name == 'nt':
        _ =system('cls')
    else:
        _ = system('clear')

matrix = [[' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',]]


def print_matrix():
    print()
    print("  1    2    3    4    5    6    7")
    for i in range(0,6):
        print (matrix[i])

def check_and_drop(column, piece):
    sum = 0
    for i in range(6):#counting the empty cells
        if matrix [i][column - 1] != ' ':
            sum += 1
    if sum == 6:
        return False

    matrix [ 5 - sum] [column - 1] = piece #adding piece in the empty cell
    return True

def take_input(player): #taking the input from the player
    while True:
        players_column = input(f"\nPlease player {player} enter column (from 1 to 7 inclusive): ")
        if players_column in ['1' , '2', '3', '4', '5' , '6' ,'7']:
            if player == 1:
                x_or_o = 'x'
            else:
                x_or_o = 'o'
            valid = check_and_drop(int(players_column),x_or_o)
            if not valid:
                print("\n+The column you entered is full.")
            else:
                break
        else:
            print("Please enter a valid input.")

def winner_checker():
    for col in range(0,7): # cheking all coloumns for a vertical winner
        for row in range(0,3):#checking the first three rows
            list =[]
            if matrix[row][col]==' ':
                continue

            list.append(matrix[row][col])
            for elements in range(1,4): 
                list.append(matrix[row+elements][col])
            result = all(element == list[0] for element in list) # check if all elements are the same
            if not result:
                continue
            else:
                return True
    for row in range(0,6): # cheking all rows for a horizontal winner
        for col in range(0,4):#checking the first 4 cloloumns
            list =[]
            if matrix[row][col]==' ':
                continue

            list.append(matrix[row][col])
            for elements in range(1,4): 
                list.append(matrix[row][col+elements])
            result = all(element == list[0] for element in list) # check if all elements are the same
            if not result:
                continue
            else:
                return True

    
    for col in range(0,4): #checking the first 4 coloumns for ascending diagonal
        for row in range(3,6):##checking the last 3 rows for ascending diagona
            list =[]
            if matrix[row][col]==' ':
                continue
            list.append(matrix[row][col])
            for elements in range(1,4): # adding 4 ascending diagonal elemnts in a list and then comparing them
                list.append(matrix[row-elements][col+elements])

            result = all(element == list[0] for element in list) # check if all elements are the same
            if not result:
                continue
            else:
                return True
    
    for col in range(0,4): # checking the first 4 columns for descending diagonal
        for row in range(0,3):# checking the first 3 rows
            list =[]
            if matrix[row][col]==' ':
                continue

            list.append(matrix[row][col])
            for elements in range(1,4): # adding 4 ascending diagonal elemnts in a list and then comparing them
                list.append(matrix[row+elements][col+elements])
            result = all(element == list[0] for element in list) # check if all elements in the list are equal
            if not result:
                continue
            else:
                return True

def draw(): #if there is no winner
    sum = 0
    for col in range(0,7):
        for row in range(0,6):
            if matrix[row][col]==' ':
                continue
            else:
                sum = sum+1
    if sum==42:
        print("draw")
        exit()


def game_on():#checking weather the player wants to play again
    global matrix
    while True:
        decision=input("do you want to play again\n if yes type'y' if no type'n': ")
        if decision in ['y','n']:
            if decision =='y':
                matrix = [[' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',],
        [' ',' ',' ',' ',' ',' ',' ',]]
                return True
            else:
                exit()
        else:
            print("invalid input: only type'y' or 'n'")
            continue
             




print_matrix()#displaying the board for the first time
while True: 
    take_input(1)
    clear()
    print_matrix()
    if winner_checker():
        print_matrix()
        print("player 1 won")
        if game_on():
            print_matrix()
            continue
        
    take_input(2)
    clear()
    if winner_checker():
        print_matrix()
        print("player 2 won")
        if game_on():
            print_matrix()
            continue

    print_matrix()
    if draw():
         if game_on():
            print_matrix()
            continue






   

    