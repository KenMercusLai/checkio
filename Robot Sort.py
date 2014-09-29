import heapq
from itertools import permutations
from copy import deepcopy


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


def swapsort(array):
    if list(array) == sorted(array):
        return ''
    DistanceMetrics = {}
    Status = set()
    for i in permutations(array, len(array)):
        Status.add(i)
    Status = list(Status)
    for i in Status:
        if i not in DistanceMetrics:
            DistanceMetrics[str(i)] = {}
        for j in range(len(i) - 1):
            temp = list(deepcopy(i))
            temp[j], temp[j + 1] = temp[j + 1], temp[j]
            temp = tuple(temp)
            DistanceMetrics[str(i)][str(temp)] = 1
    steps = shortestPath(DistanceMetrics,
                         str(array), str(tuple(sorted(array))))[-1]
    result = []
    for i, j in zip(steps, steps[1:]):
        i = eval(i)
        j = eval(j)
        for k in range(len(i)):
            if i[k] != j[k]:
                result.append(str(k) + str(k + 1))
                break
    print ','.join(result)
    return ','.join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    def check_solution(f, indata):
        result = f(indata)
        array = list(indata[:])
        la = len(array)
        if not isinstance(result, str):
            print("The result should be a string")
            return False
        actions = result.split(",") if result else []
        for act in actions:
            if len(act) != 2 or not act.isdigit():
                print("The wrong action: {}".format(act))
                return False
            i, j = int(act[0]), int(act[1])
            if i >= la or j >= la:
                print("Index error: {}".format(act))
                return False
            if abs(i - j) != 1:
                print("The wrong action: {}".format(act))
                return False
            array[i], array[j] = array[j], array[i]
        if len(actions) > (la * (la - 1)) // 2:
            print("Too many actions. BOOM!")
            return False
        if array != sorted(indata):
            print("The array is not sorted. BOOM!")
            return False
        return True

    assert check_solution(swapsort, (6, 4, 2)), "Reverse simple"
    assert check_solution(swapsort, (1, 2, 3, 4, 5)), "All right!"
    assert check_solution(swapsort, (1, 2, 3, 5, 3)), "One move"
    swapsort((1,2,3,4,5,6,7,8,9,1,))
