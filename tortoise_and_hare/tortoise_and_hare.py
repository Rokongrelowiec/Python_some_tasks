class bcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'


def tortoise_and_hare():
    lst = [2, 5, 11, 3, 8, 13, 21, 19, 15, 41, 33, 27, 31]

    tortoise_current = 1
    hare_current = 3

    hare_position = lst[hare_current]
    tortoise_position = lst[tortoise_current]

    laps_hare = 0
    laps_tortoise = 0

    while True:
        hare_position = lst[hare_current]
        tortoise_position = lst[tortoise_current]
        if hare_position == tortoise_position:
            break
        elif tortoise_position == lst[len(lst) - 1] and hare_position == lst[len(lst) - 2]:
            tortoise_current = 0
            hare_current = 1
            laps_hare += 1
            laps_tortoise += 1
        elif tortoise_position == lst[len(lst) - 1] and hare_position == lst[len(lst) - 3]:
            tortoise_current = 0
            hare_current = 0
            laps_hare += 1
            laps_tortoise += 1
        elif hare_position == lst[len(lst) - 1]:
            hare_current = 2
            tortoise_current += 1
            laps_hare += 1
        elif hare_position == lst[len(lst) - 2]:
            hare_current = 1
            tortoise_current += 1
            laps_hare += 1
        elif hare_position == lst[len(lst) - 3]:
            hare_current = 0
            tortoise_current += 1
            laps_hare += 1
        elif tortoise_position == lst[len(lst) - 1]:
            tortoise_current = 0
            hare_current += 3
            laps_tortoise += 1
        else:
            hare_current += 3
            tortoise_current += 1

    print("Hare position (number it stand on):", hare_position)
    print("Tortoise position (number it stand on):", tortoise_position)
    print(f"{bcolors.OK}Laps of hare: {laps_hare}")
    print(f"Laps of tortoise: {laps_tortoise}{bcolors.RESET}")

tortoise_and_hare()
