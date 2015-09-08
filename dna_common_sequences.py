from itertools import combinations
from copy import deepcopy
CACHE = {}


def generate_subsequences(sequence, length):
    if (sequence, length) in CACHE:
        return CACHE[(sequence, length)]
    result = []
    if len(sequence) == 1:
        return list(sequence)
    for i in range(len(sequence) - 1):
        if length > 1:
            result += [sequence[i] + j
                       for j in generate_subsequences(sequence[i + 1:], length - 1)]
        else:
            result = list(sequence)
            break
    result = [i for i in result if len(i) == length]
    CACHE[(sequence, length)] = result
    return result


def common(first, second):    
    # build common str matches at length 2
    result = {}
    for i in combinations(range(len(first)), 2):
        first_subsequence = [first[ii] for ii in i]
        for j in combinations(range(len(second)), 2):
            second_subsequence = [second[jj] for jj in j]
            if first_subsequence == second_subsequence:
                if i not in result:
                    result[i] = []
                result[i].append(j)

    longer_result = 1
    while longer_result:
        print(len(result))
        longer_result = {}
        for i in result:
            i = list(i)
            # remove unexpanable subsequences early
            if i[-1] == len(first) - 1:
                continue
            for j in result[tuple(i)]:
                j = list(j)
                if j[-1] == len(second) - 1:
                    continue

                # test combinations
                for expand_i in range(i[-1]+1, len(first)):
                    first_subsequence = [first[ii] for ii in i + [expand_i]]
                    for expand_j in range(j[-1]+1, len(second)):
                        second_subsequence = [second[jj] for jj in j + [expand_j]]
                        if first_subsequence == second_subsequence:
                            if tuple(i + [expand_i]) not in longer_result:
                                longer_result[tuple(i + [expand_i])] = []
                            longer_result[tuple(i + [expand_i])].append(tuple(j + [expand_j]))
        if longer_result:
            result = deepcopy(longer_result)
    print(result)
    final_result = []
    for i in result:
        final_result.append(''.join([first[j] for j in i]))
    return ','.join(sorted(final_result))
    

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"
    assert common('TTGGTGTCGCTAGACC', 'CGCTAGTGGGGAAT') == 'TTGGGGAA'
    common('AACGTTTTGGGTTTAGAGAAAGTGCTCACAGTAGGTACGTCCCCCAGACCCCACGCCAATGTAT', 'TTTGGGAATGCAATTTAGCTCACAGAGCATACAATGAGAACCACCGAGATCATATTAAGTCTCC') == 'TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATTAT'
