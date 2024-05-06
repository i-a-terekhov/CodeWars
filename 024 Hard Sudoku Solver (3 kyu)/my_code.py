from time_decorator import time_decorator


@time_decorator
def solve(board):
    normal_lines = [[], [], [], [], [], [], [], [], []]
    transposed_lines = [[], [], [], [], [], [], [], [], []]
    squads_list = [
        [], [], [],
        [], [], [],
        [], [], []
    ]
    base_sequence_of_steps = [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
        (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
        (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
        (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
        (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8),
        (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8),
    ]

    mini_square_adresses = [
        ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)),
        ((3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)),
        ((6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)),
        ((0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)),
        ((3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)),
        ((6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)),
        ((0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)),
        ((3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)),
        ((6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)),
    ]

    coordinates_to_squad_number = {
        "88": 8, "87": 8, "86": 8, "85": 5, "84": 5, "83": 5, "82": 2, "81": 2, "80": 2,
        "78": 8, "77": 8, "76": 8, "75": 5, "74": 5, "73": 5, "72": 2, "71": 2, "70": 2,
        "68": 8, "67": 8, "66": 8, "65": 5, "64": 5, "63": 5, "62": 2, "61": 2, "60": 2,
        "58": 7, "57": 7, "56": 7, "55": 4, "54": 4, "53": 4, "52": 1, "51": 1, "50": 1,
        "48": 7, "47": 7, "46": 7, "45": 4, "44": 4, "43": 4, "42": 1, "41": 1, "40": 1,
        "38": 7, "37": 7, "36": 7, "35": 4, "34": 4, "33": 4, "32": 1, "31": 1, "30": 1,
        "28": 6, "27": 6, "26": 6, "25": 3, "24": 3, "23": 3, "22": 0, "21": 0, "20": 0,
        "18": 6, "17": 6, "16": 6, "15": 3, "14": 3, "13": 3, "12": 0, "11": 0, "10": 0,
        "08": 6, "07": 6, "06": 6, "05": 3, "04": 3, "03": 3, "02": 0, "01": 0, "00": 0,
    }

    for i in range(8, -1, -1):
        for j in range(8, -1, -1):
            if board[i][j] > 0:
                squad_number = coordinates_to_squad_number[f'{i}{j}']
                normal_lines[i].append(board[i][j])
                transposed_lines[j].append(board[i][j])
                squads_list[squad_number].append(board[i][j])
                base_sequence_of_steps.remove((i, j))

    queue_of_squads = []
    squads_potential = {}
    for squad in range(9):
        squads_potential[squad] = len(squads_list[squad])
    lines_from_squads = {
        '012': 0, '345': 0, '678': 0,
        '036': 0, '147': 0, '258': 0
    }
    for squad, potential in squads_potential.items():
        if squad in [0, 1, 2]:
            lines_from_squads['012'] += potential
        elif squad in [3, 4, 5]:
            lines_from_squads['345'] += potential
        elif squad in [6, 7, 8]:
            lines_from_squads['678'] += potential
        if squad in [0, 3, 6]:
            lines_from_squads['036'] += potential
        elif squad in [1, 4, 7]:
            lines_from_squads['147'] += potential
        elif squad in [2, 5, 8]:
            lines_from_squads['258'] += potential

    sorted_squads = sorted(lines_from_squads, key=lines_from_squads.get, reverse=True)
    for squad in sorted_squads:
        for field in squad:
            if int(field) not in queue_of_squads:
                queue_of_squads.append(int(field))

    right_sequence_of_steps = []
    for squad in queue_of_squads:
        for address in mini_square_adresses[squad]:
            if address in base_sequence_of_steps:
                right_sequence_of_steps.append(address)

    max_step = len(right_sequence_of_steps) - 1
    step = -1
    go_straight = True
    while step < max_step:
        if go_straight:
            step += 1
        else:
            step -= 1
        i, j = right_sequence_of_steps[step]
        squad_number = coordinates_to_squad_number[f'{i}{j}']
        if board[i][j] > 0:
            transposed_lines[j].remove(board[i][j])
            squads_list[squad_number].remove(board[i][j])
        pre_suitable_number = board[i][j]

        while True:
            pre_suitable_number += 1
            if pre_suitable_number > 9:
                board[i][j] = 0
                go_straight = False
                break
            elif pre_suitable_number in board[i]:
                continue
            elif pre_suitable_number in transposed_lines[j]:
                continue
            elif pre_suitable_number in squads_list[squad_number]:
                continue
            else:
                board[i][j] = pre_suitable_number
                transposed_lines[j].append(pre_suitable_number)
                squads_list[squad_number].append(pre_suitable_number)
                go_straight = True
                break
    return board
