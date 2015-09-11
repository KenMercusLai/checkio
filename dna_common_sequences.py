from itertools import combinations
from copy import deepcopy

POSSIBLE_ELEMENTS = 'ATCG'


def findfirst(sequence, start_index, target):
    for i in range(start_index, len(sequence)):
        if sequence[i] == target:
            return [i]
    return []


def common(first, second):
    results = []
    new_result_counter = 1
    while new_result_counter:
        new_result_counter = 0
        print('--------')
        print(len(results))
        if results:
            for j in range(len(results)):
                # if j[0][-1] == len(first) - 1 or j[1][-1] == len(second) - 1:
                #     continue
                # print(j)
                for target in POSSIBLE_ELEMENTS:
                    # print(target)
                    index_of_first = findfirst(
                        first, results[j][0][-1] + 1, target)
                    index_of_second = findfirst(
                        second, results[j][1][-1] + 1, target)

                    for i_first in index_of_first:
                        for i_second in index_of_second:
                            results.append((results[j][0] + [i_first],
                                            results[j][1] + [i_second]))
                            new_result_counter += 1
                # print((new_result_counter))
                # input()
        else:
            for i in POSSIBLE_ELEMENTS:
                index_of_first = findfirst(first, 0, i)

                index_of_second = findfirst(second, 0, i)

                for j in index_of_first:
                    for k in index_of_second:
                        results.append(([j], [k]))
                        new_result_counter += 1
        if new_result_counter:
            results = results[-new_result_counter:]

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
    assert common('GGAGTACCATGGGCGGGACGTCACAGCCCCCAACTCA', 'AAGGTGACGCAAATGGTATATTCGCTAAGGATT') == 'AGTACCATGGACGCAAGAT,AGTACCATGGACGTAAGAT,AGTACCATGGATACGCAAA,AGTACCATGGATACGCAAT,AGTACCATGGCGCTAAGAT,GGGACCATGGACGCAAGAT,GGGACCATGGACGTAAGAT,GGGACCATGGATACGCAAA,GGGACCATGGATACGCAAT,GGGACCATGGCGCTAAGAT,GGTACCATGGACGCAAGAT,GGTACCATGGACGTAAGAT,GGTACCATGGATACGCAAA,GGTACCATGGATACGCAAT,GGTACCATGGCGCTAAGAT'
    assert common('AACGTTTTGGGTTTAGAGAAAGTGCTCACAGTAGGTACGTCCCCCAGACCCCACGCCAATGTAT',
           'TTTGGGAATGCAATTTAGCTCACAGAGCATACAATGAGAACCACCGAGATCATATTAAGTCTCC') == 'TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATTAT'
