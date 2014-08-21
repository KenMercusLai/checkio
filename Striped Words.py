VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def SplitText(text):
    result = []
    tempText = ''
    for i in text:
        if i.isalpha() or i.isdigit():
            tempText += i.upper()
        else:
            result.append(tempText)
            tempText = ''
    if tempText:
        result.append(tempText)
    return [i for i in result if i]


def checkio(text):
    counter = 0
    for j in SplitText(text):
        notStriped = True
        if len(j) == 1:
            notStriped = False
        for i in zip(j, j[1:]):
            if ((i[0] in VOWELS + CONSONANTS)
                    and (i[1] in VOWELS + CONSONANTS)):
                if ((i[0] in CONSONANTS and i[1] in CONSONANTS)
                        or (i[1] in VOWELS and i[0] in VOWELS)):
                    notStriped = False
                    break
            else:
                notStriped = False
        if notStriped:
            counter += 1
    return counter

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
