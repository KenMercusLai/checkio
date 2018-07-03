def to_binary(int_digit, length=4):
    """Convert a digit into binary string.

    Arguments:
        int_digit {str} -- the digit needed to be convert

    Keyword Arguments:
        length {int} -- length of converted string (default: {4})

    Returns:
        str -- a string with specific length converted from int

    """
    format_str = '{:0>%ds}' % length
    return format_str.format(bin(int(int_digit))[2:])


def checkio(data):
    data = ['{:0>2s}'.format(i) for i in data.split(':')]
    bin_data = [[to_binary(i[0], 3), to_binary(i[1])] for i in data]
    bin_data = list(map(lambda x: ' '.join(x), bin_data))
    bin_data = ' : '.join(bin_data)
    return bin_data.replace('0', '.').replace('1', '-')[1:]


# These "asserts" using only for self-checking
# and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("11:10:12") == ".- ...- : ..- .... : ..- ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
