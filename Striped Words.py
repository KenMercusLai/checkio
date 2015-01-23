VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def split_text(text):
    result = []
    temp_text = ''
    for i in text:
        if i.isalpha() or i.isdigit():
            temp_text += i.upper()
        else:
            result.append(temp_text)
            temp_text = ''
    if temp_text:
        result.append(temp_text)
    return [i for i in result if i]


def checkio(text):
    counter = 0
    for j in split_text(text):
        not_striped = True
        if len(j) == 1:
            not_striped = False
        for i in zip(j, j[1:]):
            if ((i[0] in VOWELS + CONSONANTS)
                    and (i[1] in VOWELS + CONSONANTS)):
                if ((i[0] in CONSONANTS and i[1] in CONSONANTS)
                        or (i[1] in VOWELS and i[0] in VOWELS)):
                    not_striped = False
                    break
            else:
                not_striped = False
        if not_striped:
            counter += 1
    return counter

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
