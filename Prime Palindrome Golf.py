from math import ceil


def golf(number):
    while True:
        number += 1
        index = int(ceil(len(str(number)) / 2.0))
        if str(number)[:index] == str(number)[-index:][::-1]:
            if all(number % i for i in xrange(2, number)):
                return number

print golf(13)
