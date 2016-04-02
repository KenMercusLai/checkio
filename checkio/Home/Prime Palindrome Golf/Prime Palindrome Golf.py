# flake8: noqa
def golf(k):
    return [i for i in range(k+1,99999)if`i`==`i`[::-1]and~-2**i%i<2][0]

print golf(90000)
