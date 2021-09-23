import pygame
from board import Board
from piece import PieceColor, Pawn

pygame.init()
board = Board(black_tile_color=(120, 150, 90),
              white_tile_color=(240, 240, 210),
              tile_size=75,
              margin_size=50,
              border_size=10)

win = pygame.display.set_mode((board.width, board.height))
pygame.display.set_caption("Python Chess")

pygame.font.init()
game_font = pygame.font.SysFont("Arial", 26)


def main():
    board_surface = board.draw()
    win.blit(board_surface, (0, 0))

    indicator_surface = board.draw_indicators(game_font=game_font)
    win.blit(indicator_surface, (0, 0))

    # mypawn = Pawn(PieceColor.Black, 88)
    # mypawn.set_position("c7")
    # print(mypawn.position)
    # print(mypawn.position_indexed)

    pieces_surface, ps_x, ps_y = board.draw_pieces()
    win.blit(pieces_surface, (ps_x, ps_y))
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


main()
