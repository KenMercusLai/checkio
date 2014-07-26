def golf(number):
    return [i for i in range(number + 1, 99999) if i == int(str(i)[::-1]) and all(i % j for j in range(2, i))][0]


print golf(90000)
