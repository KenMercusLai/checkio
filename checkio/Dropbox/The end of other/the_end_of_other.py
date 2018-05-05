def checkio(words_set):
    word_list = sorted(list(words_set), key=len)
    return any([word_list[i] in word_list[j][-len(word_list[i]):]
                for i in range(len(word_list))
                for j in range(i + 1, len(word_list))])


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) is True, "helLO"
    assert checkio(
        {u"hello", u"la", u"hellow", u"cow"}) is False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) is True, "duck to walk"
    assert checkio({u"one"}) is False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) is False, "Only end"
