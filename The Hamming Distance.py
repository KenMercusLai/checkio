def checkio(n, m):
    binN = bin(n)[2:]
    binM = bin(m)[2:]
    if len(binN) > len(binM):
        binM = binM.zfill(len(binN))
    else:
        binN = binN.zfill(len(binM))
    counter = 0
    for i in range(len(binN)):
        if binN[i] != binM[i]:
            counter += 1
    return counter

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
