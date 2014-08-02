from itertools import combinations, tee
from copy import deepcopy


def mindCheck(mindStatus):
    return all([i == mindStatus[i] for i in mindStatus])


def search(mindStatus, switches):
    s1, s2 = tee(switches)
    for i in s1:
        mindStatusCopy = deepcopy(mindStatus)
        mindStatusCopy[i[0]], mindStatusCopy[
            i[1]] = mindStatusCopy[i[1]], mindStatusCopy[i[0]]
        if mindCheck(mindStatusCopy):
            return [i]
        s2, s3 = tee(switches)
        aaa = [j for j in s2 if j != i]
        ret = search(mindStatusCopy, aaa)
        if ret:
            return [i] + ret
    return None


def mind_switcher(journal):
    # get all robots
    robots = []
    for i in journal:
        robots += list(i)
    robots += ['sophia', 'nikola']
    robots = list(set(robots))
    mindStatus = {}
    for i in robots:
        mindStatus[i] = i
    for i in journal:
        i = list(i)
        mindStatus[i[0]], mindStatus[i[1]] = mindStatus[i[1]], mindStatus[i[0]]

    # get all possible switches
    def allSwitches():
        for i in combinations(robots, 2):
            if set(i) not in journal:
                yield i
    switchProcesses = search(mindStatus, allSwitches())
    return tuple([{i[0], i[1]} for i in switchProcesses])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    def check_solution(func, data):
        robots = {"nikola": "nikola", "sophia": "sophia"}
        switched = []
        for pair in data:
            switched.append(set(pair))
            r1, r2 = pair
            robots[r1], robots[r2] = robots.get(r2, r2), robots.get(r1, r1)

        result = func(data)
        if not isinstance(result, (list, tuple)) or not all(isinstance(p, set) for p in result):
            print("The result should be a list/tuple of sets.")
            return False
        for pair in result:
            if len(pair) != 2:
                print(1, "Each pair should contain exactly two names.")
                return False
            r1, r2 = pair
            if not isinstance(r1, str) or not isinstance(r2, str):
                print("Names must be strings.")
                return False
            if r1 not in robots.keys():
                print("I don't know '{}'.".format(r1))
                return False
            if r2 not in robots.keys():
                print("I don't know '{}'.".format(r2))
                return False
            if set(pair) in switched:
                print("'{}' and '{}' already were switched.".format(r1, r2))
                return False
            switched.append(set(pair))
            robots[r1], robots[r2] = robots[r2], robots[r1]
        for body, mind in robots.items():
            if body != mind:
                print("'{}' has '{}' mind.".format(body, mind))
                return False
        return True

    assert check_solution(mind_switcher, ({"scout", "super"},))
    assert check_solution(
        mind_switcher, ({'hater', 'scout'}, {'planer', 'hater'}))
    # assert check_solution(mind_switcher, ({'scout', 'driller'},
    #                                       {'scout', 'lister'},
    #                                       {'hater', 'digger'},
    #                                       {'planer', 'lister'},
    #                                       {'super', 'melter'}))
