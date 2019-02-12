import unittest

from auto_painting import checkio


def check_solution(func, k, n, max_steps):
    result = func(k, n)
    actions = result.split(",")
    if len(actions) > max_steps:
        print("It can be shorter.")
        return False
    details = [0] * n
    for act in actions:
        if len(act) > k:
            print("The system can contain {0} detail(s).".format(k))
            return False
        if len(set(act)) < len(act):
            print("You can not place one detail twice in one load")
            return False
        for ch in act:
            details[int(ch)] += 1
    if any(d < 2 for d in details):
        print("I see no painted details.")
        return False
    if any(d > 2 for d in details):
        print("I see over painted details.")
        return False
    return True


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [2, 3], "answer": [3, 2, 3]},
            {"input": [6, 3], "answer": [2, 3, 3]},
            {"input": [3, 6], "answer": [4, 3, 6]},
            {"input": [1, 4], "answer": [8, 1, 4]},
            {"input": [2, 5], "answer": [5, 2, 5]},
        ],
        "Extra": [
            {"input": [1, 7], "answer": [14, 1, 7]},
            {"input": [2, 7], "answer": [7, 2, 7]},
            {"input": [2, 8], "answer": [8, 2, 8]},
            {"input": [2, 9], "answer": [9, 2, 9]},
            {"input": [3, 4], "answer": [3, 3, 4]},
            {"input": [4, 4], "answer": [2, 4, 4]},
            {"input": [4, 6], "answer": [3, 4, 6]},
            {"input": [5, 3], "answer": [2, 5, 3]},
        ],
        "Extra2": [
            {"input": [5, 6], "answer": [3, 5, 6]},
            {"input": [6, 9], "answer": [3, 6, 9]},
            {"input": [7, 9], "answer": [3, 7, 9]},
            {"input": [8, 9], "answer": [3, 8, 9]},
            {"input": [10, 10], "answer": [2, 10, 10]},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert check_solution(checkio, i['input'][0], i['input'][1], i['answer'][0])

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert check_solution(checkio, i['input'][0], i['input'][1], i['answer'][0])

    def test_Extra2(self):
        for i in self.TESTS['Extra2']:
            assert check_solution(checkio, i['input'][0], i['input'][1], i['answer'][0])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
