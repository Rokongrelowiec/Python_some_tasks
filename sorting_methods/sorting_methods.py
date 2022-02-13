def bogo_sort(lst):
    import random

    while True:
        random.shuffle(lst)
        if all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)):
            break
        else:
            continue
    print("bogo_sort - Sorted list:", lst)

bogo_sort([3, 1, 11, 21, 13, 33, 6])

def bubble_sort(lst):
    lst1 = []

    for i in lst:
        for e in lst:
            if e == i:
                if e in lst1:
                    continue
                else:
                    lst1.append(e)

    for i in range(len(lst1) - 1):
        for e in range(len(lst1) - 1):
            if lst1[e] > lst1[e + 1]:
                lst1[e], lst1[e + 1] = lst1[e + 1], lst1[e]
            
    print("bubble_sort - Sorted list:", lst1)

bubble_sort([3, 1, 11, 21, 13, 33, 19, 41, 22, 16, 8, 23, 7, 7, 2])

def selection_sort(lst):
    lst1 = []
    lst2 = []

    for i in lst:
        for e in lst:
            if e == i:
                if e in lst1:
                    continue
                else:
                    lst1.append(e)

    for i in range(len(lst1)):
        min = lst1[0]
        for e in range(len(lst1)):
            if (lst1[e] < min): 
                min = lst1[e]

        lst2.append(min)
        del lst1[lst1.index(min)]
    print("selection_sort - Sorted list:", lst2)

selection_sort([3, 1, 11, 21, 13, 33, 19, 41, 22, 16, 8, 23, 7, 3, 10, 11, 38, 24])

def insertion_sort(lst):
    for i in range(len(lst)):
        for e in range(i, 0, -1):
            if lst[e] < lst[e-1]:
                lst[e], lst[e-1] = lst[e-1], lst[e]
    print("insertion_sort - Sorted list: ", lst)

insertion_sort([2, 1, 3, 10, 5, 11, 21, 23, 13, 7, 15])
