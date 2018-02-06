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
    """ Get from ints between specified number, includes prompts """
    while True:
        try:
            num = int(input(prompt))
            if low <= num <= high:
                return num
            else:
                print("Value must be between {} and {} inclusive: ".format(low, high))
        except ValueError:
            print("Value must be between {} and {} inclusive: ".format(low, high))


def run_two_player_mode():
    """ Runs two player Connect three on variable length board """
    MIN_ROWS = 3
    MAX_ROWS = 7
    MIN_COLS = 3
    MAX_COLS = 7

    rows = get_int_between("Please select number of rows (Min: {}  Max: {}): ".format(MIN_ROWS, MAX_ROWS), MIN_ROWS,
                           MAX_ROWS)
    cols = get_int_between("Please select number of columns (Min: {}  Max: {}): ".format(MIN_COLS, MAX_COLS), MIN_COLS,
                           MAX_COLS)

    game = Connect3Board(rows, cols)
    print(game)

    while game.get_winner() is None:
        move = get_int_between("Player {}'s turn. Choose column (0 to {})".format(game.get_whose_turn(), cols - 1), 0,
                               cols - 1)

        if game.can_add_token_to_column(move) is True:
            game.add_token(move)
            print(game)
        else:
            print("That column is not available. Please choose again.")

    if game.get_winner() == Connect3Board.DRAW:
        print("This game has ended in a draw!")
    else:
        print("Player {} wins!".format(game.get_winner()))


def run_ai_mode():
    """ Run Connect 3 against AI on a 3x3 board """
    player = piece_selection()

    rows = 3
    cols = 3

    game = Connect3Board(rows, cols)
    print(game)

    game_tree = GameTree(game)
    position = game_tree.get_root_position()

    while game.get_winner() is None:
        if game.get_whose_turn() == player:
            move = get_int_between("Your turn. Choose column (0 to {}): ".format(cols - 1), 0, cols - 1)

            if game.can_add_token_to_column(move) is True:
                game.add_token(move)
                position = position.get_child(move)
                print(game)
            else:
                print("ERROR: Invalid move, please try again")
        else:
            children_scores = position.get_children_scores()
            child_index = None
            max_score = -2
            min_score = 2

            for i, child in enumerate(children_scores):
                if game.get_whose_turn() == game.TOKENS[0]:
                    if child is not None and child > max_score:
                        max_score = child
                        child_index = i
                else:
                    if child is not None and child < min_score:
                        min_score = child
                        child_index = i

            game.add_token(child_index)
            position = position.get_child(child_index)

            print("AI's turn")
            print(game)

    if game.get_winner() == Connect3Board.DRAW:
        print("This game has ended in a draw!")
    else:
        print("Player {} wins!".format(game.get_winner()))


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


if __name__ == '__main__':
    main()
