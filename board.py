import pygame
from piece import PieceColor, Piece, Pawn, Rook, Knight, Bishop, King, Queen


class Board:
    pieces = []

    def __init__(self, black_tile_color, white_tile_color, tile_size, margin_size, border_size, piece_size):
        self.black_tile_color = black_tile_color
        self.white_tile_color = white_tile_color
        self.tile_size = tile_size
        self.margin_size = margin_size
        self.border_size = border_size
        self.piece_size = piece_size
        self.bordered_margin_size = margin_size + border_size
        self.width = self.height = 8 * tile_size + 2 * self.bordered_margin_size

    # Draw the chess board (return surface to blit on window)
    def draw(self):
        board_surface = pygame.Surface((self.width, self.height))
        # Fill the surface and draw chess board border
        board_surface.fill(self.white_tile_color)
        pygame.draw.rect(board_surface, self.black_tile_color, pygame.Rect(self.margin_size, self.margin_size,
                                                                           8 * self.tile_size + 2 * self.border_size,
                                                                           8 * self.tile_size + 2 * self.border_size))

        # Draw all the tiles in the fitting places with the corresponding colors
        for i in range(8):
            for j in range(8):
                tile_color = self.white_tile_color if (i + j) % 2 == 0 else self.black_tile_color
                pygame.draw.rect(board_surface, tile_color,
                                 pygame.Rect(self.bordered_margin_size + i * self.tile_size,
                                             self.bordered_margin_size + j * self.tile_size,
                                             self.tile_size, self.tile_size))

        return board_surface

    # Draw the coordinate indicators outside the board (return the surface)
    def draw_indicators(self, game_font):

        indicator_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        indicator_surface = indicator_surface.convert_alpha()

        for idx in range(8):
            coord_num = game_font.render(str(idx + 1), True, self.black_tile_color)
            coord_l_rect = coord_num.get_rect(
                center=(self.margin_size / 2, self.height - self.bordered_margin_size - (idx + 0.5) * self.tile_size))
            coord_r_rect = coord_num.get_rect(
                center=(self.width - self.margin_size / 2,
                        self.height - self.bordered_margin_size - (idx + 0.5) * self.tile_size))

            coord_alpha = game_font.render(chr(97 + idx), True, self.black_tile_color)
            coord_t_rect = coord_num.get_rect(
                center=(self.bordered_margin_size + (idx + 0.5) * self.tile_size, self.margin_size / 2))
            coord_b_rect = coord_num.get_rect(
                center=(self.bordered_margin_size + (idx + 0.5) * self.tile_size, self.height - self.margin_size / 2))

            indicator_surface.blit(coord_num, coord_l_rect)
            indicator_surface.blit(coord_num, coord_r_rect)
            indicator_surface.blit(coord_alpha, coord_t_rect)
            indicator_surface.blit(coord_alpha, coord_b_rect)

        return indicator_surface

    # Draw the pieces in their respective places (return the surface)
    def draw_pieces(self):
        pieces_surface = pygame.Surface((8*self.tile_size, 8*self.tile_size), pygame.SRCALPHA)
        pieces_surface = pieces_surface.convert_alpha()

        for piece in self.pieces:
            piece_x, piece_y = piece.position_indexed
            img_rect = piece.img.get_rect(center=((piece_x+0.5) * self.tile_size,
                                                  (piece_y+0.5) * self.tile_size))
            pieces_surface.blit(piece.img, img_rect)

        return pieces_surface, self.bordered_margin_size, self.bordered_margin_size

    # Place the pieces to their initial positions (as done in the beginning of a usual chess game)
    def reset_pieces(self):
        self.pieces = []

        # White pawns
        self.pieces += [Pawn(PieceColor.White, self.piece_size, coord_alphanum="a2"),
                        Pawn(PieceColor.White, self.piece_size, coord_alphanum="b2"),
                        Pawn(PieceColor.White, self.piece_size, coord_alphanum="c2"),
                        Pawn(PieceColor.White, self.piece_size, coord_alphanum="d2"),
                        Pawn(PieceColor.White, self.piece_size, coord_alphanum="e2"),
                        Pawn(PieceColor.White, self.piece_size, coord_alphanum="f2"),
                        Pawn(PieceColor.White, self.piece_size, coord_alphanum="g2"),
                        Pawn(PieceColor.White, self.piece_size, coord_alphanum="h2")]

        # Black pawns
        self.pieces += [Pawn(PieceColor.Black, self.piece_size, coord_alphanum="a7"),
                        Pawn(PieceColor.Black, self.piece_size, coord_alphanum="b7"),
                        Pawn(PieceColor.Black, self.piece_size, coord_alphanum="c7"),
                        Pawn(PieceColor.Black, self.piece_size, coord_alphanum="d7"),
                        Pawn(PieceColor.Black, self.piece_size, coord_alphanum="e7"),
                        Pawn(PieceColor.Black, self.piece_size, coord_alphanum="f7"),
                        Pawn(PieceColor.Black, self.piece_size, coord_alphanum="g7"),
                        Pawn(PieceColor.Black, self.piece_size, coord_alphanum="h7")]

        # Rooks
        self.pieces += [Rook(PieceColor.White, self.piece_size, coord_alphanum="a1"),
                        Rook(PieceColor.White, self.piece_size, coord_alphanum="h1"),
                        Rook(PieceColor.Black, self.piece_size, coord_alphanum="a8"),
                        Rook(PieceColor.Black, self.piece_size, coord_alphanum="h8")]

        # Knights
        self.pieces += [Knight(PieceColor.White, self.piece_size, coord_alphanum="b1"),
                        Knight(PieceColor.White, self.piece_size, coord_alphanum="g1"),
                        Knight(PieceColor.Black, self.piece_size, coord_alphanum="b8"),
                        Knight(PieceColor.Black, self.piece_size, coord_alphanum="g8")]

        # Bishops
        self.pieces += [Bishop(PieceColor.White, self.piece_size, coord_alphanum="c1"),
                        Bishop(PieceColor.White, self.piece_size, coord_alphanum="f1"),
                        Bishop(PieceColor.Black, self.piece_size, coord_alphanum="c8"),
                        Bishop(PieceColor.Black, self.piece_size, coord_alphanum="f8")]

        # Kings & Queens
        self.pieces += [King(PieceColor.White, self.piece_size, coord_alphanum="d1"),
                        Queen(PieceColor.White, self.piece_size, coord_alphanum="e1"),
                        King(PieceColor.Black, self.piece_size, coord_alphanum="d8"),
                        Queen(PieceColor.Black, self.piece_size, coord_alphanum="e8")]

        self.pieces += [Rook(PieceColor.White, self.piece_size, coord_alphanum="d5")]

    def get_clicked_place(self, mouse_pos):
        pos_x, pos_y = mouse_pos[0]-self.bordered_margin_size, mouse_pos[1]-self.bordered_margin_size
        pos_x, pos_y = pos_x // self.tile_size, pos_y // self.tile_size

        if pos_x < 0 or pos_x >= 8 or pos_y < 0 or pos_y >= 8:
            return None

        else:
            return Piece.index_to_coord_alphanum(pos_x, pos_y)
