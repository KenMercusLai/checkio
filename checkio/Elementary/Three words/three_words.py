is_word = lambda x: 1 if x.isalpha() else 0


def checkio(words):
    word_list = [is_word(i) for i in words.split()]
    consecutive_words = [sum(word_list[i:i + 3])
                         for i in range(len(word_list))
                         if word_list[i]]
    return any([True for i in consecutive_words if i >= 3])

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':  # pragma: no cover
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
