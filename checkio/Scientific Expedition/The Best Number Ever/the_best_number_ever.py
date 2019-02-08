def generate_segments(coners):
    # generate line segments based on corner numbers
    # the results are sorted by the first item,
    # or the second if the first one is the same
    h_lines = [(coners[0], coners[1]), (coners[2], coners[3])]

    v_lines = [(coners[0], coners[2]), (coners[1], coners[3])]

    segments = []
    for line in h_lines:
        for i in range(line[0], line[1]):
            segments.append((i, i + 1))

    for line in v_lines:
        for i in range(line[0], line[1], 4):
            segments.append((i, i + 4))

    return sorted(segments)


def generate_all_squares():
    # generate all possible squares.
    ret = []
    # 1x1
    for i in [1, 2, 3, 5, 6, 7, 9, 10, 11]:
        corners = [i, i + 1, i + 4, i + 1 + 4]
        ret.append(generate_segments(corners))
    # 2x2
    for i in [1, 2, 5, 6]:
        corners = [i, i + 2, i + 8, i + 2 + 8]
        ret.append(generate_segments(corners))

    # 3x3
    for i in [1]:
        corners = [i, i + 3, i + 12, i + 3 + 12]
        ret.append(generate_segments(corners))

    return ret


def checkio(lines_list):
    """Return the quantity of squares."""
    all_squares = generate_all_squares()
    lines_list = set(map(lambda x: tuple(sorted(x)), lines_list))
    squares = 0
    for i in all_squares:
        if set(i).intersection(lines_list) == set(i):
            squares += 1
    return squares


if __name__ == '__main__':
    assert (
        checkio(
            [
                [1, 2],
                [3, 4],
                [1, 5],
                [2, 6],
                [4, 8],
                [5, 6],
                [6, 7],
                [7, 8],
                [6, 10],
                [7, 11],
                [8, 12],
                [10, 11],
                [10, 14],
                [12, 16],
                [14, 15],
                [15, 16],
            ]
        )
        == 3
    ), "First, from description"
    assert (
        checkio(
            [
                [1, 2],
                [2, 3],
                [3, 4],
                [1, 5],
                [4, 8],
                [6, 7],
                [5, 9],
                [6, 10],
                [7, 11],
                [8, 12],
                [9, 13],
                [10, 11],
                [12, 16],
                [13, 14],
                [14, 15],
                [15, 16],
            ]
        )
        == 2
    ), "Second, from description"
    assert checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1, "Third, one small square"
    assert (
        checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0
    ), "Fourth, it's not square"
    assert (
        checkio([[16, 15], [16, 12], [15, 11], [11, 10], [10, 14], [14, 13], [13, 9]])
        == 0
    ), "Fifth, snake"
