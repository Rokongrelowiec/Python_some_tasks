def closest(tab):

    sum = 0
    for i in tab:
        sum += i
    res = sum/len(tab)
    index = 0
    min = tab[0]
    for i in range(len(tab)):
        if abs(tab[i] - res) < min:
            index = i
    return tab[index]
    
print(closest([1, 2, 3, 4, 5, 6, 7]))
print(closest([2, 4, 8, 16, 7, 1, 4]))

