__author__ = 'KenMercusLai'


HANDS = (
    "one pair",
    "two pair",
    "three of a kind",
    "flush",
    "straight",
    "full house",
    "four of a kind",
    "five of a kind",
)


def poker_dice(rolls, scores):
    rolls = rolls[0]
    if len(set(rolls)) ==1:
    return "one pair" or rolls[:]



print poker_dice([["KH","KH","TH","9S","9S"]],{})