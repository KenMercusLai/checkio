def SplitList(originalList):
    zeroIndexes = sorted(
        [i for i, j in enumerate(originalList) if j == 0], reverse=True)
    if not zeroIndexes:
        return [originalList]
    result = []
    zeroIndexes.append(-1)
    for i in zeroIndexes:
        result.append(originalList[i + 1:])
        originalList = originalList[:i]
    return result


def checkio(words):
    wordList = map(lambda x: 1 if x.isalpha() else 0, words.split())
    return len(filter(lambda x: x >= 3, map(sum,  SplitList(wordList)))) >= 1

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
