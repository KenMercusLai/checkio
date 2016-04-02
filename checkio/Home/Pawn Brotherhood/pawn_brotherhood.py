def possible_neighbor(pawn):
    # find neighbors can suppor itself
    col, row = list(pawn)
    result = []
    if int(row) > 1:
        row = str(int(pawn[1]) - 1)
    if col < 'h':
        result.append(chr(ord(col) + 1) + row)
    if col > 'a':
        result.append(chr(ord(col) - 1) + row)
    return result

def safe_pawns(pawns):
    safe_counter = 0
    for i in pawns:
        for j in possible_neighbor(i):
            if j in pawns:
                safe_counter += 1
                break
    return safe_counter

if __name__ == '__main__': # pragma: no cover
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1


