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

        King('white', ('e', '1'), board=self)
        Bishop('white', ('f', '1'), board=self)
        Knight('white', ('g', '1'), board=self)
        Rook('white', ('h', '1'), board=self)

    def __create_black_pawns(self):
        Pawn('black', ('e', '7'), board=self)
        Pawn('black', ('f', '7'), board=self)
        Pawn('black', ('g', '7'), board=self)
        Pawn('black', ('h', '7'), board=self)

        King('black', ('e', '8'), board=self)
        Bishop('black', ('f', '8'), board=self)
        Knight('black', ('g', '8'), board=self)
        Rook('black', ('h', '8'), board=self)

    def pos_on_board(self, x, y):
        # a1 -> (0, 7), h8 -> (7, 0)
        return (ord('8') - ord(y), ord(x) - ord('a'))  # flip 

    def pos_to_str_tuple(self, pos):
        # (0, 1) -> ('a', '1'), (7, 0) -> ('h', '8')
        x, y = pos
        return (chr(y + ord('a')), chr(ord('8') - x))

    def is_player_pawn(self, color, pawn):
        return pawn in self.pawns[color]  # if pawn is dead it will return false

    def get_player_moves(self, color):
        moves = []
        for pawn in self.pawns[color]:
            moves += pawn.possible_moves()
        return moves

    def in_borders(self, pos):
        return ('a', '1') <= pos <= ('h', '8')

    def __str__(self):
        for i in xrange(8):
            for j in xrange(8):
                print self.board[i][j],
            print
        return ''

    def get_pawn(self, pos):
       if self.in_borders(pos):  # position is correct
        x, y = self.pos_on_board(*pos)
        return self.board[x][y]

    def put_pawn(self, pawn):
        x, y = self.pos_on_board(*pawn.position)
        self.pawns[pawn.color].append(pawn)
        self.board[x][y] = pawn

    def reset_board(self):
        self.__clear_board()
        self.__create_white_pawns()
        self.__create_black_pawns()

    def move_pawn(self, start, end):
        pawn = self.get_pawn(end)
        if pawn is not '.':
            self.pawns[pawn.color].remove(pawn)  # pawn beats other pawn

        pawn = self.get_pawn(start)
        x, y = self.pos_on_board(*end)
        self.board[x][y] = pawn
        x, y = self.pos_on_board(*start)
        self.board[x][y] = '.'
