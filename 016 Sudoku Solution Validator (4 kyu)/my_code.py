def valid_solution(board):
    for iteration in range(9):  ## checking lines
        if len(board[iteration]) != len(set(board[iteration])):
            return False

        colum = []  ## cheking zero and colums
        for k in range(9):
            if board[k][iteration] == 0:
                return False
            colum.append(board[k][iteration])
        if len(colum) != len(set(colum)):
            return False

        square = []  ## cheking square 3*3
        for i in range(3):
            for j in range(3):
                square.append(board[i + 3 * int(iteration // 3)][j + 3 * (iteration % 3)])
        if len(square) != len(set(square)):
            return False
    return True
