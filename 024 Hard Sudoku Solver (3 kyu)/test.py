from hard_sudoku_solver import solve
from old_version import solve as old_version
from code_from_codewars import solve as cw_solve


problem = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]

problem2 = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 3]
        ]

problem3 = [
            [7, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]

problem4 = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]

problem5 = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 3]
        ]

problem6 = [
            [7, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]

problem7 = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]

problem8 = [
            [9, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 3]
        ]

problem9 = [
            [7, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 4, 0, 6, 0, 0, 0],
            [0, 0, 5, 0, 7, 0, 3, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 4, 0],
            [4, 0, 1, 0, 6, 0, 5, 0, 8],
            [0, 9, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 7, 0, 3, 0, 2, 0, 0],
            [0, 0, 0, 7, 0, 5, 0, 0, 0],
            [1, 0, 0, 0, 4, 0, 0, 0, 7]
        ]


old_version(problem)
old_version(problem2)
old_version(problem3)
print('-' * 20)
solve(problem4)
solve(problem5)
solve(problem6)
print('-' * 20)
cw_solve(problem7)
cw_solve(problem8)
cw_solve(problem9)
