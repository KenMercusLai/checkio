import re
VOWELS = "aeiouy"


def translate(phrase):
    i = 0
    newPhrase = ''
    while i < len(phrase):
        if phrase[i] == ' ':
            newPhrase += phrase[i]
            i += 1
        elif phrase[i] in VOWELS:
            newPhrase += phrase[i]
            i += 3
        else:
            newPhrase += phrase[i]
            i += 2
    return newPhrase

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(
        u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
