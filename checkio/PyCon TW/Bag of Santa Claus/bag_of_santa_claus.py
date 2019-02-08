__author__ = 'KenMercusLai'


def choose_good_gift(current_gift, gifts_in_bag, gift_number):
    from random import random

    # coin
    if random() > 0.5:
        return True
    else:
        return False


if __name__ == '__main__':
    # This part is using only for self-checking
    # and not necessary for auto-testing
    from random import random, randint, uniform

    scale = (random() + random()) ** randint(0, 1024)

    standings = gift_count = best_gifts = 0
    bag_count = 2000
    for j in range(bag_count):
        gifts_in_bag = randint(10, 1000)
        gift_count += gifts_in_bag

        gifts = []
        selected_gift = None
        for i in range(gifts_in_bag):
            new_gift = uniform(0.0, scale)
            gifts.append(new_gift)
            decision = choose_good_gift(new_gift, gifts_in_bag, i + 1)
            if decision:
                selected_gift = new_gift
                gifts.extend([uniform(0.0, scale) for _ in range(gifts_in_bag - i - 1)])
                break
        if selected_gift is None:
            priority = len(gifts)
        else:
            priority = sum(selected_gift < x for x in gifts)
        standings += priority
        best_gifts += not priority
    print(
        'You do won {:n} best gifts from {:n} bags with {:,} gifts!\n'
        'It seems like for bags of {:n} gifts -\n'
        'you would choose the second best gift, silver ;)'.format(
            best_gifts, bag_count, gift_count, round(gift_count / standings) + 1
        )
    )
