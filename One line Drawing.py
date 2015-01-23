import itertools
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
                if Node.Status in [i.Status for i in ClosedSet]:
                    continue
                if Node.Status in [i.Status for i in OpenSet]:
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

    def __init__(self, Status, G, Parent):
        self.G = G
        self.H = None
        self.Parent = Parent
        self.Status = Status
        self.Comment = None

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


class OneLineDrawingPuzzle(AStar):

    def __init__(self, Goal):
        super(OneLineDrawingPuzzle, self).__init__(Goal)

    def Heuristic(self, Node):
        return sum([1 for i in Node.Status if Node.Status[i] != self.Goal[i]])

    def GetResult(self, Node):
        Result = []
        while Node.Parent:
            Result = [Node.Comment] + Result
            Node = Node.Parent
        Result = [Node.Comment] + Result
        return Result


class OneLineDrawingPuzzleNode(AStarNode):

    def __init__(self, Status, G, Parent):
        super(OneLineDrawingPuzzleNode, self).__init__(Status, G, Parent)

    def PossibleNextNodes(self):
        result = []
        for i in self.Status:
            x1, y1, x2, y2 = i
            if self.Status[i] == 0:
                if (x1, y1) == self.Comment or (x2, y2) == self.Comment:
                    tempStatus = deepcopy(self.Status)
                    tempStatus[i] = 1
                    newNode = OneLineDrawingPuzzleNode(
                        tempStatus, self.G + 1, self)
                    if (x1, y1) == self.Comment:
                        newNode.Comment = (x2, y2)
                    else:
                        newNode.Comment = (x1, y1)
                    result.append(newNode)
        return result


def CanBeDrawInOneLine(segments):
    points = []
    for i in segments:
        points.append((i[0], i[1]))
        points.append((i[2], i[3]))
    pointCount = [(i, len([k for k in j]))
                  for i, j in itertools.groupby(sorted(points))]
    OddPoints = filter(lambda x: x[1] % 2 != 0, pointCount)
    return OddPoints


def draw(segments):
    OddPoints = CanBeDrawInOneLine(segments)
    # 0 or 2 odd points, else cannot be drawn by one line
    if len(OddPoints) in [2, 0]:
        GOAL = {}
        state = {}
        for i in segments:
            GOAL[i] = 1
            state[i] = 0
        puzzle = OneLineDrawingPuzzle(GOAL)
        start_node = OneLineDrawingPuzzleNode(state, 0, None)
        if len(OddPoints) == 2:
            start_node.Comment = OddPoints[0][0]
        else:
            start_node.Comment = (i[0], i[1])
        ret = puzzle.Search(start_node)
        return ret
    return []


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    def checker(func, in_data, is_possible=True):
        user_result = func(in_data)
        if not is_possible:
            if user_result:
                print("How did you draw this?")
                return False
            else:
                return True
        if len(user_result) < 2:
            print("More points please.")
            return False
        data = list(in_data)
        for i in range(len(user_result) - 1):
            f, s = user_result[i], user_result[i + 1]
            if (f + s) in data:
                data.remove(f + s)
            elif (s + f) in data:
                data.remove(s + f)
            else:
                print("The wrong segment {}.".format(f + s))
                return False
        if data:
            print("You forgot about {}.".format(data[0]))
            return False
        return True

    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2),
                    (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
                    (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2),
                    (7, 5, 1, 2)}, False), "Example 2"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2),
                    (1, 5, 4, 7), (4, 7, 7, 5),
                    (7, 5, 7, 2), (1, 5, 7, 2),
                    (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
