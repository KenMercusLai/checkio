from itertools import cycle
VALIDCHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def GetKeyStream(decrypted, encrypted):
    for i in range(26):
        if ((VALIDCHARS.index(decrypted) + i) % 26
                == VALIDCHARS.index(encrypted)):
            return i


def RemoveDups(ListObject):
    return map(list, set(map(tuple, ListObject)))


def GetKey(KeyStream):
    for i in range(1, len(KeyStream) + 1):
        SubKeys = [KeyStream[j:j + i] for j in range(0, len(KeyStream), i)]
        if len(SubKeys) == 1:
            return SubKeys[0]
        elif (len(RemoveDups(SubKeys[:-1])) == 1
              and SubKeys[-1] == SubKeys[0][:len(SubKeys[-1])]):
            return SubKeys[0]


def OriginalChar(encrypted, key):
    for i in range(26):
        if (i + key) % 26 == VALIDCHARS.index(encrypted):
            return VALIDCHARS[i]


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    EncryptKeyStream = [GetKeyStream(old_decrypted[i], old_encrypted[i])
                        for i in range(len(old_decrypted))]
    EncryptKey = GetKey(EncryptKeyStream)
    NewEncryptKey = []
    counter = len(new_encrypted)
    for i in cycle(EncryptKey):
        NewEncryptKey.append(i)
        counter -= 1
        if not counter:
            break
    # print NewEncryptKey
    return ''.join([OriginalChar(new_encrypted[i], NewEncryptKey[i])
                    for i in range(len(new_encrypted))])


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert decode_vigenere(u'DONTWORRYBEHAPPY',
                           u'FVRVGWFTFFGRIDRF',
                           u'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere(u'HELLO', u'OIWWC', u'ICP') == "BYE", "HELLO"
    assert decode_vigenere(u'LOREMIPSUM',
                           u'OCCSDQJEXA',
                           u'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
