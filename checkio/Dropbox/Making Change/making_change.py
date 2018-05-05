import heapq
from collections import defaultdict


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
            for (next_item, c) in graph[v].items():
                heapq.heappush(queue, (cost + c, next_item, path))
    return queue


def checkio(price, denominations):
    conn = defaultdict(dict)
    open_number = set([price])
    closed_number = set([])
    while open_number:
        current = open_number.pop()
        closed_number.add(current)
        for i in denominations:
            if current - i >= 0:
                conn[current][current - i] = 1
                if current - i == 0:
                    conn[0][current] = 1
                if current - i not in closed_number:
                    open_number.add(current - i)
    if conn and 0 in conn:
        steps, numbers = shortestPath(conn, price, 0)
    else:
        return None
    return steps


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    print('Done')
