def perm(a, k=0):
    if len(a) == k:
        print(a)
    else:
        for i in range(k, len(a)):
            a[i], a[k] = a[k], a[i]
            perm(a, k+1)
            a[i], a[k] = a[k], a[i]

perm(['A', 'B', 'C', 'D'])
