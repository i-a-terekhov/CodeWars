def validate_battlefield(field):
    ships = {"sub": 4, "cruiser": 3, "destryer": 2, "battleship": 1}
    extra_field = [[0 for i in range(0, 15)] for j in range(0, 15)]
    for i in range(0, 10):
        for j in range(0, 10):
            extra_field[i + 1][j + 1] = field[i][j]
    # check diagonal cells
    for i in range(1, 11):
        for j in range(1, 11):
            if extra_field[i][j] == 1:
                for k in (i - 1, i + 1):
                    for m in (j - 1, j + 1):
                        if extra_field[k][m] > 0:
                            return False
                # find the bow of the ship (upper left cell of the ship)
                if extra_field[i - 1][j] + extra_field[i][j - 1] == 0:
                    # submarine check
                    if extra_field[i + 1][j] + extra_field[i][j + 1] == 0:
                        ships['sub'] -= 1
                    # cruiser check
                    elif (
                            (extra_field[i + 1][j], extra_field[i + 2][j]) == (1, 0) or
                            (extra_field[i][j + 1], extra_field[i][j + 2]) == (1, 0)):
                        ships['cruiser'] -= 1
                    # destroyer check
                    elif (
                            (extra_field[i + 1][j],
                             extra_field[i + 2][j],
                             extra_field[i + 3][j]) == (1, 1, 0) or
                            (extra_field[i][j + 1],
                             extra_field[i][j + 2],
                             extra_field[i][j + 3]) == (1, 1, 0)):
                        ships['destryer'] -= 1
                    # battleship check
                    elif (
                            (extra_field[i + 3][j], extra_field[i + 4][j]) == (1, 0) or
                            (extra_field[i][j + 3], extra_field[i][j + 4]) == (1, 0)):
                        ships['battleship'] -= 1
                    else:
                        return False

    for value in ships.values():
        if value != 0: return False
    return True
