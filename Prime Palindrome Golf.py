from math import ceil


def golf(number):
    while True:
        number += 1
        numberString = str(number)
        index = int(ceil(len(numberString) / 2.0))
        if numberString[:index] == numberString[-index:][::-1]:
            if all(number % i for i in xrange(2, number)):
                return number

print golf(13)
