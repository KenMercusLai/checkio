import unittest

from water_jars import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [5, 7, 6],
                "answer": ['02', '21', '10', '21', '02', '21', '10', '21', '02', '21']},
            {
                "input": [3, 4, 1],
                "answer": ['02', '21']},
            {
                "input": [2, 1, 1],
                "answer": ['02']},
            {
                "input": [8, 5, 2],
                "answer": ['02', '21', '02', '21']},
            {
                "input": [9, 8, 7],
                "answer": ['02', '21', '02', '21']},
            {
                "input": [8, 10, 4],
                "answer": ['02', '21', '10', '21', '02', '21']},
            {
                "input": [2, 7, 1],
                "answer": ['02', '21', '10', '21', '10', '21']},
            {
                "input": [5, 8, 7],
                "answer": ['01', '12', '01', '12', '20', '12', '01', '12']},
        ],
        "Extra": [
            {
                "input": [9, 1, 6],
                "answer": ['01', '12', '20', '12', '20', '12']},
            {
                "input": [7, 2, 4],
                "answer": ['02', '21', '02', '21']},
            {
                "input": [8, 1, 4],
                "answer": ['01', '12', '20', '12', '20', '12', '20', '12']}
        ]
    }

    def check_solution(self, func, initial_data, max_steps):
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

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert self.check_solution(checkio, i['input'], len(i['answer']))

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert self.check_solution(checkio, i['input'], len(i['answer']))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
