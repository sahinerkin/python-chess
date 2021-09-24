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

    def moves_available(self, pieces):
        pass

    def set_position(self, coord_alphanum):
        alpha = coord_alphanum[0]
        num = int(coord_alphanum[1])
        self.position = coord_alphanum
        self.position_indexed = Pawn.coord_alphanum_to_index(coord_alphanum)

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
        self.img = pygame.image.load(pieces_root + self.color.value + "_pawn.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)

    def moves_available(self, pieces):
        moves = []
        tmp_x, tmp_y = self.position_indexed
        if self.color == PieceColor.White:
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y-1)
            if tmp_y-1 >= 0 and Piece.piece_in(pieces, tmp_coord_alphanum) is None:
                moves.append(tmp_coord_alphanum)

        else:
            tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y+1)
            if tmp_y+1 < 8 and Piece.piece_in(pieces, tmp_coord_alphanum) is None:
                moves.append(tmp_coord_alphanum)

        return moves


class Rook(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_rook.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)

    # def moves_available(self, pieces):
    #     moves = []
    #     tmp_x, tmp_y = self.position_indexed
    #     if self.color == PieceColor.White:
    #         while tmp_y > 0:
    #             tmp_y -= 1
    #             tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
    #             if Pawn.piece_in(pieces, tmp_coord_alphanum) is not None:
    #                 break
    #             moves.append(tmp_coord_alphanum)
    #
    #     else:
    #         tmp_y += 1
    #         while tmp_y < 8:
    #             tmp_coord_alphanum = Piece.index_to_coord_alphanum(tmp_x, tmp_y)
    #             if Pawn.piece_in(pieces, tmp_coord_alphanum) is not None:
    #                 break
    #             moves.append(tmp_coord_alphanum)
    #
    #     return moves

class Knight(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_knight.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)


class Bishop(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_bishop.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)


class King(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_king.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)


class Queen(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_queen.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)

