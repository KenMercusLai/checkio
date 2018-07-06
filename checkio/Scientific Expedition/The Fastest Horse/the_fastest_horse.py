from itertools import groupby


def fastest_horse(horses: list) -> int:
    winners = [i.index(min(i)) + 1 for i in horses]
    winning_counts = [(k, len(list(g))) for k, g in groupby(sorted(winners))]
    winner = sorted(winning_counts, key=lambda x: x[1])[-1][0]
    return winner


if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'],
                          ['1:10', '1:18', '1:14'],
                          ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
