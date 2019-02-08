import unittest

from seven_segment import possible_numbers, seven_segment


def test_possible_numbers():
    first_digit = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    second_digit = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert possible_numbers({'B', 'C', 'b', 'c'}, {'A'}, first_digit) == [1, 7]
    assert possible_numbers({'B', 'C', 'b', 'c'}, {'A'}, second_digit) == [1]

    assert possible_numbers(
        {'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}, first_digit
    ) == [1, 3, 7]
    assert possible_numbers(
        {'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}, second_digit
    ) == [5, 6]


# class Tests(unittest.TestCase):
#     TESTS = {
#         "Basics": [
#             {
#                 "input": [['B', 'C', 'b', 'c'],
#                     ['A']],
#                 "answer": 2,
#             },
#             {
#                 "input": [['B', 'C', 'a', 'f', 'g', 'c', 'd'],
#                     ['A', 'G', 'D', 'e']],
#                 "answer": 6,
#             },
#             {
#                 "input": [['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'],
#                     ['G', 'g']],
#                 "answer": 4,
#             },
#             {
#                 "input": [['B', 'C', 'a', 'f', 'g', 'c', 'd'],
#                     ['A', 'G', 'D', 'F', 'b', 'e']],
#                 "answer": 20,
#             },
#             {
#                 "input": [['A', 'B', 'C', 'b', 'c', 'f', 'g'],
#                     ['G', 'd']],
#                 "answer": 1,
#             },
#             {
#                 "input": [[],
#                     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'a', 'b', 'c', 'd', 'e', 'f', 'g']],
#                 "answer": 100,
#             },
#         ],
#         # "Randoms": make_test(10),
#     }

#     def test_Basics(self):
#         for i in self.TESTS['Basics']:
#             assert seven_segment(*i['input']) == i['answer'], i['input']

#     # def test_Extra(self):
#     #     for i in self.TESTS['Extra']:
#     #         assert seven_segment(i['input']) == i['answer'], i['input']


# if __name__ == "__main__":  # pragma: no cover
#     unittest.main()
