""" playgame.py

Contains the Connect 3 game playing application.
This file forms part of the assessment for CP2410 Assignment 2

************** Cameron Clark ****************************

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
        move = get_int_between("Player {}'s turn. Choose column (0 to {})".format(game.get_whose_turn(), cols - 1), 0, cols - 1)

        if game.can_add_token_to_column(move) is True:
            game.add_token(move)
            print(game)
        else:
            print("That column is not available. Please choose again.")

    if game.get_winner() == Connect3Board.DRAW:
        print("This game has ended in a draw!")
    else:
        print("Player {} wins!". format(game.get_winner()))


def run_ai_mode():
    player = piece_selection()

    cols = 3
    rows = 3
    game = Connect3Board(cols, rows)
    print(game)

    while game.get_winner() is None:
        token = game.TOKENS[game._turn_number % 2]
        if token == player:
            #player moves
            move = get_int_between("Your turn. Choose column (0 to 2): ", 0, cols - 1)

            if game.can_add_token_to_column(move) is True:
                game.add_token(move)
                print(game)
            else:
                print("ERROR: Invalid move, please try again")
        # else:
        #     #AI moves
        #     #TODO: Add AI
        #     # print("beep boop :(")

    if game.get_winner() == Connect3Board.DRAW:
        print("This game has ended in a draw!")
    else:
        print("Player {} wins!". format(game.get_winner()))

def get_mode():
    mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    while mode[0].upper() not in 'ABQ':
        mode = input("A. Two-player mode\nB. Play against AI\nQ. Quit\n>>> ")
    return mode[0].upper()


def piece_selection():
    result = None
    finished = False
    while not finished:
        result = input("Will you play as O or #? ").upper()
        if result == "O" or result == "#":
            finished = True
        else:
            print("ERROR: Please enter O or #")
    return result


# def get_int(prompt):
#     result = 0
#     finished = False
#     while not finished:
#         try:
#             result = int(input(prompt))
#             finished = True
#         except ValueError:
#             print("Please enter a valid integer.")
#     return result


if __name__ == '__main__':
    main()
