from math import sqrt


def triangular_number(n):
    return n * (n + 1) / 2


def is_consecutive(number_list, j):
    start_index = number_list.index(j[0])
    end_index = number_list.index(j[-1])
    if start_index + len(j) - 1 == end_index:
        return True
    else:
        return False


def checkio(number):
    n = sqrt(number * 2)
    number_list = [
        triangular_number(i)
        for i in range(1, int(n) + 1)
        if triangular_number(i) < number
    ]
    length = len(number_list)
    while length > 1:
        for i in range(len(number_list) - length + 1):
            if sum(number_list[i : i + length]) == number:
                return number_list[i : i + length]
        length -= 1
    return []


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
