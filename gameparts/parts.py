class Board:
    field_size = 3

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    # def display(self):
    #     for row in self.board:
    #         print("|".join(row))
    #         print("-" * 5)

    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == " ":
                    return False
        return True

    def chek_win(self, player):
        for i in range(self.field_size):
            if all([self.board[i][j] == player for j in range(self.field_size)]) or all(
                [self.board[j][i] == player for j in range(self.field_size)]
            ):
                return True
            elif all(
                [self.board[i][i] == player for i in range(self.field_size)]
            ) or all([self.board[i][i - 2] == player for i in range(self.field_size)]):
                return True
        return False

    def clear_board(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                self.board[i][j] = " "

    def save_result(self, player=None):
        with open(R"C:\Dev\tic_tac_toe\results.txt", "a", encoding="utf-8") as o:
            if player is None:
                o.write("Ничья" + "\n")
            else:
                o.write(f"Победил игрок {player}" + "\n")

    def __str__(self):
        return f"Объект игрового поля размером {self.field_size}x{self.field_size}"
