def fibgolf(s, u):
    if s == 'perrin' or s == 'tribonacci' or s == 'padovan':
        if s == 'perrin':
            a = 3
            b = 0
            c = 2
        else:
            a = 0
            b = 1
            c = 1
        i = 3
        while True:
            n = a + b
            if s == 'tribonacci':
                n += c
            if i == u:
                return n
            a = b
            b = c
            c = n
            i += 1
    else:
        if s == 'lucas':
            a = 2
        else:
            a = 0
        b = 1
        i = 2
        while True:
            n = a + b
            if s == 'pell':
                n += b
            elif s == 'jacobsthal':
                n += a
            if i == u:
                return n
            a = b
            b = n
            i += 1
if __name__ == '__main__':
    assert fibgolf('fibonacci', 10) == 55
    assert fibgolf('tribonacci', 10) == 149
    assert fibgolf('lucas', 10) == 123
    assert fibgolf('jacobsthal', 10) == 341
    assert fibgolf('pell', 10) == 2378
    assert fibgolf('perrin', 10) == 17
    assert fibgolf('padovan', 10) == 9
