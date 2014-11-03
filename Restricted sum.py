def checkio(number):
    a = True + True
    while a < number:
        b = True + True
        while not a * b > number:
            if a * b == number:
                return False
            b += True
        a += True
    return True
