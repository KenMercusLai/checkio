def checkio():
    return 73  # if you are Sheldon

if __name__ == '__main__': # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert isinstance(checkio(), (int, float, complex))
