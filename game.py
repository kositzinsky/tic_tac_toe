from gameparts import Board
import pygame


pygame.init()

CELL_SIZE = 200
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

running = True
current_player = "X"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)


def draw_lines():
    # Горизонтальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH,
        )
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH,
        )


def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == "X":
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE,
                    ),
                    X_WIDTH,
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE),
                    (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE),
                    X_WIDTH,
                )
            elif board[row][col] == "O":
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2,
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH,
                )


def main():
    game = Board()
    current_player = "X"
    running = True
    draw_lines()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_col] == " ":
                    game.make_move(clicked_row, clicked_col, current_player)

                    if game.chek_win(current_player):
                        game.save_result(current_player)
                        running = False
                    elif game.is_board_full():
                        game.save_result()
                        running = False

                    current_player = "O" if current_player == "X" else "X"
                    draw_figures(game.board)

            pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
