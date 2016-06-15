#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, time, random, pdb
from board import Board


class ChessAI(object):
    def __init__(self, filename):
        self.file = filename
        self.my_color = 'black'
        self.opponent_color = 'white'
        self.current_color = 'white'
        self.last_move = None
        self.board = Board()

    def readMove(self):
        try:
            with open(self.file, 'r') as f:
                content = f.readlines()
                return content[-1].strip()  # read last move
        except Exception as e:
            print "plik jest pusty lub nie istnieje"
            self.my_color = 'white'
            self.opponent_color = 'black'
            open(self.file, 'a').close()
            return None

    def writeMove(self, start, end):
        with open(self.file, 'a') as f:
            move = "{start}{end}\n".format(start=start, end=end)
            f.write(move)
            return move

    def play(self):
        self.board.reset_board()
        # pdb.set_trace()
        move = self.readMove()
        while self.board.check_mate():
            print self.board
            if self.my_color is self.current_color:
                # my move
                moves = self.board.get_player_moves(self.my_color)
                if moves:
                    random_move = random.randint(0, len(moves) - 1)
                    move = moves[random_move]
                    print "wykonuje ruch:", move
                    start, end = move[:2], move[2:]
                    self.board.move_pawn(start, end)
                    self.writeMove(start, end)
                    self.current_color = self.opponent_color
                    self.last_move = move
                else:
                    print "SZACH MAT"
            else:
                move = self.readMove()
                # wait for opponent
                tries = 0
                while self.last_move == move:
                    time.sleep(1)
                    if tries is 5:
                        break
                    tries+=1
                if not self.last_move == move:
                    self.last_move = move
                    start, end = move[:2], move[2:]
                    self.board.move_pawn(start, end)
                    self.current_color = self.my_color

if __name__ == "__main__":
    cai = ChessAI('szachy.txt')
    cai.play()
