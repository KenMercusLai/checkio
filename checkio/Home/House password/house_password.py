def checkio(data):
    has_numbers = {str(i) for i in range(0, 10)}.intersection(set(data))
    has_lower_chars = {chr(i) for i in range(ord('a'), ord('z') + 1)}.intersection(
        set(data)
    )
    has_upper_chars = {chr(i) for i in range(ord('A'), ord('Z') + 1)}.intersection(
        set(data)
    )
    if len(data) >= 10 and has_numbers and has_lower_chars and has_upper_chars:
        return True
    return False


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"
