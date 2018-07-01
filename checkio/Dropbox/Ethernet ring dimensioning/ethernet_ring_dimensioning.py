from math import ceil


ETHERNET = (100, 40, 10, 1, 0.1)  # Ethernet bandwidth capacity in Gbps


def generate_path(ring, start, end):
    # generate the shortest path from start to end.

    # according to the task, the preference path in order is:
    # 1. from start to end following the ring order if it's the shortest
    # 2. from start to end following in the reversed ring order
    # if it's the shortest
    # 3. from end to start following in the ring order if it's the shortest

    start_index = ring.index(start)
    end_index = ring.index(end)

    ring_chain = ring + ring
    if start_index < end_index:
        path = ring[start_index:end_index + 1]
        if len(path) * 2 > len(ring) + 2:
            path = ring_chain[end_index:start_index + len(ring) + 1]
            path = path[::-1]
    else:
        path = ring[end_index:start_index + 1]
        if len(path) * 2 == len(ring) + 2:
            path = ring_chain[start_index:end_index + len(ring) + 1]
        elif len(path) * 2 > len(ring) + 2:
            path = ring_chain[start_index:end_index + len(ring) + 1]
            path = path[::-1]
    return path


def segment_bandwidth(ring, flows):
    ring_segments = (list(map(lambda x: x[0] + x[1], zip(ring, ring[1:])))
                     + [ring[-1] + ring[0]])
    path_segments = {i: 0 for i in ring_segments}
    for i in flows:
        start, end, bandwidth = i[0][0], i[0][1], i[1]
        path = generate_path(ring, start, end)
        shortest_path_segments = map(lambda x: x[0] + x[1], zip(path, path[1:]))
        for j in shortest_path_segments:
            try:
                path_segments[j] += bandwidth
            except KeyError:
                path_segments[j[::-1]] += bandwidth
    return path_segments


def checkio(ring, *flows):
    result = [0, 0, 0, 0, 0]
    for i in sorted(segment_bandwidth(ring, flows).values(), reverse=True):
        if i > 40:
            result[0] += ceil(i / 100)
        elif i > 10:
            result[1] += 1
        elif i > 1:
            result[2] += 1
        elif i > 0.1:
            result[3] += 1
        elif i > 0:
            result[4] += 1
    return result


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" are used only for self-checking and not necessary for
    # auto-testing
    assert checkio("AEFCBG",
                   ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]
    assert checkio("ABCDEFGH", ["AD", 4], ["DA", 4]) == [0, 0, 3, 0, 0]
