def counting_sort(tab):
    dct = {}
    for i in range(max(tab)+1):
        dct[i] = 0
    for i in tab:
        dct[i] += 1
    lst = []
    for i in range(max(tab)+1):
        if dct[i] > 0:
            for e in range(dct[i]):
                lst.append(i)
    return lst

print(counting_sort([1, 2, 4, 1, 2, 6, 7, 3, 7, 9, 8 , 5, 5, 11, 6, 4, 21, 4, 13, 7, 18]))
