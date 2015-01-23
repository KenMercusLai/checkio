def check_command(pattern, command):
    pattern = map(lambda x: x == '1', list(str(bin(pattern))[2:]))
    command = map(lambda x: x.isalpha(), list(command))
    while pattern or command:
        try:
            p = pattern.pop()
        except:
            p = False
        try:
            c = command.pop()
        except:
            c = False
        if c != p:
            return False
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert check_command(42, u"12a0b3e4") == True, "42 is the answer"
    assert check_command(101, u"ab23b4zz") == False, "one hundred plus one"
    assert check_command(0, u"478103487120470129") == True, "Any number"
    assert check_command(127, u"Checkio") == True, "Uppercase"
    assert check_command(7, u"Hello") == False, "Only full match"
    assert check_command(8, u"a") == False, "Too short command"
    assert check_command(5, u"H2O") == True, "Water"
    assert check_command(42, u"C2H5OH") == False, "Yep, this is not the Answer"
