from math import ceil


def golf(number):
    while True:
        number += 1
        numberString = str(number)
        index = int(ceil(len(numberString) / 2.0))
        if numberString[:index] == numberString[-index:][::-1]:
            isPrime = True
            for i in range(2, number):
                if number % i == 0:
                    isPrime = False
                    break
            if isPrime:
                return number

print golf(13)
