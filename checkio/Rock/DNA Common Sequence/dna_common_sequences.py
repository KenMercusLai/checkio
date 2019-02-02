# please read the following article for algothmn explanation
# http://wordaligned.org/articles/longest-common-subsequence


def common(first, second):
    dp_rec = [[('', )] * (len(second) + 1) for i in range(len(first) + 1)]
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            # same ending
            if first[i - 1] == second[j - 1]:
                dp_rec[i][j] = tuple((s + first[i - 1])
                                     for s in dp_rec[i - 1][j - 1])
            # otherwise depend on LCS size
            else:
                lcs_left_len = len(dp_rec[i][j - 1][0])
                lcs_up_len = len(dp_rec[i - 1][j][0])
                if lcs_left_len == lcs_up_len:
                    # remove duplicates
                    dp_rec[i][j] = tuple(set(dp_rec[i][j - 1]
                                             + dp_rec[i - 1][j]))
                elif lcs_left_len > lcs_up_len:
                    dp_rec[i][j] = dp_rec[i][j - 1]
                else:
                    dp_rec[i][j] = dp_rec[i - 1][j]
    return ','.join(sorted(dp_rec[-1][-1]))


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"
