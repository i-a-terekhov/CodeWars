from time_decorator import time_decorator


@time_decorator
def solve(puzzle):
    def guessAt():
        _, x, y = min((len(s), x, y) for x, row in enumerate(grid) for y, s in enumerate(row) if s)
        return x, y, grid[x][y].pop()

    def isValid():
        return all(bool(s) ^ bool(ans[x][y]) for x, row in enumerate(grid) for y, s in enumerate(row))

    def filterGridSets(i, j, v):
        nonlocal counts
        counts += 1
        ans[i][j] = v
        xS, yS = i // 3 * 3, j // 3 * 3
        for z in range(9):
            for a, b in ((i, z), (z, j), (xS + z // 3, yS + z % 3)):  # in row, in col, in square
                grid[a][b].discard(v)

    grid = [[{puzzle[x][y]} if puzzle[x][y] else {1, 2, 3, 4, 5, 6, 7, 8, 9} for y in range(9)] for x in range(9)]
    stk, counts, ans = [], 0, [[0] * 9 for _ in range(9)]

    while counts != 81:

        change = True
        while change:
            change = False
            for x in range(9):
                for y in range(9):
                    if len(grid[x][y]) == 1:
                        change = True
                        filterGridSets(x, y, grid[x][y].pop())
        if counts == 81: break

        if isValid():
            x, y, guess = guessAt()
            stk.append(([[set(s) for s in r] for r in grid], [r[:] for r in ans], x, y, guess, counts))
            grid[x][y].clear()
            filterGridSets(x, y, guess)
        else:
            grid, ans, x, y, guess, counts = stk.pop()
            grid[x][y].discard(guess)

    return ans
