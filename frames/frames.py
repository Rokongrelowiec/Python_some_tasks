def frames(arr, n, k):
    lst = []
    for i in range(0, n):
        tmp = arr[i:k+i]
        min = tmp[0]
        max = tmp[0]
        for e in tmp:
            if e > max:
                max = e
            elif e < min:
                min = e
        sub = max - min
        lst.append(sub)
    max_in_frame = 0
    for i in lst:
        if i > max_in_frame:
            max_in_frame = i
    return max_in_frame

print(frames([2, -5, 8, 15, 2, 4], 6, 3))
