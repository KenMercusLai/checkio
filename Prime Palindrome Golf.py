def golf(k):
    return [i for i in range(k + 1, 99999) if i == int(str(i)[::-1]) and all(i % j for j in range(2, i))][0]


print golf(90000)
