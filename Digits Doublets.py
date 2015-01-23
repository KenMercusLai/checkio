import heapq


def shortest_path(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while True:
        (cost, v, path) = heapq.heappop(queue)
        if v not in seen:
            path = path + [v]
            seen.add(v)
            if v == end:
                return cost, path
            for (next_item, c) in graph[v].iteritems():
                heapq.heappush(queue, (cost + c, next_item, path))
    return queue


def checkio(numbers):
    number_dict = {}
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if len([k for k in zip(str(numbers[i]), str(numbers[j]))
                    if k[0] != k[1]]) == 1:
                if numbers[i] not in number_dict:
                    number_dict[numbers[i]] = {}
                if numbers[j] not in number_dict:
                    number_dict[numbers[j]] = {}
                number_dict[numbers[i]][numbers[j]] = 1
                number_dict[numbers[j]][numbers[i]] = 1
    return shortest_path(number_dict, numbers[0], numbers[-1])[1]

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [
        123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [
        111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [
        456, 454, 654], "Third, [456, 656, 654] is correct too"
