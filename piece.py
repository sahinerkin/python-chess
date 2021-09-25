import pygame
from enum import Enum

pieces_root = "./img/pieces/png_final/"


class PieceColor(Enum):
    White = "w"
    Black = "b"


class Piece:
    def __init__(self, color):
        self.color = color
        self.position = self.position_indexed = None
        self.img = None
        self.capturable = True
        self.in_check_pos = False

    def moves_available(self, pieces):
        pass

    def set_position(self, coord_alphanum):
        self.position = coord_alphanum
        self.position_indexed = Pawn.coord_alphanum_to_index(coord_alphanum)

    def move_to(self, coord_alphanum):
        self.set_position(coord_alphanum)

    def draw_to(self, surface, pos_x, pos_y):
        img_rect = self.img.get_rect(center=(pos_x, pos_y))
        surface.blit(self.img, img_rect)

    @staticmethod
    def coord_alphanum_to_index(coord_alphanum):
        alpha = coord_alphanum[0]
        num = int(coord_alphanum[1])
        return ord(alpha)-97, 8-num

    @staticmethod
    def index_to_coord_alphanum(x, y):
        return chr(x+97) + str(8-y)

    @staticmethod
    def piece_in(pieces, coord_alphanum):
        for piece in pieces:
            if piece.position == coord_alphanum:
                return piece
        return None


class Pawn(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.first_move = True
        self.img = pygame.image.load(pieces_root + self.color.value + "_pawn.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)

    def move_to(self, coord_alphanum):
        self.set_position(coord_alphanum)
        self.first_move = False

    def moves_available(self, pieces):
        moves = []
        captures = []

        tmp_x, tmp_y = self.position_indexed

        if self.color == PieceColor.White:
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y-1)
            if tmp_y-1 >= 0 and Piece.piece_in(pieces, tmp_coord_alphanum) is None:
                moves.append(tmp_coord_alphanum)
            if self.first_move:
                tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y-2)
                if tmp_y-2 >= 0 and Piece.piece_in(pieces, tmp_coord_alphanum) is None:
                    moves.append(tmp_coord_alphanum)

            tmp_x, tmp_y = self.position_indexed

            if tmp_x-1 >= 0 and tmp_y-1 >= 0:
                cpt = Piece.piece_in(pieces, Piece.index_to_coord_alphanum(tmp_x-1, tmp_y-1))
                if cpt is not None and cpt.color == PieceColor.Black:
                    if cpt.capturable:
                        captures.append(Piece.index_to_coord_alphanum(tmp_x-1, tmp_y-1))
                    else:
                        self.in_check_pos = True

            if tmp_x+1 <= 7 and tmp_y-1 >= 0:
                cpt = Piece.piece_in(pieces, Piece.index_to_coord_alphanum(tmp_x+1, tmp_y-1))
                if cpt is not None and cpt.color == PieceColor.Black:
                    if cpt.capturable:
                        captures.append(Piece.index_to_coord_alphanum(tmp_x+1, tmp_y-1))
                    else:
                        self.in_check_pos = True

        else:
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y+1)
            if tmp_y+1 <= 7 and Piece.piece_in(pieces, tmp_coord_alphanum) is None:
                moves.append(tmp_coord_alphanum)
            if self.first_move:
                tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y+2)
                if tmp_y+2 <= 7 and Piece.piece_in(pieces, tmp_coord_alphanum) is None:
                    moves.append(tmp_coord_alphanum)

            tmp_x, tmp_y = self.position_indexed

            if tmp_x-1 >= 0 and tmp_y+1 <= 7:
                cpt = Piece.piece_in(pieces, Piece.index_to_coord_alphanum(tmp_x-1, tmp_y+1))
                if cpt is not None and cpt.color == PieceColor.Black:
                    if cpt.capturable:
                        captures.append(Piece.index_to_coord_alphanum(tmp_x-1, tmp_y+1))
                    else:
                        self.in_check_pos = True

            if tmp_x+1 <= 7 and tmp_y+1 <= 7:
                cpt = Piece.piece_in(pieces, Piece.index_to_coord_alphanum(tmp_x+1, tmp_y+1))
                if cpt is not None and cpt.color == PieceColor.Black:
                    if cpt.capturable:
                        captures.append(Piece.index_to_coord_alphanum(tmp_x+1, tmp_y+1))
                    else:
                        self.in_check_pos = True

        return moves, captures


