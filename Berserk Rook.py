def berserk_rook(berserker, enemies):
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert berserk_rook(u'd3', {u'd6', u'b6', u'c8', u'g4', u'b8', u'g6'}) == 5, "one path"
    assert berserk_rook(u'a2', {u'f6', u'f2', u'a6', u'f8', u'h8', u'h6'}) == 6, "several paths"
    assert berserk_rook(u'a2', {u'f6', u'f8', u'f2', u'a6', u'h6'}) == 4, "Don't jump through"
