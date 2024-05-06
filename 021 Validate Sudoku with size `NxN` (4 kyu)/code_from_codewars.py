import math


class Sudoku(object):
    def __init__(self, board):
        self.board = board

    def is_valid(self):
        if not isinstance(self.board, list):
            return False
        n = len(self.board)
        rootN = int(round(math.sqrt(n)))
        if rootN * rootN != n:
            return False
        isValidRow = lambda r: (isinstance(r, list) and
                                len(r) == n and
                                all(map(lambda x: type(x) == int, r)))
        if not all(map(isValidRow, self.board)):
            return False
        oneToN = set(range(1, n + 1))
        isOneToN = lambda l: set(l) == oneToN
        tranpose = [[self.board[j][i] for i in range(n)] for j in range(n)]
        squares = [[self.board[p + x][q + y] for x in range(rootN)
                    for y in range(rootN)]
                   for p in range(0, n, rootN)
                   for q in range(0, n, rootN)]
        return (all(map(isOneToN, self.board)) and
                all(map(isOneToN, tranpose)) and
                all(map(isOneToN, squares)))
