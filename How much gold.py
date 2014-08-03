from fractions import Fraction

METALS = ('gold', 'tin', 'iron', 'copper')


def checkio(alloys):
    return 1 - sum([1 - alloys[i] if 'gold' in i else alloys[i]
                    for i in alloys]) / 2


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio({
        'gold-tin': Fraction(1, 2),
        'gold-iron': Fraction(1, 3),
        'gold-copper': Fraction(1, 4),
    }) == Fraction(1, 24), "1/24 of gold"
    assert checkio({
        'tin-iron': Fraction(1, 2),
        'iron-copper': Fraction(1, 2),
        'copper-tin': Fraction(1, 2),
    }) == Fraction(1, 4), "quarter"
