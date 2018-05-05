import itertools


def get_password(cipher_grille, ciphered_password):
    flat_grille = [True if j == 'X' else False
                   for i in cipher_grille
                   for j in i]
    flat_password = [j for i in ciphered_password for j in i]
    return ''.join(itertools.compress(flat_password, flat_grille))


def recall_password(cipher_grille, ciphered_password):
    password = ''
    for i in range(4):
        password += get_password(cipher_grille, ciphered_password)
        cipher_grille = list(map(lambda x: ''.join(x),
                                 zip(*cipher_grille[::-1])))
    return password


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
