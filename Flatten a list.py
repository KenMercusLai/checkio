def flat_list(a):
    t=[]
    for i in a:
        if isinstance(i,list):t=t+flat_list(i)
        else:t.append(i)
    return t


assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
