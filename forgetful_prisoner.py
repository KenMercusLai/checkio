def translate_map_to_memory(map_array):
    return int(''.join([''.join(i) for i in map_array]), 2)

def translate_memory_to_map(memory):
    return [list(bin(memory)[2:].zfill(100)[i:i+10]) for i in range(0, 100, 10)]

def find_possible_position(scanner):
    result = []
    for y in range(scanner['N'], 10-scanner['S']):
        for x in range(scanner['W'], 10-scanner['E']):
            result.append((y, x))
    return result

def find_path(scanner, memory):
    positions = find_possible_position(scanner)
    if len(positions) == 1:
        print(translate_memory_to_map(memory))
        
    return "SE", memory


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    WALL = "X"
    EXIT = "E"
    EMPTY = "."
    MAX_STEP = 300

    def get_visible(maze, player):
        result = {}
        for direction, (dr, dc) in DIR.items():
            cr, cc = player
            distance = -1
            while maze[cr][cc] != WALL:
                cr += dr
                cc += dc
                distance += 1
            result[direction] = distance
        return result

    def checker(func, player, maze):
        step = 0
        memory = 0
        while True:
            result, memory = func(get_visible(maze, player), memory)
            if not isinstance(result, str) or any(ch not in DIR.keys() for ch in result):
                print("The function should return a string with directions.")
                return False
            if not isinstance(memory, int) or memory < 0 or memory >= 2 ** 100:
                print("The memory number should be an integer from 0 to 2**100.")
                return False
            for act in result:
                if step >= MAX_STEP:
                    print("You are tired and your scanner is off. Bye bye.")
                    return False
                r, c = player[0] + DIR[act][0], player[1] + DIR[act][1]
                if maze[r][c] == WALL:
                    print("BAM! You in the wall at {}, {}.".format(r, c))
                    return False
                elif maze[r][c] == EXIT:
                    print("GRATZ!")
                    return True
                else:
                    player = r, c
                    step += 1

    assert checker(find_path, (1, 1), [
        "XXXXXXXXXXXX",
        "X..........X",
        "X.XXXXXXXX.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.XXXXXXXX.X",
        "X.........EX",
        "XXXXXXXXXXXX",
    ]), "Simple"
    assert checker(find_path, (1, 4), [
        "XXXXXXXXXXXX",
        "XX...X.....X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "XE.X.....X.X",
        "XXXXXXXXXXXX",
    ]), "Up Down"
    assert checker(find_path, (10, 10), [
        "XXXXXXXXXXXX",
        "X.X.XX.X.X.X",
        "X..........X",
        "X.XXXXXXXX.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X......X.X",
        "X.X..E...X.X",
        "X.X......X.X",
        "X.XXXX.XXX.X",
        "X..........X",
        "XXXXXXXXXXXX",
    ]), "Left"

