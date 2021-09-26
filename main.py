import pygame
from board import Board
from piece import Piece, PieceColor

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

    win.fill(chessboard.white_tile_color)

    indicator_surface = chessboard.draw_indicators(game_font=game_font)
    win.blit(indicator_surface, (0, 0))

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
    board.reset_pieces()

    draw_everything(win, board)

    turn = PieceColor.White

    drag = False
    dragged_piece = None
    drag_surface = pygame.Surface((board.window_width, board.window_height), pygame.SRCALPHA)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                if drag and dragged_piece is not None:
                    img_rect = dragged_piece.img.get_rect(center=pygame.mouse.get_pos())
                    draw_everything(window=win, chessboard=board, clicked_piece=dragged_piece)
                    drag_surface.fill((0, 0, 0, 0))
                    drag_surface.blit(dragged_piece.img, img_rect)
                    win.blit(drag_surface, (0, 0))
                    pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_place = board.get_clicked_place(pygame.mouse.get_pos())
                # print("Place " + clicked_place if clicked_place is not None else "Place Invalid")
                if clicked_place is not None:
                    clicked_piece = Piece.piece_in(board.pieces, clicked_place)
                    if clicked_piece is not None and turn == clicked_piece.color:
                        draw_everything(window=win, chessboard=board, clicked_piece=clicked_piece)
                        drag = True
                        dragged_piece = clicked_piece
                        board.remove_piece_at(clicked_piece.position)
                        drag_surface.fill((0, 0, 0, 0))
                        win.blit(drag_surface, (0, 0))
                        pygame.display.update()
                    else:
                        draw_everything(window=win, chessboard=board)

            if event.type == pygame.MOUSEBUTTONUP and drag:
                drag = False
                if dragged_piece is not None:
                    dropped_place = board.get_clicked_place(pygame.mouse.get_pos())
                    if dropped_place is not None:
                        moves, captures = dragged_piece.moves_available(board.pieces)
                        if dropped_place in moves:
                            dragged_piece.move_to(dropped_place)
                            turn = PieceColor.Black if turn == PieceColor.White else PieceColor.White
                        elif dropped_place in captures:
                            board.remove_piece_at(dropped_place)
                            dragged_piece.move_to(dropped_place)
                            turn = PieceColor.Black if turn == PieceColor.White else PieceColor.White

                    board.pieces.append(dragged_piece)

                draw_everything(win, board)


if __name__ == "__main__":
    main()
