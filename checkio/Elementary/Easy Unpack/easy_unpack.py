def easy_unpack(elements: tuple) -> tuple:
    return elements[0], elements[2], elements[-2]


if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
