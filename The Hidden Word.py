def CipherText(text):
    return ''.join([j.lower()
                    for i in text for j in i if j != ' ']).split('\n')


def checkio(text, word):
    CipheredText = CipherText(text)
    LongestLine = max(map(len, CipheredText))
    for i in range(len(CipheredText)):
        CipheredText[i] += ' ' * (LongestLine - len(CipheredText[i]))
    RowStart, RowEnd, ColStart, ColEnd = 0, 0, 0, 0
    # in rows
    for i, j in enumerate(CipheredText):
        index = j.find(word)
        if index != -1:
            RowStart = RowEnd = i + 1
            ColStart = index + 1
            ColEnd = index + len(word)
    if RowStart != 0:
        return [RowStart, ColStart, RowEnd, ColEnd]
    # in cols
    CipheredText = zip(*CipheredText[::])
    for i in range(len(CipheredText)):
        CipheredText[i] = ''.join(list(CipheredText[i]))
    for i, j in enumerate(CipheredText):
        index = j.find(word)
        if index != -1:
            ColStart = ColEnd = i + 1
            RowStart = index + 1
            RowEnd = index + len(word)
    return [RowStart, ColStart, RowEnd, ColEnd]

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
    assert checkio(u"""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", u"noir") == [4, 16, 7, 16]
