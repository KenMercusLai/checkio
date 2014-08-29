import re


def recognize(number):
    """
        Is it a normal ship?
    """
    return len(set(re.findall('1{1,}', bin(number)[2:]))) == 1

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert recognize(21) is True, "First example"
    assert recognize(1587) is True, "Second example"
    assert recognize(3687) is False, "Thid example"
