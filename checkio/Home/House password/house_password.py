def checkio(data):
    if (len(data) >= 10 and
            {str(i) for i in range(0, 10)}.intersection(set(data)) and
            {chr(i) for i in range(ord('a'), ord('z') + 1)}
        .intersection(set(data)) and
            {chr(i) for i in range(ord('A'), ord('Z') + 1)}
            .intersection(set(data))):
        # replace this for solution
        return True
    return False

# Some hints
# Just check all conditions


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"
