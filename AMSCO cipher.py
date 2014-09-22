def decode_amsco(message, key):
    # create empty matrix
    matrix = [[] for i in range(len(str(key)))]
    i = 0
    while i < len(message):
        for j in range(len(str(key))):
            if ((j % 2 != 0 and len(matrix[j]) % 2 == 0)
                    or (j % 2 == 0 and len(matrix[j]) % 2 != 0)):
                if i + 2 <= len(message):
                    matrix[j].append('  ')
                    i += 2
                elif i + 1 <= len(message):
                    matrix[j].append(' ')
                    i += 1
            else:
                if i + 1 <= len(message):
                    matrix[j].append(' ')
                    i += 1

    # fill the empty matrix
    for i in range(1, len(str(key)) + 1):
        column = matrix[str(key).index(str(i))]
        for j in range(len(column)):
            column[j] = message[:len(column[j])]
            message = message[len(column[j]):]

    # re-order by rows
    OriginalMessage = ''
    for i in range(max(map(len, matrix))):
        OriginalMessage += ''.join([j[i] for j in matrix if i <= len(j) - 1])

    return OriginalMessage

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert decode_amsco(
        u"oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco(u'kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco(u'hrewhoorrowyilmmmoaouletow',
                        123) == "howareyouwillhometommorrow", "How are you"
