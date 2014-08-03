from copy import deepcopy
GOAL = (1, 2, 1, 0, 2, 0, 0, 3, 0, 4, 3, 4)


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


class EigthyEighthPuzzle(AStar):

    def __init__(self, Goal):
        super(EigthyEighthPuzzle, self).__init__(Goal)

    def Heuristic(self, Node):
        # return 0
        return sum([1 for i, j in enumerate(Node.Status)
                    if i not in [3, 5, 6, 8] and GOAL[i] != j])

    def GetResult(self, Node):
        Result = ''
        while Node.Parent:
            Result = Node.Comment + Result
            Node = Node.Parent
        return Result


class EigthyEighthPuzzleNode(AStarNode):

    def __init__(self, Status, G, Parent):
        super(EigthyEighthPuzzleNode, self).__init__(Status, G, Parent)

    def PossibleNextNodes(self):
        result = []

        # rotate 1
        tempList = list(deepcopy(self.Status))
        tempList[0], tempList[2], tempList[3], tempList[
            5] = tempList[2], tempList[5], tempList[0], tempList[3]
        newNode = EigthyEighthPuzzleNode(tuple(tempList), self.G + 1, self)
        newNode.Comment = '1'
        result.append(newNode)
        # rotate 2
        tempList = list(deepcopy(self.Status))
        tempList[1], tempList[3], tempList[4], tempList[
            6] = tempList[3], tempList[6], tempList[1], tempList[4]
        newNode = EigthyEighthPuzzleNode(tuple(tempList), self.G + 1, self)
        newNode.Comment = '2'
        result.append(newNode)
        # rotate 3
        tempList = list(deepcopy(self.Status))
        tempList[5], tempList[7], tempList[8], tempList[
            10] = tempList[7], tempList[10], tempList[5], tempList[8]
        newNode = EigthyEighthPuzzleNode(tuple(tempList), self.G + 1, self)
        newNode.Comment = '3'
        result.append(newNode)
        # rotate 4
        tempList = list(deepcopy(self.Status))
        tempList[6], tempList[8], tempList[9], tempList[
            11] = tempList[8], tempList[11], tempList[6], tempList[9]
        newNode = EigthyEighthPuzzleNode(tuple(tempList), self.G + 1, self)
        newNode.Comment = '4'
        result.append(newNode)
        return result


def puzzle88(state):
    Puzzle = EigthyEighthPuzzle(GOAL)
    startNode = EigthyEighthPuzzleNode(state, 0, None)
    return Puzzle.Search(startNode)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert puzzle88((0, 2, 1, 3, 2, 1, 4, 0, 0, 4, 0, 3)) in (
        '1433', '4133'), "Example"
    assert puzzle88((0, 2, 1, 2, 0, 0, 4, 1, 0, 4, 3, 3)) in (
        '4231', '4321'), "Rotate all"
    assert puzzle88((0, 2, 1, 2, 4, 0, 0, 1, 3, 4, 3, 0)) in (
        '2314', '2341', '3214', '3241'), "Four paths"
