import pygame
import piece


class Board:
    tiles = 8 * [[0] * 8]

    def __init__(self, black_tile_color, white_tile_color, tile_size, margin_size, border_size):
        self.black_tile_color = black_tile_color
        self.white_tile_color = white_tile_color
        self.tile_size = tile_size
        self.margin_size = margin_size
        self.border_size = border_size
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
        return pieces_surface, self.bordered_margin_size, self.bordered_margin_size

    def print_tiles(self):
        print(self.tiles)
