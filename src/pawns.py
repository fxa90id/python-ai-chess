class Pawn(object):
    _me = 'p'
    def __init__(self, color, position, board):
        self.color = color
        self.position = position
        self.board = board
        self.board.put_pawn(self)

    def __str__(self):
        return u"%s" % (self._me.upper() if self.color is 'white' else self._me)

class King(Pawn):
    _me = 'a'
    pass

class Bishop(Pawn):
    _me = 'b'
    pass

class Knight(Pawn):
    _me = 'k'
    pass

class Rook(Pawn):
    _me = 'r'
    pass
