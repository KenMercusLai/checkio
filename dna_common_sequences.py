def generate_subsequences(sequence, length):
    result = []
    if len(sequence) == 1:
        return list(sequence)
    for i in range(len(sequence) - 1):
        if length > 1:
            result += [sequence[i] +
                       j for j in generate_subsequences(sequence[i + 1:], length - 1)]
        else:
            return list(sequence)
    result = [i for i in result if len(i) == length]
    return result


def common(first, second):
    max_common_length = min(len(first), len(second))
    for sequence_length in range(max_common_length, 1, -1):
        first_set = set(generate_subsequences(first, sequence_length))
        second_set = set(generate_subsequences(second, sequence_length))
        intersection = first_set.intersection(second_set)
        if intersection:
            return ','.join(sorted(intersection))
    return ""

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"
