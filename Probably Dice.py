from __future__ import division
from itertools import product, combinations_with_replacement, permutations


def probability(dice_number, sides, target):
    dice = range(1, sides + 1)
    counter = 0
    for i in combinations_with_replacement(dice, dice_number):
        if sum(i) == target:
            print i
            # counter += len(set([j for j in permutations(i)]))
    print counter, sides ** dice_number, round(counter / (sides ** dice_number), 4)
    # combinations = [i for i in product(*([dice] * dice_number))
    #                 if sum(i) == target]
    return round(counter / (sides ** dice_number), 4)

if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for
    # auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    # assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    # assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    # assert(almost_equal(probability(2, 6, 7), 0.1667)
    #        ), "Maximum for two 6-sided dice"
    # assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    # assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    # assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)
           ), "Many dice, many sides"
