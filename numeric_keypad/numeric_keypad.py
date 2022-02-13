def phone_old():

    text = input("Tekst: ")
    text = text.upper()
    text = text.strip()


    for i in text:
        w = ord(i)
        if w >= 87:
            w -= 87
            for e in range(w+1):
                print('9', end='')

        elif w >= 84:
            w -= 84
            for e in range(w+1):
                print('8', end='')

        elif w >= 80:
            w -= 80
            for e in range(w+1):
                print('7', end='')

        elif w >= 77:
            w -= 77
            for e in range(w+1):
                print('6', end='')

        elif w >= 74:
            w -= 74
            for e in range(w+1):
                print('5', end='')

        elif w >= 71:
            w -= 71
            for e in range(w+1):
                print('4', end='')
            
        elif w >= 68:
            w -= 68
            for e in range(w+1):
                print('3', end='')

        elif w >= 65:
            w -= 65
            for e in range(w+1):
                print('2', end='')

    print()

phone_old()
