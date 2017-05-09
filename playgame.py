""" playgame.py

Contains the Connect 3 game playing application.
This file forms part of the assessment for CP2410 Assignment 2

************** ENTER YOUR NAME HERE ****************************

"""
from connect3board import Connect3Board
from gametree import GameTree


def main():
    print('Welcome to Connect 3 by Cameron Clark')
    mode = get_mode()
    while mode != 'Q':
        if mode == 'A':
            run_two_player_mode()
        elif mode == 'B':
            run_ai_mode()
        mode = get_mode()


def get_int_between(prompt, low, high):
    while True:
        try:
            num = int(input(prompt))
            if low <= num <= high:
                return num
            else:
                print("Value must be between {} and {} inclusive".format(low, high))
        except ValueError:
            pass


def run_two_player_mode():

    cols = get_int_between("Please select number of columns (Min: 3  Max:7)", 3, 7)
    rows = get_int_between("Please select number of rows (Min: 3  Max:7)", 3, 7)

    game = Connect3Board(cols, rows)
    print(game)

    while game.get_winner() is None:
        move = get_int_between("Player {} please enter a column to drop a piece".format(game.get_whose_turn()), 0, cols - 1)

        # print(game._board[0][0])

        if game.can_add_token_to_column(move) is True:
            game.add_token(move)
            print(game)
        else:
            print("ERROR: Invalid move for {}, please try again".format(game.get_whose_turn()))

    print("++++++++-------------------------------------------------------------++++++++")
    print("pizza party for {},  you win". format(game.get_winner()))
    print("++++++++-------------------------------------------------------------++++++++")
    # pass


def run_ai_mode():
    # for you to complete...
    pass


def get_mode():
    mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    while mode[0].upper() not in 'ABQ':
        mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    return mode[0].upper()


def get_int(prompt):
    result = 0
    finished = False
    while not finished:
        try:
            result = int(input(prompt))
            finished = True
        except ValueError:
            print("Please enter a valid integer.")
    return result


if __name__ == '__main__':
    main()
