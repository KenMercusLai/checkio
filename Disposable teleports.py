from copy import deepcopy


def FindPath(connection_dict, StartPoint):
    if StartPoint in connection_dict:
        if len(connection_dict) == 1:
            return connection_dict[StartPoint]
        else:
            ret = []
            for i in connection_dict[StartPoint]:
                NewConnectionDict = deepcopy(connection_dict)
                NewConnectionDict[StartPoint].remove(i)
                if not NewConnectionDict[StartPoint]:
                    del NewConnectionDict[StartPoint]
                NewConnectionDict[i].remove(StartPoint)
                if not NewConnectionDict[i]:
                    del NewConnectionDict[i]
                for j in FindPath(NewConnectionDict, i):
                    ret.append(i + j)
                # add this to mean i can stop here even I have path to go
                ret.append(i)
            return ret
    else:
        return ['']


def checkio(teleports_string):
    connections = teleports_string.split(',')
    connection_dict = {}
    for i in connections:
        if i[0] not in connection_dict:
            connection_dict[i[0]] = []
        if i[1] not in connection_dict:
            connection_dict[i[1]] = []
        connection_dict[i[0]].append(i[1])
        connection_dict[i[1]].append(i[0])
    path = FindPath(connection_dict, '1')
    path = map(lambda x: '1' + x, path)
    path = filter(lambda x: ('1' == x[-1]
                             and set(x) == set(connection_dict.keys())),
                  path)
    sorted(path, key=len, reverse=True)
    if path:
        return path[0]


# This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)]))
                         for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(
        checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(
        checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(
        checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"
