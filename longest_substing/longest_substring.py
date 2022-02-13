def longest(tab):
    max = 0
    aktualny = 0
    for i in range(1, len(tab)):
        if tab[i-1] < tab[i]:
            aktualny += 1
            if (aktualny > max):
                max = aktualny
            else:
                aktualny = 0
            
    print(max)

longest([2, -5, 8, 15, 19, 2, 4])