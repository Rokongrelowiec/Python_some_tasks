def missing(A):
    max = A[0]
    for i in A:
        if i > max:
            max = i
    if max < 1:
        return 1
    else:
        for i in range(1, max+1):
            if i in A:
                continue
            else:
                return i
        else:
            return i + 1
print(missing([1, 2, 3, 5, 6, 7]))
print(missing([-3, -4, -8]))
print(missing([1, 2, 3, 4]))
