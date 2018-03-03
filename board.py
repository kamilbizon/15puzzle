class Board():
    def __init__(self):

        self.EMPTY = ""

        self.board = [[""]*4 for _ in range(4)]

        index = 1
        for i in range(4):
            for j in range(4):
                self.board[i][j] = index
                index += 1
        self.board[3][3] = self.EMPTY

    def available_moves(self, empty_coordinates):

        # find coordinates of empty
        for i in self.board:
            for j in i:
                empty_coordinates = (self.board.index(i), i.index(j))

        # square in the middle
        if 0 < empty_coordinates[0] < 3 and 0 < empty_coordinates[1] < 3:
            return ((empty_coordinates[0] - 1, empty_coordinates[1]),
                    (empty_coordinates[0], empty_coordinates[1] + 1),
                    (empty_coordinates[0], empty_coordinates[1] - 1),
                    (empty_coordinates[0] + 1, empty_coordinates[1]))
        # corners
        elif empty_coordinates == (0, 0):
            return ((0, 1), (1, 0))
        elif empty_coordinates == (0, 3):
            return ((0, 2), (1, 3))
        elif empty_coordinates == (3, 0):
            return ((2, 0), (3, 1))
        elif empty_coordinates == (3, 3):
            return ((2, 3), (3, 2))
        # left column
        elif empty_coordinates[0] == 0:
            return ((empty_coordinates[0], empty_coordinates[1] - 1),
                    (empty_coordinates[0], empty_coordinates[1] + 1),
                    (empty_coordinates[0] + 1, empty_coordinates[1]))
        # right column
        elif empty_coordinates[0] == 3:
            return((empty_coordinates[0], empty_coordinates[1] - 1),
                   (empty_coordinates[0], empty_coordinates[1] + 1),
                   (empty_coordinates[0] - 1, empty_coordinates[1]))
        # top row
        elif empty_coordinates[1] == 0:
            return((empty_coordinates[0] - 1, empty_coordinates[1]),
                   (empty_coordinates[0] + 1, empty_coordinates[1]),
                   (empty_coordinates[0], empty_coordinates[1] + 1))
        # bottom row
        else:
            return((empty_coordinates[0] - 1, empty_coordinates[1]),
                   (empty_coordinates[0] + 1, empty_coordinates[1]),
                   (empty_coordinates[0], empty_coordinates[1] - 1))


board = Board()

# print board
# for i  in range(4):
#     for j in range(4):
#         print(board.board[i][j],"\t", end="")
#     print()

# test available_moves
# for i in range(4):
#     for j in range(4):
#         print(board.available_moves((i, j)))

class Game():
    pass