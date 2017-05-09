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