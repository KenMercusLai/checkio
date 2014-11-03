def rotate(state, pipe_numbers):
    pipe_numbers = sorted(set(pipe_numbers))
    PipeSplit = [0] + [i + 1 for i, j in
                       enumerate(zip(pipe_numbers, pipe_numbers[1:]))
                       if j[0] == j[1]] + [len(pipe_numbers)]
    Cannons = [pipe_numbers[i[0]:i[1]] for i in zip(PipeSplit, PipeSplit[1:])]
    RotateCounter = []
    for i in Cannons:
        for j in range(len(state)):
            if len(i) == sum([k1 for k0, k1 in enumerate(state[-j:]+state[:-j]) if k0 in i]):
                RotateCounter.append(j)
    return RotateCounter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [
        1, 8], "Example"
    assert rotate(
        [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [
        0, 5], "Two cannonballs in the same pipe"
