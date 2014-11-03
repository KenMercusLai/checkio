import heapq


def shortestPath(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while True:
        (cost, v, path) = heapq.heappop(queue)
        if v not in seen:
            path = path + [v]
            seen.add(v)
            if v == end:
                return cost, path
            for (next, c) in graph[v].iteritems():
                heapq.heappush(queue, (cost + c, next, path))
    return queue


def build_network(matrix, TargetNumber):
    MatrixDict = {}
    neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    matrix = [tuple(['X']) + i + tuple(['X']) for i in matrix]
    matrix = [tuple(['X'] * len(matrix[0]))] \
        + matrix \
        + [tuple(['X'] * len(matrix[0]))]
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            if matrix[i + 1][j + 1] == TargetNumber:
                if (i, j) not in MatrixDict:
                    MatrixDict[(i, j)] = {}
                for k in neighbors:
                    if matrix[i + 1 + k[0]][j + 1 + k[1]] == TargetNumber:
                        MatrixDict[(i, j)][(i + k[0], j + k[1])] = 1
    return MatrixDict


def can_pass(matrix, first, second):
    TargetNumber = matrix[first[0]][first[1]]
    try:
        shortestPath(build_network(matrix, TargetNumber), first, second)
        return True
    except:
        return False


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) is True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) is False, 'First example'
