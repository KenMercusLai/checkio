def GetKeyMatrix(key):
    key += 'abcdefghijklmnopqrstuvwxyz0123456789'
    Keys = []
    [Keys.append(i) for i in key if i not in Keys]
    return Keys


def encode(message, key):
    KeyMatrix = GetKeyMatrix(key)

    # convert message
    message = [i for i in message.lower() if i in KeyMatrix]
    i = 0
    Digraphs = []
    while i <= len(message) - 1:
        # If needed, append a "z" to complete the final digraph (or "x" if the
        # last letter is "z")
        if i == len(message) - 1:
            if message[i] != 'z':
                Digraphs.append(message[i] + 'z')
            else:
                Digraphs.append(message[i] + 'x')
            i += 1
        elif message[i] != message[i + 1]:
            Digraphs.append(''.join(message[i:i + 2]))
            i += 2
        # If both letters are the same, add an "x" after the first letter (for
        # double "x" use "z" as completion character)
        elif message[i] == message[i + 1]:
            if message[i] != 'x':
                Digraphs.append(message[i] + 'x')
            else:
                Digraphs.append(message[i] + 'z')
            i += 1
        else:
            print 'FUCK!', message[i], message[i + 1]
            raise

    EncryptedText = []
    for i in Digraphs:
        row0 = KeyMatrix.index(i[0]) / 6
        col0 = KeyMatrix.index(i[0]) % 6
        row1 = KeyMatrix.index(i[1]) / 6
        col1 = KeyMatrix.index(i[1]) % 6
        if row0 == row1:
            col0 += 1
            col1 += 1
            if col0 > 5:
                col0 -= 6
            if col1 > 5:
                col1 -= 6
        elif col0 == col1:
            row0 += 1
            row1 += 1
            if row0 > 5:
                row0 -= 6
            if row1 > 5:
                row1 -= 6
        else:
            col0, col1 = col1, col0
        EncryptedText.append(KeyMatrix[row0 * 6 + col0] +
                             KeyMatrix[row1 * 6 + col1])
    return ''.join(EncryptedText)


def decode(secret_message, key):
    KeyMatrix = GetKeyMatrix(key)

    # convert message
    secret_message = [secret_message[i:i + 2]
                      for i in range(0, len(secret_message.lower()), 2)]
    message = []
    for i in secret_message:
        row0 = KeyMatrix.index(i[0]) / 6
        col0 = KeyMatrix.index(i[0]) % 6
        row1 = KeyMatrix.index(i[1]) / 6
        col1 = KeyMatrix.index(i[1]) % 6
        if row0 == row1:
            col0 -= 1
            col1 -= 1
            if col0 < 0:
                col0 += 6
            if col1 < 0:
                col1 += 6
        elif col0 == col1:
            row0 -= 1
            row1 -= 1
            if row0 < 0:
                row0 += 6
            if row1 < 0:
                row1 += 6
        else:
            col0, col1 = col1, col0
        message.append(KeyMatrix[row0 * 6 + col0] + KeyMatrix[row1 * 6 + col1])
    return ''.join(message)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert encode("Fizz Buzz is x89 XX.",
                  "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode(
        "do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode(
        "How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode(
        "My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode(
        "ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
