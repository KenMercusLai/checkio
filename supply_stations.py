def supply_routes(the_map):
    return "", "", "", ""


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    DIRS = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1),
    }

    def checker(f, the_map):
        result = f(the_map)
        if (not isinstance(result, (tuple, list)) and len(the_map) != 4 and
                any(not isinstance(r, str) for r in the_map)):
            return False, "The result must be a list/tuple of four strings"
        stations = [None] * 4
        factory_supply = [0] * 4
        for i, row in enumerate(the_map):
            for j, ch in enumerate(row):
                if ch in "1234":
                    stations[int(ch) - 1] = (i, j)
        wmap = [list(row) for row in the_map]
        width = len(wmap[0])
        height = len(wmap)
        for numb, route in enumerate(result, 1):
            coor = stations[numb - 1]
            for i, ch in enumerate(route):
                if ch not in DIRS.keys():
                    return False, "Routes must contain only NSWE"
                row, col = coor[0] + DIRS[ch][0], coor[1] + DIRS[ch][1]
                if not (0 <= row < height and 0 <= col < width):
                    return False, "Ooops, we lost the route from station {}".format(numb)
                checked = wmap[row][col]
                if checked == "X":
                    return False, "The route {} was struck {} {}".format(numb, coor, (row, col))
                if checked == "F":
                    factory_supply[numb - 1] = 1
                    if i >= len(route):
                        return False, "A route should be ended in the factory"
                    break
                if checked != ".":
                    return False, "Don't intersect routes"
                wmap[row][col] = str(numb)
                coor = row, col
        if factory_supply != [1, 1, 1, 1]:
            return False, "You should deliver all four resources"
        return True, "Great!"

    test1 = checker(supply_routes, ("..........",
                                    ".1X.......",
                                    ".2X.X.....",
                                    ".XXX......",
                                    ".X..F.....",
                                    ".X........",
                                    ".X..X.....",
                                    ".X..X.....",
                                    "..3.X...4.",
                                    "....X....."))
    print(test1[1])
    assert test1[0], "First test"
    test2 = checker(supply_routes, ("1...2",
                                    ".....",
                                    "..F..",
                                    ".....",
                                    "3...4"))
    print(test2[1])
    assert test2[0], "Second test"
    test3 = checker(supply_routes, ("..2..",
                                    ".....",
                                    "1.F.3",
                                    ".....",
                                    "..4.."))
    print(test3[1])
    assert test3[0], "Third test"

