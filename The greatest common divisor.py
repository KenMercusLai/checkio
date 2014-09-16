def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """

    def factors(n):
        return sorted(set(reduce(list.__add__,
                                 ([i, n // i]
                                  for i in range(1, int(n ** 0.5) + 1)
                                  if n % i == 0))), reverse=True)

    for i in factors(min(args)):
        if all(map(lambda x: x % i == 0, args)):
            return i


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
