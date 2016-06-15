class Pawn(object):
    _me = 'p'
    def __init__(self, color, position, board):
        self.color = color
        self.position = position
        self.board = board
        self.board.put_pawn(self)
        if self.color is 'white':
            self._me = self._me.upper()
            self.direction = 1
        else:
            self.direction = -1

    def __str__(self):
        return u"%s" % (self._me)


    def possible_moves(self, king_safe=True):
        moves = []
        x, y = self.position
        pos = (chr(ord(x)), chr(ord(y) + self.direction))
        l_pos = (chr(ord(x) - 1), chr(ord(y) + self.direction))
        r_pos = (chr(ord(x) + 1), chr(ord(y) + self.direction))
        try:
            pawn = self.board.get_pawn(pos)
            if pawn is '.':
                line = ''.join(self.position) + ''.join(pos)
                if self.king_ok(line, king_safe):
                    moves.append(line)
        except IndexError:
            pass
        try:
            pawn = self.board.get_pawn(l_pos)
            print "l_pos found:", pawn
            if not (pawn is '.') and pawn.color is not self.color:
                line = ''.join(self.position) + ''.join(l_pos)
                if self.king_ok(line, king_safe):
                    moves = [line] + moves
        except IndexError:
            pass
        try:
            pawn = self.board.get_pawn(r_pos)
            print "r_pos found:", pawn
            if not (pawn is '.') and pawn.color is not self.color:
                line = ''.join(self.position) + ''.join(l_pos)
                if self.king_ok(line, king_safe):
                    moves = [line] + moves
        except IndexError:
            pass
        print "Pawns:", moves
        return moves

    def king_ok(self, line, king_safe):
        if king_safe:
            start, end = tuple(line[:2]), tuple(line[2:])
            if self.color is 'white':
                king = self.board.white_king.position
                color = 'black'
            else:
                king = self.board.black_king.position
                color = 'white'
            return self.board.king_safe_after(start, end, king, color)
        return True


class King(Pawn):
    _me = 'a'
    def possible_moves(self, king_safe=True):
        moves = []
        x, y = self.position
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i, j) == (0, 0):
                    continue
                try:
                    pos = (chr(ord(x) + i), chr(ord(y) + j))
                    print pos,
                    if self.board.in_borders(pos):
                        pawn = self.board.get_pawn(pos)
                        if pawn is '.':
                            line = ''.join(self.position) + ''.join(pos)
                            if self.king_ok(line, king_safe):
                                moves.append(line)
                        elif pawn.color is not self.color:
                            line = ''.join(self.position) + ''.join(pos)
                            if self.king_ok(line, king_safe):
                                moves.append(line)
                except IndexError:
                    pass
        print "King:", moves
        return moves


class Bishop(Pawn):
    _me = 'b'
    def possible_moves(self, king_safe=True):
        moves = []
        x, y = self.position
        temp = 1
        for i in [-1, 1]:
            for j in [-1, 1]:
                try:
                    pos = (chr(ord(x) + temp*i), chr(ord(y) + temp*j))
                    while self.board.get_pawn(pos) is '.':
                        pos = (chr(ord(x) + temp*i), chr(ord(y) + temp*j))
                        if self.board.in_borders(pos):
                            line = ''.join(self.position) + ''.join(pos)
                            if self.king_ok(line, king_safe):
                                moves.append(line)
                        temp = temp + 1
                except IndexError: 
                    pass
        print "Bishop:", moves
        return moves


class Knight(Pawn):
    _me = 'k'
    def possible_moves(self, king_safe=True):
        moves = []
        x, y = self.position
        for j in range(-1, 2, 2):
            for i in range(-1, 2, 2):
                try:
                    pos = (chr(ord(x) + j), chr(ord(y) + i*2))
                    if self.board.in_borders(pos):
                        pawn = self.board.get_pawn(pos)
                        if pawn is '.':
                            line = ''.join(self.position) + ''.join(pos)
                            if self.king_ok(line, king_safe):
                                moves.append(line)                    
                        elif pawn.color is not self.color:
                            line = ''.join(self.position) + ''.join(pos)
                            if self.king_ok(line, king_safe):
                                moves = [line] + moves
                except IndexError:
                    pass
                try:
                    pos = (chr(ord(x) + j*2), chr(ord(y) + i))
                    if self.board.in_borders(pos):
                        pawn = self.board.get_pawn(pos)
                        if pawn is '.':
                            line = ''.join(self.position) + ''.join(pos)
                            if self.king_ok(line, king_safe):
                                moves.append(line)
                        elif pawn.color is not self.color:
                            line = ''.join(self.position) + ''.join(pos)
                            if self.king_ok(line, king_safe):
                                moves = [line] + moves
                except IndexError:
                    pass
        print "Knight:", moves
        return moves

class Rook(Pawn):
    _me = 'r'
    def possible_moves(self, king_safe=True):
        moves = []
        x, y = self.position
        temp = 1
        for j in [-1, 1]:
            try:
                pos = (x, chr(ord(y) + temp*j))
                while self.board.get_pawn(pos) is '.':
                    if self.board.in_borders(pos):
                        line = ''.join(self.position) + ''.join(pos)
                        if self.king_ok(line, king_safe):
                            moves.append(line)
                        temp = temp + 1
                        pos = (x, chr(ord(y) + temp*j))

                    pawn = self.board.get_pawn(pos)
                    if pawn is not '.':
                        if pawn.color is not self.color:
                            line = ''.join(self.position) + ''.join(pos)
                            if self.king_ok(line, king_safe):
                                moves.append(line)
            except IndexError:
                pass
            try:
                temp = 1
                pos = (chr(ord(x) + temp*j), y)
                while self.board.get_pawn(pos) is '.':
                    if self.board.in_borders(pos):
                        line = ''.join(self.position) + ''.join(pos)
                        if self.king_ok(line, king_safe):
                            moves.append(line)
                        temp = temp + 1
                        pos = (chr(ord(x) + temp*j), y)
                    pawn = self.board.get_pawn(pos)
                    if pawn is not '.':
                        if pawn.color is not self.color:
                            line = ''.join(self.position) + ''.join(pos)
                            if self.king_ok(line, king_safe):
                                moves.append(line)    
            except IndexError: 
                pass
        print "Rook:", moves
        return moves
