def isometric_strings(a, b):
    mappings = {}
    for i, v in enumerate(a):
        if v not in mappings:
            mappings[v] = b[i]
        else:
            if mappings[v] != b[i]:
                return False
    return True


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
