from gameparts import Board
from gameparts.exeptions import FieldIndexError, CellOccupiedError


def main():
    game = Board()
    game.display()
    running = True
    current_player = "X"
    while running:
        # Тут пользователь вводит координаты ячейки.
        while True:
            try:
                row = int(input("Введите номер строки: ")) - 1
                if 0 < row >= game.field_size:
                    raise FieldIndexError

                column = int(input("Введите номер столбца: ")) - 1
                if 0 < column >= game.field_size:
                    raise FieldIndexError

                if game.board[row][column] != " ":
                    raise CellOccupiedError

            except FieldIndexError:
                print(
                    f"Значение должно быть неотрицательным и меньше {game.field_size}."
                )
                print("Пожалуйста, введите значения для строки и столбца заново.")
                continue

            except ValueError:
                print("Буквы вводить нельзя. Только числа.")
                print("Пожалуйста, введите значения для строки и столбца заново.")
                continue

            except Exception as e:
                print(f"Возникла ошибка: {e}")
                continue

            else:
                break

        game.make_move(row, column, current_player)
        print("Ход сделан!")
        game.display()

        if game.chek_win(current_player):
            print(f"Победил игрок: {current_player}")
            print('Еще игру? y/n')
            if input() == 'y':
                game.clear_board()
                game.display()
                current_player = 'X'
            else:
                running = False

        if game.is_board_full():
            print("Ничья")
            print('Еще игру? y/n')
            if input() == 'y':
                game.clear_board()
                game.display()
                current_player = 'X'
            else:
                running = False

        
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
