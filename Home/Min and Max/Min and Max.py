from copy import deepcopy
import types


def ArgumentsList(args, key):
    if len(args) == 1 and (isinstance(args[0], list)
                           or isinstance(args[0], str)
                           or isinstance(args[0], tuple)):
        newArgs = deepcopy(args[0])
        clearArgs = map(key, args[0])
    elif len(args) == 1 and (isinstance(args[0], types.GeneratorType)
                             or isinstance(args[0], set)):
        newArgs = list(args[0])
        clearArgs = map(key, newArgs)
    else:
        newArgs = list(args)
        clearArgs = map(key, list(args))
    return newArgs, clearArgs


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    newArgs, clearArgs = ArgumentsList(args, key)

    changed = False
    while not changed:
        changed = True
        for i in range(len(clearArgs) - 1):
            if clearArgs[i] < clearArgs[i + 1]:
                clearArgs = clearArgs[:i + 1] + clearArgs[i + 2:]
                newArgs = newArgs[:i + 1] + newArgs[i + 2:]
                changed = False
                break
        for i in range(len(clearArgs) - 1):
            if clearArgs[i] > clearArgs[i + 1]:
                clearArgs = clearArgs[:i] + clearArgs[i + 1:]
                newArgs = newArgs[:i] + newArgs[i + 1:]
                changed = False
                break
    return newArgs[0]


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    newArgs, clearArgs = ArgumentsList(args, key)

    changed = False
    while not changed:
        changed = True
        for i in range(len(clearArgs) - 1):
            if clearArgs[i] > clearArgs[i + 1]:
                clearArgs = clearArgs[:i + 1] + clearArgs[i + 2:]
                newArgs = newArgs[:i + 1] + newArgs[i + 2:]
                changed = False
                break
        for i in range(len(clearArgs) - 1):
            if clearArgs[i] < clearArgs[i + 1]:
                clearArgs = clearArgs[:i] + clearArgs[i + 1:]
                newArgs = newArgs[:i] + newArgs[i + 1:]
                changed = False
                break
    return newArgs[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [
        9, 0], "lambda key"
    print min(abs(i) for i in range(-10, 10))
    print max(x + 5 for x in range(6))
    print min({1, 2, 3, 4, -10})
