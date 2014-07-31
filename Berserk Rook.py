def findConnectRook(berserker, enemies):
    col, row = list(berserker)
    result = []
    # same row
    bigger = True
    smaller = True
    for i in range(8):
        if bigger and int(row) + i <= 8:
            pseudoEnemy = col + str(int(row) + i)
            if pseudoEnemy in enemies:
                result.append(pseudoEnemy)
                bigger = False
        if smaller and int(row) - i >= 1:
            pseudoEnemy = col + str(int(row) - i)
            if pseudoEnemy in enemies:
                result.append(pseudoEnemy)
                smaller = False
    # same col
    bigger = True
    smaller = True
    for i in range(8):
        if bigger and chr(ord(col) + i) <= 'h':
            pseudoEnemy = chr(ord(col) + i) + row
            if pseudoEnemy in enemies:
                result.append(pseudoEnemy)
                bigger = False
        if smaller and chr(ord(col) - i) >= 'a':
            pseudoEnemy = chr(ord(col) - i) + row
            if pseudoEnemy in enemies:
                result.append(pseudoEnemy)
                smaller = False
    return result


def berserk_rook(berserker, enemies):
    connectedEnemies = findConnectRook(berserker, enemies)
    if not connectedEnemies:
        return 0
    newStatus = [(i, [j for j in enemies if j != i]) for i in connectedEnemies]
    aaa = [berserk_rook(*i) for i in newStatus]
    result = max(aaa)
    return 1 + result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert berserk_rook(
        u'd3', {u'd6', u'b6', u'c8', u'g4', u'b8', u'g6'}) == 5, "one path"
    assert berserk_rook(
        u'a2', {u'f6', u'f2', u'a6', u'f8', u'h8', u'h6'}) == 6, "several paths"
    assert berserk_rook(
        u'a2', {u'f6', u'f8', u'f2', u'a6', u'h6'}) == 4, "Don't jump through"
