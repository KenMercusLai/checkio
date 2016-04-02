def count_neighbours(grid, row, col):
    # get indexes of rows and cols we want to slide out
    rows = [i for i in range(row-1, row+2) if 0 <= i <= len(grid) - 1]
    cols = [i for i in range(col-1, col+2) if 0 <= i <= len(grid[0]) -1]
    neighbors = [grid[r][c] for r in rows for c in cols]
    # we don't want to count outselves
    return sum(neighbors) - grid[row][col]


if __name__ == '__main__': #pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
