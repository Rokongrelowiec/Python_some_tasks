def duplicates():
    lista1 = [1, 3, 5, 7, 11, 12, 13]
    lista2 = [3, 13, 11, 21, 5, 1, 11, 13]
    lista3 = []

    for i in lista1:
        for e in lista2:
            if i == e:
                if e in lista3 or i in lista3:
                    continue
                else:
                    lista3.append(e)
    print(lista3)

duplicates()

def duplicates2():
    list1 = [1, 3, 5, 7, 11, 12, 13, 3, 8, 19]
    list2 = [3, 13, 11, 21, 5, 1, 11, 13, 53]
    list3 = set(list1) | set(list2)
    list3 = list(list3)
    print(list3)

duplicates2()
