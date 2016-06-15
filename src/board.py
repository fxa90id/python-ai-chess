import pdb, copy
from pawns import Pawn, King, Bishop, Knight, Rook

class Board(object):
    def __init__(self):
        self.pawns = {'white': [], 'black': []}
        self.__clear_board()

    def __clear_board(self):
        self.board = [['.' for _ in xrange(8)] for _ in xrange(8)]

    def __create_white_pawns(self):
        Pawn('white', ('e', '2'), board=self)
        Pawn('white', ('f', '2'), board=self)
        Pawn('white', ('g', '2'), board=self)
        Pawn('white', ('h', '2'), board=self)

        self.white_king = King('white', ('e', '1'), board=self)
        Bishop('white', ('f', '1'), board=self)
        Knight('white', ('g', '1'), board=self)
        Rook('white', ('h', '1'), board=self)

    def __create_black_pawns(self):
        Pawn('black', ('e', '7'), board=self)
        Pawn('black', ('f', '7'), board=self)
        Pawn('black', ('g', '7'), board=self)
        Pawn('black', ('h', '7'), board=self)

        self.black_king = King('black', ('e', '8'), board=self)
        Bishop('black', ('f', '8'), board=self)
        Knight('black', ('g', '8'), board=self)
        Rook('black', ('h', '8'), board=self)

    def pos_on_board(self, pos):
        # a1 -> (0, 7), h8 -> (7, 0)
        x, y = pos
        return (ord('8') - ord(y), ord(x) - ord('a'))  # flip 

    def pos_to_str_tuple(self, pos):
        # (0, 1) -> ('a', '1'), (7, 0) -> ('h', '8')
        x, y = pos[:2]
        return (chr(y + ord('a')), chr(ord('8') - x))

    def is_player_pawn(self, color, pawn):
        return pawn in self.pawns[color]  # if pawn is dead it will return false

    def get_player_moves(self, color, king_safe=True):
        moves = []
        for pawn in self.pawns[color]:
            moves += pawn.possible_moves(king_safe)
        return moves

    def in_borders(self, pos):
        x, y = pos
        return 'a' <= x <= 'h' and '1' <= y <= '8'

    def __str__(self):
        print "    A B C D E F G H"
        print "  -------------------"
        for i in xrange(8):
            print "%d |" % (8-i), 
            for j in xrange(8):
                print self.board[i][j],
            print "| %d" % (8-i)
        print "  -------------------"
        print "    A B C D E F G H"
        return ''

    def get_pawn(self, pos):
        x, y = self.pos_on_board(pos)
        if self.in_borders(pos):  # position is correct
            return self.board[x][y]
        else:
            raise IndexError("wrong position: %d %d", x, y)

    def put_pawn(self, pawn):
        x, y = self.pos_on_board(pawn.position)
        self.pawns[pawn.color].append(pawn)
        self.board[x][y] = pawn

    def reset_board(self):
        self.__clear_board()
        self.__create_white_pawns()
        self.__create_black_pawns()

    def move_pawn(self, start, end):
        start, end = tuple(start), tuple(end)
        pawn = self.get_pawn(end)

        try:
            if pawn is not '.':
                self.old_pawn = pawn
                self.pawns[pawn.color].remove(pawn)  # pawn beats other pawn
            else:
                self.old_pawn = '.'
        except:
            print pawn, pawn.color

        pawn = self.get_pawn(start)
        x, y = self.pos_on_board(end)
        self.board[x][y] = pawn
        pawn.position = end
        x, y = self.pos_on_board(start)
        self.board[x][y] = '.'

    def undo_move_pawn(self, start, end):
        start, end = tuple(start), tuple(end)
        pawn = self.get_pawn(end)
        x, y = self.pos_on_board(end)
        self.board[x][y] = self.old_pawn
        x, y = self.pos_on_board(start)
        self.board[x][y] = pawn
        pawn.position = start


    def king_safe_after(self, start, end, king, color):
        self.move_pawn(start, end)
        moves = self.get_player_moves(color, king_safe=False)
        self.undo_move_pawn(start, end)
        p_moves = [tuple(move[2:]) for move in moves] # get only end positions
        print "krol", king, "ruchy przeciwnika:", p_moves
        return not (king in p_moves)

    def check_mate(self):
        kings = 0
        for color in self.pawns:
            for pawn in self.pawns[color]:
                if isinstance(pawn, King):
                    kings += 1
        return kings is 2


