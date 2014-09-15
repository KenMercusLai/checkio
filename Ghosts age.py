def fib_to(n):
    fibs = [1, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def checkio(opacity):
    age = 0
    OpacityLeft = 10000
    FibNumbers = fib_to(20)
    while opacity != OpacityLeft:
        age += 1
        if age in FibNumbers:
            OpacityLeft -= age
        else:
            OpacityLeft += 1
    return age

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
