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


class RobotSortPuzzle(AStar):

    def __init__(self, Goal):
        super(RobotSortPuzzle, self).__init__(Goal)

    def Heuristic(self, Node):
        return sum([i * 2 for i, j in enumerate(self.Goal)
                    if Node.Status[i] != j])

    def GetResult(self, Node):
        Result = ''
        while Node.Parent:
            Result = Node.Comment + ',' + Result
            print Node.Comment, Node.Status
            Node = Node.Parent
        return Result


class RobotSortPuzzleNode(AStarNode):

    def __init__(self, Status, G, Parent):
        super(RobotSortPuzzleNode, self).__init__(Status, G, Parent)

    def PossibleNextNodes(self):
        result = []
        for i in range(len(self.Status) - 1):
            temp = deepcopy(self.Status)
            temp[i], temp[i + 1] = temp[i + 1], temp[i]
            newNode = RobotSortPuzzleNode(temp,
                                          self.G + 1, self)
            newNode.Comment = str(i) + str(i + 1)
            result.append(newNode)
        return result


def swapsort(array):
    Puzzle = RobotSortPuzzle(sorted(array))
    startNode = RobotSortPuzzleNode(list(array), 0, None)
    return Puzzle.Search(startNode)[:-1]


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
