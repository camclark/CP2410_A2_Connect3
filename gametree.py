""" gametree.py

Contains the definition of the GameTree class.
This file forms part of the assessment for CP2410 Assignment 2

************** ENTER YOUR NAME HERE ****************************

"""
from connect3board import Connect3Board


class GameTree:
    MAX_PLAYER = 'O'
    MIN_PLAYER = '#'
    MAX_WIN_SCORE = 1
    MIN_WIN_SCORE = -1
    DRAW_SCORE = 0

    # noinspection PyProtectedMember
    class _Node:
        __slots__ = '_gameboard', '_children', '_score'

        def __init__(self, gameboard: Connect3Board):
            self._gameboard = gameboard
            self._children = [None] * self._gameboard.get_columns()

            # for you to complete...

        def _create_children(self):
            token = Connect3Board.TOKENS[Connect3Board._turn_number % 2]

            for col in Connect3Board._cols:
                if Connect3Board._board[0][col] is None:
                    for row in range(Connect3Board._rows - 1, -1, -1):
                        if Connect3Board._board[row][col] is None:
                            Connect3Board._board[row][col] = token
                            Connect3Board._turn_number += 1
                            GameTree._Node._create_children()


            # token = Connect3Board.TOKENS[Connect3Board._turn_number % 2]
            # board = GameTree._Node._gameboard
            # for col in board._cols:
            #     if board[0][col] is None:
            #         for row in range(board._rows - 1, -1, -1):
            #             if board[row][col] is None:
            #                 board[row][col] = token
            #                 Connect3Board._turn_number += 1
            #                 GameTree._Node._create_children()



            # for you to complete...
            pass

        def _compute_score(self):
            # for you to complete...
            pass

    class _Position:
        def __init__(self, node):
            self._node = node

        def get_gameboard(self):
            """ Return the node's gameboard """
            return self._node._gameboard

        def get_child(self, column):
            """ Return a Position object for the column-th child of the node """
            return GameTree._Position(self._node._children[column])

        def get_children_scores(self):
            """ Return a list of the scores for all child nodes """
            return [child._score if child is not None else None for child in self._node._children]

    def __init__(self, root_board):
        self._root = GameTree._Node(root_board)

    def get_root_position(self):
        """ Return a Position object at the root of the game tree """
        return GameTree._Position(self._root)