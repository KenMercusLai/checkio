def long_repeat(line):
    # length the longest substring that consists of the same char
    if len(line) >= 2:
        slice_index = [
            index for index, value in enumerate(line[:-1]) if value != line[index + 1]
        ]
        values = [
            slice_index[index + 1] - value
            for index, value in enumerate(slice_index[:-1])
        ]
        if values:
            return max(values)
    return len(line)


if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
