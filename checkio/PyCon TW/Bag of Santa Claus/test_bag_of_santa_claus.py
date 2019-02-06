import unittest
from random import randint, random, uniform

from bag_of_santa_claus import choose_good_gift


class Tests(unittest.TestCase):
    def test_Basics(self):
        scale = (random() + random()) ** randint(0, 1024)

        standings = gift_count = best_gifts = 0
        bag_count = 2000
        for j in range(bag_count):
            gifts_in_bag = randint(10, 1000)
            gift_count += gifts_in_bag

            gifts = []
            selected_gift = None
            for i in range(gifts_in_bag):
                new_gift = uniform(0., scale)
                gifts.append(new_gift)
                decision = choose_good_gift(new_gift, gifts_in_bag, i + 1)
                if decision:
                    selected_gift = new_gift
                    gifts.extend([uniform(0., scale)
                                  for _ in range(gifts_in_bag - i - 1)])
                    break
            if selected_gift is None:
                priority = len(gifts)
            else:
                priority = sum(selected_gift < x for x in gifts)
            standings += priority
            best_gifts += not priority
        return best_gifts, bag_count, gift_count


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
