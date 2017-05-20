""" gametree.py

Contains the definition of the GameTree class.
This file forms part of the assessment for CP2410 Assignment 2

************** Cameron Clark ****************************

"""
from connect3board import Connect3Board


class GameTree:
    MAX_PLAYER = 'O'
    MIN_PLAYER = '#'
    MAX_WIN_SCORE = 1
    MIN_WIN_SCORE = -1
    DRAW_SCORE = 0

    class _Node:
        __slots__ = '_gameboard', '_children', '_score', '_depth_limit'
        # depth limit in slots?

        def __init__(self, gameboard: Connect3Board):
            self._gameboard = gameboard
            self._children = [None] * self._gameboard.get_columns()
            # Where to put check for depth limit?
            self._depth_limit = self._gameboard.get_columns() * self._gameboard.get_rows()

            if self._gameboard.get_winner() is None:
                self._create_children()
            elif self._gameboard.get_winner() == gameboard.DRAW:
                self._score = GameTree.DRAW_SCORE
            elif self._gameboard.get_winner() == GameTree.MAX_PLAYER:
                self._score = GameTree.MAX_WIN_SCORE
            elif self._gameboard.get_winner() == GameTree.MIN_WIN_SCORE:
                self._score = GameTree.MIN_WIN_SCORE

            # if self._score is None:
            #     self._compute_score()
            if self._children is not None:
                self._compute_score()

        def _create_children(self):
            """ ALL GOOD """
            print(self._gameboard._cols)
            # changed line
            # for col in self._gameboard._cols:
            for col in range(self._gameboard._cols - 1):
                board_copy = self._gameboard.make_copy()

                if self._gameboard.can_add_token_to_column(col):
                    board_copy.add_token(col)
                    self._children[col] = GameTree._Node(board_copy)
                    print("AM I EVEN RUNNING?")

        def _compute_score(self):
            # if it's O turn
            #   find the maximum score of the children and return it's score
            # if it's X turn
            #   find the minimum score of the children and return it's score
            if self._gameboard.get_whose_turn() == GameTree.MAX_PLAYER:
                max_score = -2
                for child in self._children:
                    if child._score > max_score:
                        max_score = child.score
                self._score = max_score

            else:
                min_score = 2
                print(self._children, "whewwwwww")
                for child in self._children:
                    print(child, "HERE I AMMMMMM")
                    if child._score < min_score:
                        min_score = child.score
                self._score = min_score

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