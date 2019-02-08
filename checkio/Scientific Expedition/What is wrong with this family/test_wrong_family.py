import unittest

from wrong_family import is_family, merge_members


def test_merge_members():
    group = [[1], [2], [3]]
    assert merge_members(group, 1, 2) == [[1, 2], [3]]
    group = [[1], [2], [3]]
    assert merge_members(group, 1, 3) == [[1, 3], [2]]

    group = [[1], [2], [3, 4]]
    assert merge_members(group, 1, 2) == [[3, 4], [1, 2]]
    group = [[1], [2], [3, 4]]
    assert merge_members(group, 1, 3) == [[1, 3, 4], [2]]
    group = [[1], [2], [3, 4]]
    assert merge_members(group, 1, 4) == [[1, 3, 4], [2]]

    group = [[1, 2], [3, 4]]
    assert merge_members(group, 1, 4) == [[1, 2, 3, 4]]

    # same group
    group = [[1, 2], [3]]
    assert merge_members(group, 1, 2) == [[1, 2], [3]]

    # failed case
    group = [[1], [2], [3]]
    assert merge_members(group, 1, 4) == [[1], [2], [3]]


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [
                    ['Logan', 'Mike']
                ],
                "answer": True,
                "explanation": "One father, one son"
            },
            {
                "input": [
                    ['Logan', 'Mike'],
                    ['Logan', 'Jack']
                ],
                "answer": True,
                "explanation": "Two sons"
            },
            {
                "input": [
                    ['Logan', 'Mike'],
                    ['Logan', 'Jack'],
                    ['Mike', 'Alexander']
                ],
                "answer": True,
                "explanation": "Grandfather"
            },
            {
                "input": [
                    ['Logan', 'Mike'],
                    ['Logan', 'Jack'],
                    ['Mike', 'Logan']
                ],
                "answer": False,
                "explanation": "Can you be a father for your father?"
            },
            {
                "input": [
                    ['Logan', 'Mike'],
                    ['Logan', 'Jack'],
                    ['Mike', 'Jack']
                ],
                "answer": False,
                "explanation": "Can you be a father for your brother?"
            },
            {
                "input": [
                    ['Logan', 'William'],
                    ['Logan', 'Jack'],
                    ['Mike', 'Alexander']
                ],
                "answer": False,
                "explanation": "Looks like Mike is stranger in Logan's family"
            }
        ],
        "Extra": [
            {
                "input": [
                    ['Logan', 'William'],
                    ['Logan', 'Jack'],
                    ['Mike', 'Mike']
                ],
                "answer": False,
                "explanation": "Can you be a father for yourself?"
            },
            {
                "input": [
                    ['Logan', 'William'],
                    ['William', 'Jack'],
                    ['Jack', 'Mike'],
                    ['Mike', 'Alexander']
                ],
                "answer": True,
                "explanation": "Long family"
            },
            {
                "input": [
                    ['Logan', 'William'],
                    ['Mike', 'Alexander'],
                    ['William', 'Alexander']
                ],
                "answer": False,
                "explanation": "Who's Your Daddy?"
            },
            {
                "input": [
                    ['Logan', 'Mike'],
                    ['Alexander', 'Jack'],
                    ['Jack', 'Alexander']
                ],
                "answer": False,
                "explanation": "Can you be a father of your father?"
            },
            {
                "input": [
                    ['Logan', 'Mike'],
                    ['Alexander', 'Jack'],
                    ['Jack', 'Logan']
                ],
                "answer": True,
                "explanation": "Family connections can be listed in any directions"
            },
            {
                "input": [
                    ['Logan', 'Mike'],
                    ['Alexander', 'Jack'],
                    ['Jack', 'Logan'],
                    ['Alex', 'Bob']
                ],
                "answer": False,
                "explanation": "It's complex. You can not be a father of your grandfather and Alex is not in Logan's Family."
            },
            {
                "input": [
                    ['Logan', 'Mike'],
                    ['Alexander', 'Jack'],
                    ['Mike', 'Alexander']
                ],
                "answer": True,
                "explanation": "Grandfather, Father, Son."
            },
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert is_family(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert is_family(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