class Rook(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_rook.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)

    def moves_available(self, pieces):
        moves = []
        captures = []
        tmp_x, tmp_y = self.position_indexed

        while tmp_y > 0:
            tmp_y -= 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_y < 7:
            tmp_y += 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x > 0:
            tmp_x -= 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x < 7:
            tmp_x += 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        return moves, captures


class Knight(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_knight.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)

    def moves_available(self, pieces):
        moves = []
        captures = []

        tmp_x, tmp_y = self.position_indexed

        possible_moves = [(tmp_x+1, tmp_y-2), (tmp_x+2, tmp_y-1),
                          (tmp_x+2, tmp_y+1), (tmp_x+1, tmp_y+2),
                          (tmp_x-1, tmp_y+2), (tmp_x-2, tmp_y+1),
                          (tmp_x-2, tmp_y-1), (tmp_x-1, tmp_y-2)]

        for move in possible_moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                continue

            tmp_coord_alphanum = Piece.index_to_coord_alphanum(move[0], move[1])
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                continue

            moves.append(tmp_coord_alphanum)

        return moves, captures


class Bishop(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_bishop.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)

    def moves_available(self, pieces):
        moves = []
        captures = []

        tmp_x, tmp_y = self.position_indexed

        while tmp_x > 0 and tmp_y > 0:
            tmp_x -= 1
            tmp_y -= 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x < 7 and tmp_y > 0:
            tmp_x += 1
            tmp_y -= 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x > 0 and tmp_y < 7:
            tmp_x -= 1
            tmp_y += 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x < 7 and tmp_y < 7:
            tmp_x += 1
            tmp_y += 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        return moves, captures


class King(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.capturable = False
        self.img = pygame.image.load(pieces_root + self.color.value + "_king.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)

    def moves_available(self, pieces):
        moves = []
        captures = []

        tmp_x, tmp_y = self.position_indexed

        possible_moves = [(tmp_x-1, tmp_y-1), (tmp_x, tmp_y-1), (tmp_x+1, tmp_y-1),
                          (tmp_x-1, tmp_y), (tmp_x+1, tmp_y),
                          (tmp_x-1, tmp_y+1), (tmp_x, tmp_y+1), (tmp_x+1, tmp_y+1)]

        for move in possible_moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                continue

            tmp_coord_alphanum = Piece.index_to_coord_alphanum(move[0], move[1])
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                continue

            moves.append(tmp_coord_alphanum)

        return moves, captures


class Queen(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_queen.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)

    def moves_available(self, pieces):
        moves = []
        captures = []

        tmp_x, tmp_y = self.position_indexed

        while tmp_x > 0 and tmp_y > 0:
            tmp_x -= 1
            tmp_y -= 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x < 7 and tmp_y > 0:
            tmp_x += 1
            tmp_y -= 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x > 0 and tmp_y < 7:
            tmp_x -= 1
            tmp_y += 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x < 7 and tmp_y < 7:
            tmp_x += 1
            tmp_y += 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_y > 0:
            tmp_y -= 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_y < 7:
            tmp_y += 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x > 0:
            tmp_x -= 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        tmp_x, tmp_y = self.position_indexed

        while tmp_x < 7:
            tmp_x += 1
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
            piece_in_spot = Pawn.piece_in(pieces, tmp_coord_alphanum)
            if piece_in_spot is not None:
                if piece_in_spot.color != self.color:
                    if piece_in_spot.capturable:
                        captures.append(tmp_coord_alphanum)
                    else:
                        self.in_check_pos = True
                break
            moves.append(tmp_coord_alphanum)

        return moves, captures
