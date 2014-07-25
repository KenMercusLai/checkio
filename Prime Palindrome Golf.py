from math import ceil


def gen_primes(n):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            if q > n:
                yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def isPalindrome(number):
    numberString = str(number)
    firstHalf = numberString[:int(ceil(len(numberString) / 2.0))]
    secondHalf = numberString[-int(ceil(len(numberString) / 2.0)):]
    if firstHalf == secondHalf[::-1]:
        return True
    return False


def golf(number):
    for i in gen_primes(number):
        if isPalindrome(i):
            return i

print golf(2)
print golf(10)
print golf(1493)
