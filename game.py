from gameparts import Board
from gameparts.exeptions import FieldIndexError


def main():
    game = Board()
    game.display()
    running = True
    current_player = "X"
    while running:
        # Тут пользователь вводит координаты ячейки.
        while True:
            try:
                row = int(input("Введите номер строки: "))
                if 0 < row >= game.field_size:
                    raise FieldIndexError

                column = int(input("Введите номер столбца: "))
                if 0 < column >= game.field_size:
                    raise FieldIndexError
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
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
