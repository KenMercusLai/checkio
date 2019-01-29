gFirst = 0
gSecond = 0


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
            if self.Goal(Current.Status):
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
            print(self.G)
            print(self.H)
            print(self.Parent)
            print(self.Status)
            print(self.Comment)
            assert 1 == 0

    def PossibleNextNodes(self):
        raise NotImplementedError


class WaterJarPuzzle(AStar):

    def __init__(self, Goal):
        super(WaterJarPuzzle, self).__init__(Goal)

    def Heuristic(self, Node):
        return 0

    def GetResult(self, Node):
        Result = []
        while Node.Parent:
            Result.insert(0, Node.Comment)
            Node = Node.Parent
        return Result


class WaterJarPuzzleNode(AStarNode):

    def __init__(self, Status, G, Parent):
        super(WaterJarPuzzleNode, self).__init__(Status, G, Parent)

    def PossibleNextNodes(self):
        result = []
        # empty first
        NewNode = WaterJarPuzzleNode((0, self.Status[1]), self.G + 1, self)
        NewNode.Comment = '10'
        result.append(NewNode)
        # empty second
        NewNode = WaterJarPuzzleNode((self.Status[0], 0), self.G + 1, self)
        NewNode.Comment = '20'
        result.append(NewNode)
        # fill first jar
        if self.Status[0] < gFirst:
            NewNode = WaterJarPuzzleNode((gFirst, self.Status[1]),
                                         self.G + 1, self)
            NewNode.Comment = '01'
            result.append(NewNode)
        # fill second jar
        if self.Status[1] < gSecond:
            NewNode = WaterJarPuzzleNode((self.Status[0], gSecond),
                                         self.G + 1, self)
            NewNode.Comment = '02'
            result.append(NewNode)
        # first -> second
        if self.Status[1] < gSecond:
            if (gSecond - self.Status[1]) >= self.Status[0]:
                NewNode = WaterJarPuzzleNode((0, sum(self.Status)),
                                             self.G + 1, self)
            else:
                NewNode = WaterJarPuzzleNode((self.Status[0] - (gSecond - self.Status[1]), gSecond),
                                             self.G + 1, self)
            NewNode.Comment = '12'
            result.append(NewNode)
        # second -> first
        if self.Status[0] < gFirst:
            if (gFirst - self.Status[0]) >= self.Status[1]:
                NewNode = WaterJarPuzzleNode((sum(self.Status), 0),
                                             self.G + 1, self)
            else:
                NewNode = WaterJarPuzzleNode((gFirst, self.Status[1] - (gFirst - self.Status[0])),
                                             self.G + 1, self)
            NewNode.Comment = '21'
            result.append(NewNode)
        return result


def checkio(first, second, goal):
    global gFirst, gSecond
    gFirst = first
    gSecond = second
    Puzzle = WaterJarPuzzle(lambda x, g=goal: g in x)
    startNode = WaterJarPuzzleNode((0, 0), 0, None)
    return Puzzle.Search(startNode)


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for
    # auto-testing
    def check_solution(func, initial_data, max_steps):
        first_volume, second_volume, goal = initial_data
        actions = {
            "01": lambda f, s: (first_volume, s),
            "02": lambda f, s: (f, second_volume),
            "12": lambda f, s: (
                f - (second_volume - s if f > second_volume - s else f),
                second_volume if f > second_volume - s else s + f),
            "21": lambda f, s: (
                first_volume if s > first_volume - f else s + f,
                s - (first_volume - f if s > first_volume - f else s),
            ),
            "10": lambda f, s: (0, s),
            "20": lambda f, s: (f, 0)
        }
        first, second = 0, 0
        result = func(*initial_data)
        if len(result) > max_steps:
            print("You answer contains too many steps. It can be shorter.")
            return False
        for act in result:
            if act not in actions.keys():
                print("I don't know this action {0}".format(act))
                return False
            first, second = actions[act](first, second)
        if goal == first or goal == second:
            return True
        print("You did not reach the goal.")
        return False

    assert check_solution(checkio, (5, 7, 6), 10), "Example"
    assert check_solution(checkio, (3, 4, 1), 2), "One and two"
