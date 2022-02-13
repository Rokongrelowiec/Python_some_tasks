def cyclic_rotation(head, k):
    if k>=0 and k <= len(head):
        for i in range(-1, -k-1, -1):
            head.insert(0, head[i])
        for i in range(0, k):
            del head[-1]
        for i in head:
            if i is head[-1]:
                print(i)
            else:
                print(i, end=' -> ')
    else:
        print('Cannot execute this operation')

cyclic_rotation([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)
cyclic_rotation([3, 8, 9, 7, 6], 3)
cyclic_rotation([1, 2, 3, 4], 4)

print()

def linked_list2(head, k):
    lst = head[-k:]
    head = lst + head
    for i in range(k):
        del head[-1]
    for i in head:
        if i is head[-1]:
            print(i)
        else:
            print(i, end=' -> ')
linked_list2([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
cyclic_rotation([3, 8, 9, 7, 6], 3)
cyclic_rotation([1, 2, 3, 4], 4)
