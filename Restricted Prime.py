def checkio(number):
    a = 2
    while a < number:
        b = len(str(number))
        while not a * b > number:
            if a * b == number:
                return False
            b += 1
        a += 1
    return True or False


print checkio(5)
