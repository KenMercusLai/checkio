from itertools import permutations
from math import hypot
def golf(h):
    d = []
    for i in [i for i in permutations(h)]:
        d.append(hypot(i[0][0],i[0][1])+sum([hypot(i[j][0]-i[j+1][0],i[j][1]-i[j+1][1]) for j in range(len(i) - 1)]))
    return round(min(d), 2)

print golf({(2, 2), (2, 8), (8, 8), (5, 5), (8, 2)})
