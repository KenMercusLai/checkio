from itertools import combinations
from copy import deepcopy

POSSIBLE_ELEMENTS = 'ATCG'


def findall(sequence, start_index, target):
    return [i for i in range(start_index, len(sequence)) if sequence[i] == target]


def common(first, second):
    results = []
    longer_result = 1
    while longer_result:
        longer_result = []
        print('--------')
        print(len(results))
        if results:
            for j in results:
                if j[0][-1] == len(first) - 1 or j[1][-1] == len(second) - 1:
                    continue
                for target in POSSIBLE_ELEMENTS:
                    index_of_first = findall(first, j[0][-1] + 1, target)
                    index_of_second = findall(second, j[1][-1] + 1, target)
                    for i_first in index_of_first:
                        for i_second in index_of_second:
                            longer_result.append((j[0] + [i_first], j[1] + [i_second]))
                    print(len(longer_result))
        else:
            for i in POSSIBLE_ELEMENTS:
                index_of_first = findall(first, 0, i)
                index_of_second = findall(second, 0, i)
                for j in index_of_first:
                    for k in index_of_second:
                        longer_result.append(([j], [k]))
        if longer_result:
            results = deepcopy(longer_result)

    # translate indexes into chars
    sequences = []
    for i in results:
        sequences.append(''.join([first[j] for j in i[0]]))
    print(','.join(sorted(list(set(sequences)))))
    return ','.join(sorted(list(set(sequences))))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"
    assert common('TTGGTGTCGCTAGACC', 'CGCTAGTGGGGAAT') == 'TTGGGGAA'
    common('AACGTTTTGGGTTTAGAGAAAGTGCTCACAGTAGGTACGTCCCCCAGACCCCACGCCAATGTAT',
           'TTTGGGAATGCAATTTAGCTCACAGAGCATACAATGAGAACCACCGAGATCATATTAAGTCTCC') == 'TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATTAT'
