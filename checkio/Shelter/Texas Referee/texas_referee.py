RANKS = "23456789TJQKA"
SUITS = "scdh"

from itertools import combinations


def straight_flush(cards_list):
    s = straight(cards_list)
    f = flush(cards_list)
    if s and f:
        for i in s:
            if i in f:
                return [i]


def same_rank(cards_list, num):
    result = []
    for i in combinations(cards_list, num):
        if len(set([j[0] for j in i])) == 1:
            result.append(i)
    return result


def four_of_kind(cards_list):
    four = same_rank(cards_list, 4)
    for i in four:
        sub_cards_list = [j for j in cards_list if j not in i]
        return [(list(i) + [sub_cards_list[0]])]


def full_house(cards_list):
    three = same_rank(cards_list, 3)
    for i in three:
        sub_cards_list = [j for j in cards_list if j not in i]
        pairs = same_rank(sub_cards_list, 2)
        if pairs:
            return [(list(i) + list(pairs[0]))]


def flush(cards_list):
    result = []
    for i in combinations(cards_list, 5):
        if len(set([j[1] for j in i])) == 1:
            result.append(i)
    return result


def straight(cards_list):
    result = []
    for i in combinations(cards_list, 5):
        rank = list(map(lambda x: x[0], i))
        if rank[0] - rank[-1] == 4 and len(set(rank)) == 5:
            result.append(i)
    return result


def three_of_a_kind(cards_list):
    four = same_rank(cards_list, 3)
    for i in four:
        sub_cards_list = [j for j in cards_list if j not in i]
        return [(list(i) + sub_cards_list[:2])]


def two_pair(cards_list):
    pairs = same_rank(cards_list, 2)
    if len(pairs) >= 2:
        two = tuple(list(pairs[0]) + list(pairs[1]))
        sub_cards_list = [j for j in cards_list if j not in two]
        return [sorted(list(two) + [sub_cards_list[0]], reverse=True)]


def one_pair(cards_list):
    pairs = same_rank(cards_list, 2)
    if len(pairs) == 1:
        two = tuple(list(pairs[0]))
        sub_cards_list = [j for j in cards_list if j not in two]
        return [sorted(list(two) + sub_cards_list[:3], reverse=True)]


def high_card(cards_list):
    return [(cards_list[:5])]


def texas_referee(cards_str):
    cards_list = sorted(
        [(RANKS.index(i[0]) + 2, SUITS.index(i[1])) for i in cards_str.split(',')],
        reverse=True,
    )

    hand_list = (
        straight_flush,
        four_of_kind,
        full_house,
        flush,
        straight,
        three_of_a_kind,
        two_pair,
        one_pair,
        high_card,
    )
    for fun in hand_list:
        cards = fun(cards_list)
        if cards:
            cards = [str(RANKS[i[0] - 2]) + str(SUITS[i[1]]) for i in cards[0]]
            return ','.join(cards)


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert (
        texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th"
    ), "High Straight Flush"
    assert texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d", "Straight Flush"
    assert texas_referee("5c,7h,7d,9s,9c,8h,6d") == "9c,8h,7h,6d,5c", "Straight"
    assert texas_referee("Ts,2h,2d,3s,Td,3c,Th") == "Th,Td,Ts,3c,3s", "Full House"
    assert (
        texas_referee("Jh,Js,9h,Jd,Th,8h,Td") == "Jh,Jd,Js,Th,Td"
    ), "Full House vs Flush"
    assert texas_referee("Js,Td,8d,9s,7d,2d,4d") == "Td,8d,7d,4d,2d", "Flush"
    assert texas_referee("Ts,2h,Tc,3s,Td,3c,Th") == "Th,Td,Tc,Ts,3c", "Four of Kind"
    assert texas_referee("Ks,9h,Th,Jh,Kd,Kh,8s") == "Kh,Kd,Ks,Jh,Th", "Three of Kind"
    assert texas_referee("2c,3s,4s,5s,7s,2d,7h") == "7h,7s,5s,2d,2c", "Two Pairs"
    assert texas_referee("2s,3s,4s,5s,2d,7h,8h") == "8h,7h,5s,2d,2s", "One Pair"
    assert texas_referee("3h,4h,Th,6s,Ad,Jc,2h") == "Ad,Jc,Th,6s,4h", "High Cards"
