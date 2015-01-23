def finish_map(regional_map):
    # extend original map
    extended_map = ['S' + i + 'S' for i in regional_map]
    extended_map = ['S' * len(extended_map[0])] + extended_map + ['S' * len(extended_map[0])]

    # mark squares
    changed = True
    while changed:
        changed = False
        for row in range(1, len(extended_map) - 1):
            for col in range(1, len(extended_map[0]) - 1):
                if extended_map[row][col] == '.':
                    surronded_squares = (extended_map[row - 1][col - 1:col + 2]
                                         + extended_map[row][col - 1:col + 2]
                                         + extended_map[row + 1][col - 1:col + 2])
                    if 'X' not in surronded_squares:
                        if ('D' in surronded_squares[1] or 'D' in surronded_squares[3] or
                                'D' in surronded_squares[5] or 'D' in surronded_squares[7]):
                            extended_map[row] = extended_map[row][:col] + 'D' + extended_map[row][col + 1:]
                            changed = True
                            break
            if changed:
                break

    # fill left . to S
    for row in range(len(extended_map)):
        for col in range(len(extended_map[0])):
            if extended_map[row][col] == '.':
                extended_map[row] = extended_map[row][:col] + 'S' + extended_map[row][col + 1:]

    extended_map = extended_map[1:-1]
    return [i[1:-1] for i in extended_map]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert isinstance(
        finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"

    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"

