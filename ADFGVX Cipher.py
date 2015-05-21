from itertools import cycle
VALIDCHARS = 'abcdefghijklmnopqrstuvwxyz1234567890'


def GetMessage(message):
    return ''.join([i for i in message.lower() if i in VALIDCHARS])


def FractionatedForm(char, secret_alphabet):
    index = secret_alphabet.index(char)
    return 'ADFGVX' [index / 6] + 'ADFGVX' [index % 6]


def RemoveDups(ListObject):
    temp = list(set(ListObject))
    temp.sort(key=lambda x: ListObject.index(x))
    return temp


def encode(message, secret_alphabet, keyword):
    FracForm = [FractionatedForm(i, secret_alphabet)
                for i in GetMessage(message)]
    keyword = RemoveDups(keyword)
    # heading table
    HeadingTable = {}
    counter = 0
    for i in cycle(keyword):
        if i not in HeadingTable:
            HeadingTable[i] = ''
        HeadingTable[i] += ''.join(FracForm)[counter]
        counter += 1
        if counter == len(''.join(FracForm)):
            break
    return ''.join([HeadingTable[i] for i in sorted(HeadingTable.keys())])


def CreateHeadingTable(keyword, message):
    HeadingTable = {}
    for i in keyword:
        HeadingTable[i] = []

    counter = 0
    for i in cycle(keyword):
        HeadingTable[i].append('')
        counter += 1
        if counter == len(message):
            break

    for i in sorted(HeadingTable.keys()):
        HeadingTable[i] = list(message[:len(HeadingTable[i])])
        message = message[len(HeadingTable[i]):]
    return HeadingTable


def DefractionatedForm(FracForm, secret_alphabet):
    return secret_alphabet['ADFGVX'.index(FracForm[0]) * 6 +
                           'ADFGVX'.index(FracForm[1])]


def decode(message, secret_alphabet, keyword):
    keyword = RemoveDups(keyword)
    heading_table = CreateHeadingTable(keyword, message)
    counter = 0
    fractionated_form = ''
    for i in cycle(keyword):
        fractionated_form += heading_table[i][0]
        del heading_table[i][0]
        counter += 1
        if counter == len(message):
            break
    OriginalMessage = ''
    for i in [fractionated_form[i:i + 2]
              for i in range(0, len(fractionated_form), 2)]:
        OriginalMessage += DefractionatedForm(i, secret_alphabet)
    return OriginalMessage


if __name__ == '__main__':
    assert encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode(
        "ditiszeergeheim", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
        "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"
