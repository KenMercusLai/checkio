import types


def parse_args(args, key):
    # apply key func to all args
    ret = [key(i) for i in args]
    return ret


def nomalise_args(*args):
    # turn args to a single level list
    new_args = [None]
    while len(new_args) == 1:
        new_args = list(args[0])
        if isinstance(new_args, types.GeneratorType):
            new_args = list(new_args)
        if new_args == args[0] or type(new_args[0]) in [int, float]:
            break
        args = new_args
    return new_args


def find_value(args, biggest=True):
    # find the max/min by iteration
    index = 0
    value = args[0]
    for i, v in enumerate(args):
        if (biggest and v > value) or (not biggest and v < value):
            index = i
            value = v
    return index


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    nomalised_args = nomalise_args(args)
    if key:
        parsed_args = parse_args(nomalised_args, key)
    else:
        parsed_args = nomalised_args
    return nomalised_args[find_value(parsed_args, False)]


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    nomalised_args = nomalise_args(args)
    if key:
        parsed_args = parse_args(nomalised_args, key)
    else:
        parsed_args = nomalised_args
    return nomalised_args[find_value(parsed_args)]


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
