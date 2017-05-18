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

    # noinspection PyProtectedMember
    class _Node:
        __slots__ = '_gameboard', '_children', '_score', '_depth_limit'
        # depth limit in slots

        def __init__(self, gameboard: Connect3Board):
            self._gameboard = gameboard
            self._children = [None] * self._gameboard.get_columns()
            # Where to put check for depth limit?
            self._depth_limit = self._gameboard.get_columns() * self._gameboard.get_rows()

            if self._gameboard.get_winner() is None:
                # is this right?
                GameTree._Node._children = GameTree._Node._children._create_children()
            elif self._gameboard.get_winner() == gameboard.DRAW:
                self._score = GameTree.DRAW_SCORE
            elif self._gameboard.get_winner() == GameTree.MAX_PLAYER:
                self._score = GameTree.MAX_WIN_SCORE
            elif self._gameboard.get_winner() == GameTree.MIN_WIN_SCORE:
                self._score = GameTree.MIN_WIN_SCORE

        def _create_children(self):
            # use if can add to column
            #   if cannot move to next
            for col in self._gameboard._cols:
                # below: from modified function: "can_add_token_to_column(self, column)"
                if 0 <= col < self._gameboard._cols and self._gameboard._board[0][col] is None:
                    # below: from modified function "add_token(self, column)"
                    assert 0 <= col < self._gameboard._cols
                    token = self._gameboard.TOKENS[self._gameboard._turn_number % 2]
                    if self._gameboard._board[0][col] is None:
                        for row in range(self._gameboard._rows - 1, -1, -1):
                            if self._gameboard._board[row][col] is None:
                                self._gameboard._board[row][col] = token
                                self._gameboard._turn_number =+ 1

                                # Is this how I init a new child?
                                self._children[col] = GameTree._Node

            pass

        def _compute_score(self):
            """ Return the score of a node"""
            return self._score

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