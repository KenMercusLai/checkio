def common(first, second):
    return ""

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"
