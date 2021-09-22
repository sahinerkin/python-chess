import pygame

# Defining variables for colors and sizes
black_tile_color = (120, 150, 90)
white_tile_color = (240, 240, 210)
margin_size = 50
border_size = 10
bordered_margin_size = margin_size + border_size
tile_size = 75
width = height = 8 * tile_size + 2 * bordered_margin_size


# Draw the chess board
def draw_chess_board():
    # Fill the surface and draw chess board border
    surface.fill(white_tile_color)
    pygame.draw.rect(surface, black_tile_color, pygame.Rect(margin_size, margin_size,
                                                            8 * tile_size + 2 * border_size,
                                                            8 * tile_size + 2 * border_size))

    # Draw all the tiles in the fitting places with the corresponding colors
    for i in range(8):
        for j in range(8):
            tile_color = white_tile_color if (i + j) % 2 == 0 else black_tile_color
            pygame.draw.rect(surface, tile_color,
                             pygame.Rect(bordered_margin_size + i * tile_size,
                                         bordered_margin_size + j * tile_size, tile_size, tile_size))

    win.blit(surface, (0, 0))

    # Add coordinate indicators outside the board
    for idx in range(8):
        coord_num = game_font.render(str(idx + 1), True, black_tile_color)
        coord_l_rect = coord_num.get_rect(
            center=(margin_size / 2, height - bordered_margin_size - (idx + 0.5) * tile_size))
        coord_r_rect = coord_num.get_rect(
            center=(width - margin_size / 2, height - bordered_margin_size - (idx + 0.5) * tile_size))

        coord_alph = game_font.render(chr(97 + idx), True, black_tile_color)
        coord_t_rect = coord_num.get_rect(center=(bordered_margin_size + (idx + 0.5) * tile_size, margin_size / 2))
        coord_b_rect = coord_num.get_rect(
            center=(bordered_margin_size + (idx + 0.5) * tile_size, height - margin_size / 2))

        win.blit(coord_num, coord_l_rect)
        win.blit(coord_num, coord_r_rect)
        win.blit(coord_alph, coord_t_rect)
        win.blit(coord_alph, coord_b_rect)


def main():
    draw_chess_board()
    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


pygame.init()
win = pygame.display.set_mode((width, height))
surface = pygame.Surface((width, height))
pygame.display.set_caption("Python Chess")

pygame.font.init()
game_font = pygame.font.SysFont("Arial", 26)

main()
