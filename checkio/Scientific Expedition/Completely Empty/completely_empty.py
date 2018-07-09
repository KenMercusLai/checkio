import collections


def completely_empty(val):
    if type(val) == str:
        if val == '':
            return True
        else:
            return False

    if type(val) == list:
        if len(val) == 0:
            return True
        else:
            return all([completely_empty(i) for i in val])

    if type(val) == dict:
        if len(val) == 0:
            return True
        elif len(val.keys()) == 1 and '' in val:
            return True
        return False

    if type(val) == tuple:
        return completely_empty(list(val))

    try:
        val.__getitem__(0)
    except IndexError:
        return True
    except AttributeError:
        pass

    if isinstance(val, collections.Iterable):
        return all([completely_empty(i) for i in val])
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[], []]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[], [1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[], [{'': 'No WAY'}]]) == True
    print('Done')
