from time_decorator import time_decorator


@time_decorator
def solve(board):
    transposed_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    mini_square = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    sequence_of_steps = [
        0, 1, 2, 3, 4, 5, 6, 7, 8,
        9, 10, 11, 12, 13, 14, 15, 16, 17,
        18, 19, 20, 21, 22, 23, 24, 25, 26,
        27, 28, 29, 30, 31, 32, 33, 34, 35,
        36, 37, 38, 39, 40, 41, 42, 43, 44,
        45, 46, 47, 48, 49, 50, 51, 52, 53,
        54, 55, 56, 57, 58, 59, 60, 61, 62,
        63, 64, 65, 66, 67, 68, 69, 70, 71,
        72, 73, 74, 75, 76, 77, 78, 79, 80
    ]
    squ_dict = {
        "88": (8, 8), "87": (8, 7), "86": (8, 6), "85": (5, 8), "84": (5, 7), "83": (5, 6), "82": (2, 8), "81": (2, 7),
        "80": (2, 6),
        "78": (8, 5), "77": (8, 4), "76": (8, 3), "75": (5, 5), "74": (5, 4), "73": (5, 3), "72": (2, 5), "71": (2, 4),
        "70": (2, 3),
        "68": (8, 2), "67": (8, 1), "66": (8, 0), "65": (5, 2), "64": (5, 1), "63": (5, 0), "62": (2, 2), "61": (2, 1),
        "60": (2, 0),
        "58": (7, 8), "57": (7, 7), "56": (7, 6), "55": (4, 8), "54": (4, 7), "53": (4, 6), "52": (1, 8), "51": (1, 7),
        "50": (1, 6),
        "48": (7, 5), "47": (7, 4), "46": (7, 3), "45": (4, 5), "44": (4, 4), "43": (4, 3), "42": (1, 5), "41": (1, 4),
        "40": (1, 3),
        "38": (7, 2), "37": (7, 1), "36": (7, 0), "35": (4, 2), "34": (4, 1), "33": (4, 0), "32": (1, 2), "31": (1, 1),
        "30": (1, 0),
        "28": (6, 8), "27": (6, 7), "26": (6, 6), "25": (3, 8), "24": (3, 7), "23": (3, 6), "22": (0, 8), "21": (0, 7),
        "20": (0, 6),
        "18": (6, 5), "17": (6, 4), "16": (6, 3), "15": (3, 5), "14": (3, 4), "13": (3, 3), "12": (0, 5), "11": (0, 4),
        "10": (0, 3),
        "08": (6, 2), "07": (6, 1), "06": (6, 0), "05": (3, 2), "04": (3, 1), "03": (3, 0), "02": (0, 2), "01": (0, 1),
        "00": (0, 0),
    }

    for i in range(8, -1, -1):
        for j in range(8, -1, -1):
            if board[i][j] > 0:
                i_squ, j_squ = squ_dict[f'{i}{j}']
                transposed_board[j][i] = board[i][j]
                mini_square[i_squ][j_squ] = board[i][j]
                sequence_of_steps.remove(i * 9 + j)

    max_step = len(sequence_of_steps) - 1
    step = -1
    go_straight = True

    while step < max_step:
        if go_straight:
            step += 1
        else:
            step -= 1
        i = sequence_of_steps[step] // 9
        j = sequence_of_steps[step] % 9
        i_squ, j_squ = squ_dict[f'{i}{j}']
        pre_suitable_number = board[i][j]

        while True:
            pre_suitable_number += 1
            if pre_suitable_number > 9:
                board[i][j] = 0
                transposed_board[j][i] = 0
                mini_square[i_squ][j_squ] = 0
                go_straight = False
                break
            elif pre_suitable_number in board[i]:
                continue
            elif pre_suitable_number in transposed_board[j]:
                continue
            elif pre_suitable_number in mini_square[i_squ]:
                continue
            else:
                board[i][j] = pre_suitable_number
                transposed_board[j][i] = pre_suitable_number
                mini_square[i_squ][j_squ] = pre_suitable_number
                go_straight = True
                break
    return board
