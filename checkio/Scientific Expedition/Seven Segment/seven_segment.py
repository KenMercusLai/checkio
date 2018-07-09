from itertools import combinations


SEGMENTS = [{'a', 'b', 'c', 'd', 'e', 'f'},
            {'b', 'c'},
            {'a', 'b', 'g', 'e', 'd'},
            {'a', 'b', 'g', 'c', 'd'},
            {'b', 'c', 'g', 'f'},
            {'a', 'c', 'd', 'f', 'g'},
            {'a', 'c', 'd', 'e', 'f', 'g'},
            {'a', 'b', 'c'},
            {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            {'a', 'b', 'c', 'd', 'f', 'g'}]


def possible_numbers(lit_seg, broken_seg, digit_sets):
    lit = [i.lower() for i in lit_seg if i in digit_sets]
    broken = [i.lower() for i in broken_seg if i in digit_sets]
    numbers = []
    for i, v in enumerate(SEGMENTS):
        for combin_len in range(len(broken) + 1):
            for j in combinations(broken, combin_len):
                if v == set(sorted(lit + list(j))):
                    numbers.append(i)
    return numbers


def seven_segment(lit_seg, broken_seg):
    first_digit = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    second_digit = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    first = possible_numbers(lit_seg, broken_seg, first_digit)
    second = possible_numbers(lit_seg, broken_seg, second_digit)

    return len(first) * len(second)


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'},
                         {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'},
                         {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'},
                         {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
