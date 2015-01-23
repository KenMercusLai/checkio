__author__ = 'KenMercusLai'

SHIP = "S"
TORNADO = "O"
ICEBERG = "X"
EMPTY = "."

HUNT_DISTANCE = 2

DIRS = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
    ".": (0, 0)}


def move_ship(sea_map, fuel):
    return "S" or "N" or "W" or "E" or "."


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    import random

    def prepare_map(grid, ship, tornadoes):
        grid = list(list(row) for row in grid)
        grid[ship[0]][ship[1]] = SHIP
        for t in tornadoes:
            grid[t[0]][t[1]] = TORNADO
        return tuple("".join(row) for row in grid)


    def check_solution(func, sea, fuel, tornadoes):
        ship = (0, 0)
        for step in range(fuel):
            user_result = func(prepare_map(sea, ship, tornadoes), fuel - step)
            if not isinstance(user_result, str) or user_result not in DIRS.keys():
                print("You should return a string with an action.")
                return False
            sx, sy = ship
            sea_width = len(sea[0])
            sea_height = len(sea)
            new_sx, new_sy = sx + DIRS[user_result][0], sy + DIRS[user_result][1]
            ship = new_sx, new_sy
            if new_sx < 0 or new_sx >= len(sea) or new_sy < 0 or new_sy >= len(sea[0]):
                print("Captain, we lost.")
                return False
            if (new_sx, new_sy) in tornadoes:
                print("Don't move in a tornado! SOS")
                return False
            if sea[new_sx][new_sy] == ICEBERG:
                print("ICEBERG! Turn to ... SOS")
                return False

            if (new_sx, new_sy) == (sea_height - 1, sea_width - 1):
                print("WIN!")
                print(fuel - step)
                return True

            # And tornado move
            for i in range(len(tornadoes)):
                tx, ty = tornadoes[i]
                possible = []
                for direction, (dx, dy) in DIRS.items():
                    x, y = tx + dx, ty + dy
                    if 0 <= x < sea_height and 0 <= y < sea_width and sea[x][y] != ICEBERG and (x, y) not in tornadoes:
                        possible.append((direction, (x, y)))
                distance = abs(sx - tx) + abs(sy - ty)
                if distance <= HUNT_DISTANCE:
                    best = float("inf"), (tx, ty), "."
                    for d, (x, y) in possible:
                        possible_distance = abs(sx - x) + abs(sy - y)
                        if possible_distance < best[0]:
                            best = possible_distance, (x, y), d
                        elif possible_distance == best[0]:
                            best = random.choice([(possible_distance, (x, y), d), best])
                    tornadoes[i] = best[1]
                else:
                    rand = random.choice(possible)
                    tornadoes[i] = rand[1]
            if ship in tornadoes:
                print("Tornado caught us, Cap.")
                return False
        print("We don't have fuel.")
        return False

    assert check_solution(move_ship, (
        ".....",
        ".XXX.",
        "...X.",
        ".XXX.",
        ".....",), 100, [(2, 2)]), "First"