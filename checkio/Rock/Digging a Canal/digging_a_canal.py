from copy import deepcopy


def checkio(land_map):
    adjencencies = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    land_map = [[0] * len(land_map[0])] + land_map
    distance_map = deepcopy(land_map)
    for i in range(1, len(distance_map)):
        for j in range(len(distance_map[0])):
            distance_map[i][j] = len(land_map) ** 2
    while True:
        changed = False
        for row in range(1, len(land_map)):
            for col in range(len(land_map[0])):
                temp_distance = []
                for i in adjencencies:
                    if (
                        0 <= row + i[0] <= len(land_map) - 1
                        and 0 <= col + i[1] <= len(land_map[0]) - 1
                    ):
                        temp_distance.append(
                            land_map[row][col] + distance_map[row + i[0]][col + i[1]]
                        )
                new_distance = min(temp_distance)
                if new_distance != distance_map[row][col]:
                    distance_map[row][col] = new_distance
                    changed = True
                    break
            if changed:
                break
        if not changed:
            break
    return min(distance_map[-1])


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert (
        checkio(
            [
                [1, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0, 0, 1],
                [1, 1, 1, 1, 1, 0, 1],
                [1, 1, 0, 1, 1, 0, 1],
                [1, 1, 0, 1, 1, 1, 1],
                [1, 0, 0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1],
            ]
        )
        == 2
    ), "1st example"
    assert (
        checkio(
            [
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
            ]
        )
        == 3
    ), "2nd example"
    assert (
        checkio(
            [
                [1, 1, 1, 1, 1, 0, 1, 1],
                [1, 0, 1, 1, 1, 0, 1, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 0, 0],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1],
            ]
        )
        == 2
    ), "3rd example"
