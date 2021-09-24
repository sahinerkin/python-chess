import pygame
from board import Board
from piece import Piece

pygame.init()
board = Board(black_tile_color=(120, 150, 90),
              white_tile_color=(240, 240, 210),
              tile_size=75,
              margin_size=50,
              border_size=10,
              piece_size=88)

win = pygame.display.set_mode((board.window_width, board.window_height))
win.fill(board.white_tile_color)
pygame.display.set_caption("Python Chess")

pygame.font.init()
game_font = pygame.font.SysFont("Arial", board.margin_size//2)


def draw_everything(window, chessboard, clicked_piece=None):
    board_surface = chessboard.draw()
    window.blit(board_surface, (chessboard.margin_size, chessboard.margin_size))
    pieces_surface, ps_x, ps_y = chessboard.draw_pieces()
    window.blit(pieces_surface, (ps_x, ps_y))
    if clicked_piece is not None:
        moves, captures = clicked_piece.moves_available(chessboard.pieces)
        move_surface, ms_x, ms_y = chessboard.draw_moves(moves, captures)
        window.blit(move_surface, (ms_x, ms_y))
    pygame.display.update()


def main():
    board_surface = board.draw()
    win.blit(board_surface, (board.margin_size, board.margin_size))

    indicator_surface = board.draw_indicators(game_font=game_font)
    win.blit(indicator_surface, (0, 0))

    board.reset_pieces()
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
                clicked_place = board.get_clicked_place(pygame.mouse.get_pos())
                print("Piece " + clicked_place if clicked_place is not None else "Piece Invalid")
                if clicked_place is not None:
                    clicked_piece = Piece.piece_in(board.pieces, clicked_place)
                    draw_everything(window=win, chessboard=board, clicked_piece=clicked_piece)


if __name__ == "__main__":
    main()
