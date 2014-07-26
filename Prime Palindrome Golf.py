def golf(number):
    while True:
        number += 1
        if (str(number) == str(number)[::-1]
                and all(number % i for i in xrange(2, number))):
            return number

print golf(13)
