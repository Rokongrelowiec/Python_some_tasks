class bcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'

def cash_machine():
    a = int(input(f"{bcolors.WARNING}Enter the number of zlotys: {bcolors.RESET}"))
    b = int(input(f"{bcolors.WARNING}Enter the number of pennies/groszy: {bcolors.RESET}"))
    while True:
        if (b>0 and b<100):
            break
        else:
            b = int(input(f"{bcolors.WARNING}Enter the number of pennies/groszy: {bcolors.RESET}"))

    list_polish_zlotys = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    list_polish_pennies = [50, 20, 10, 5, 2, 1]
    i = 0
    list_zlotys = []
    list_pennies = []

    while i < 9:
        if (a - list_polish_zlotys[i] >= 0):
            a = a-list_polish_zlotys[i]
            list_zlotys.append(list_polish_zlotys[i])
        else:
            i += 1
    i = 0
    while i < 6:
        if (b - list_polish_pennies[i] >= 0):
            b = b - list_polish_pennies[i]
            list_pennies.append(list_polish_pennies[i])
        else:
            i += 1
    list_banknotes = [i for i in list_zlotys if i > 9]
    list_zlotys = [i for i in list_zlotys if i < 10]
    print(f"{bcolors.OK}Banknotes: {list_banknotes}")
    print(f"Zlotys: {list_zlotys}")
    print(f"Pennies: {list_pennies} {bcolors.RESET}")

cash_machine()
