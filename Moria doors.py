import re


def CalcLikeness(word0, word1):
    Likeness = 0
    if word0[0] == word1[0]:
        Likeness += 0.1
    if word0[-1] == word1[-1]:
        Likeness += 0.1
    if len(word0) <= len(word1):
        Likeness += len(word0) * 0.3 / len(word1)
    else:
        Likeness += len(word1) * 0.3 / len(word0)
    Likeness += len(set(word0) & set(word1)) * 0.5 / len(set(word0 + word1))
    return round(Likeness * 100, 2)


def CalcMaxLikeness(AWord, WordList):
    return sum([CalcLikeness(AWord, i) for i in WordList]) / len(WordList)


def find_word(message):
    MessageGroup = re.findall('(\w+)', message)
    MessageGroup = [i.lower() for i in MessageGroup]
    Likeness = [CalcMaxLikeness(j, MessageGroup[:i] + MessageGroup[i + 1:])
                for i, j in enumerate(MessageGroup)]
    return [j for i, j in enumerate(MessageGroup)
            if Likeness[i] == max(Likeness)][-1].lower()

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(
        u"One, two, two, three, three, three.") == "three", "Repeating"
