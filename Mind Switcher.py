from itertools import combinations
from copy import deepcopy


class AStar(object):

    def __init__(self, Goal):
        self.Goal = Goal

    def Heuristic(self, Node):
        raise NotImplementedError

    def GetResult(self, Node):
        raise NotImplementedError

    def Search(self, StartNode):
        OpenSet = set()
        ClosedSet = set()
        StartNode.H = self.Heuristic(StartNode)
        OpenSet.add(StartNode)
        while OpenSet:
            Current = min(OpenSet, key=lambda o: o.G + o.H)
            if Current.Status == self.Goal:
                return self.GetResult(Current)
            OpenSet.remove(Current)
            ClosedSet.add(Current)
            for Node in Current.PossibleNextNodes():
                if (Node.Status, Node.extras) in [(i.Status, i.extras) for i in ClosedSet]:
                    continue
                if (Node.Status, Node.extras) in [(i.Status, i.extras) for i in OpenSet]:
                    index = [i.Status for i in OpenSet].index(Node.Status)
                    if Node.G < list(OpenSet)[index].G:
                        list(OpenSet)[index].G = Node.G
                        list(OpenSet)[index].Parent = Node.Parent
                else:
                    Node.H = self.Heuristic(Node)
                    if Node.SelfCheck:
                        OpenSet.add(Node)
        return None


class AStarNode(object):

    def __init__(self, Status, G, Parent, extras=None):
        self.G = G
        self.H = None
        self.Parent = Parent
        self.Status = Status
        self.Comment = None
        self.extras = extras

    def SelfCheck(self):
        if self.G and self.H and self.Status:
            return True
        else:
            print self.G
            print self.H
            print self.Parent
            print self.Status
            print self.Comment
            assert 1 == 0

    def PossibleNextNodes(self):
        raise NotImplementedError


class MindSwitcherPuzzle(AStar):

    def __init__(self, Goal):
        super(MindSwitcherPuzzle, self).__init__(Goal)

    def Heuristic(self, Node):
        # return 0
        return sum([-2 for i in Node.Status if Node.Status[i] == i])

    def GetResult(self, Node):
        Result = []
        while Node.Parent:
            Result = [Node.Comment] + Result
            Node = Node.Parent
        return Result


class MindSwitcherPuzzleNode(AStarNode):

    def __init__(self, Status, G, Parent, extras):
        super(MindSwitcherPuzzleNode, self).__init__(Status, G, Parent, extras)

    def PossibleNextNodes(self):
        result = []
        for i in self.extras:
            mindStatusCopy = deepcopy(self.Status)
            mindStatusCopy[i[0]], mindStatusCopy[
                i[1]] = mindStatusCopy[i[1]], mindStatusCopy[i[0]]
            newNode = MindSwitcherPuzzleNode(mindStatusCopy,
                                             self.G + 1,
                                             self,
                                             [j for j in self.extras if j != i])
            newNode.Comment = i
            result.append(newNode)
        return result


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
    GOAL = deepcopy(mindStatus)
    for i in journal:
        i = list(i)
        mindStatus[i[0]], mindStatus[i[1]] = mindStatus[i[1]], mindStatus[i[0]]

    # get all possible switches
    allSwitches = [i for i in combinations(robots, 2) if set(i) not in journal]
    Puzzle = MindSwitcherPuzzle(GOAL)
    startNode = MindSwitcherPuzzleNode(mindStatus, 0, None, allSwitches)
    return tuple([{i[0], i[1]} for i in Puzzle.Search(startNode)])


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
    assert check_solution(mind_switcher, ({'scout', 'driller'},
                                          {'scout', 'lister'},
                                          {'hater', 'digger'},
                                          {'planer', 'lister'},
                                          {'super', 'melter'}))
