def safe_pawns(pawns):
    safePawns = 0
    for i in pawns:
        col, row = list(i)
        # pawn in row 1 cannot be protected by others
        if row == 1:
            continue
        # protect by left col pawn
        if 'a' not in col:
            if chr(ord(col) - 1) + str(int(row) - 1) in pawns:
                safePawns += 1
                continue
        # protect by right col pawn
        if 'h' not in col:
            if chr(ord(col) + 1) + str(int(row) - 1) in pawns:
                safePawns += 1
    return safePawns

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
