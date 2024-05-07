def validateBattlefield(field):
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in field]))

    ships = []

    # this algorithm uses the field 2-dimensional array it self to store infomration about the size of ships found
    for i in range(0, 10):
        for j in range(0, 10):
            # if not at end of any edge in 2d-array, check that sum of two cross diagonal elements is not more than max
            # if it is then two ships are two close
            if j < 9 and i < 9:
                if field[i][j] + field[i + 1][j + 1] > max(field[i][j], field[i + 1][j + 1]):
                    return False
                if field[i + 1][j] + field[i][j + 1] > max(field[i + 1][j], field[i][j + 1]):
                    return False
            # if the element at position (i, j) is occupied then add the current value of position to next
            if j < 9 and field[i][j] > 0 and field[i][j + 1] > 0:
                field[i][j + 1] += field[i][j]
            elif i < 9 and field[i][j] > 0 and field[i + 1][j] > 0:
                field[i + 1][j] += field[i][j]
            elif field[i][j] > 0:
                ships.append(field[i][j])  # since we add numbers

    ships.sort()

    return ships == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]  # if the ships we have found are of correct configuration
                                                    # then it will equal this array

