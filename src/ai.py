#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, time


class ChessGame(object):
    def __init__(self, filename):
        self.file = filename

    def readMove(self):
        with open(self.file, 'r') as f:
            content = f.readlines()
            return content[-1]

    def writeMove(self, start, end):
        with open(self.file, 'a') as f:
            move = "{start}{end}\n".format(start=start, end=end)
            f.write(move)
            return move


class Board(object):
    def __init__(self):
        self.board = []


class Pawn(object):
    def __init__(self, start_position):
        self.position = start_position  # (0, 0) -> (a, 1)

    def move(self, end):
        pass

    def possible_moves(self):
        """ returns list of possible moves """
        pass

class Knight(Pawn):
    pass

class King(Pawn):
    pass

class Bishop(Pawn):
    pass

class Rook(Pawn):
    pass



if __name__ == '__main__':
    ge = ChessGame('szachy.txt')

