def binary_search(tab, var):
    if var in tab:
        tab_sort = []
        while len(tab) >= 1:
            min = tab[0]
            for i in tab:
                if i < min:
                    min = i
            tab_sort.append(min)
            tab.remove(min)
        print("Sorted tab: ", tab_sort)

        left = 0
        right = len(tab_sort)-1
        i = 1
        while True:
            center = (left+right)//2
            if tab_sort[center] == var:
                break
            elif tab_sort[center] < var:
                i += 1
                left = center + 1
            elif tab_sort[center] > var:
                i += 1
                right = center - 1

        print(f"Number of steps: {i}, to find number {var}")

binary_search([1, 2, 5, 1 , 9 , 10, 43, 231, 23, 53, 24, 34, 11, 51, 3, 1], 43)
