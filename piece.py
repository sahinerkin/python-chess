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

    def set_position(self, coord_alphanum):
        alpha = coord_alphanum[0]
        num = int(coord_alphanum[1])
        self.position = coord_alphanum
        self.position_indexed = (ord(alpha)-97, 8-num)

    def draw_to(self, surface, pos_x, pos_y):
        img_rect = self.img.get_rect(center=(pos_x, pos_y))
        surface.blit(self.img, img_rect)


class Pawn(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_pawn.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)


class Rook(Piece):
    def __init__(self, color, size, coord_alphanum=None):
        super().__init__(color)
        self.img = pygame.image.load(pieces_root + self.color.value + "_rook.png")
        self.img = pygame.transform.scale(self.img, (size, size)).convert_alpha()
        if coord_alphanum:
            self.set_position(coord_alphanum)


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

