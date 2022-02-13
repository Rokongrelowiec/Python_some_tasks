class bcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'

def gameGuess():
    from random import randint
    from time import sleep
    print("I will try to guess number between 0 and 100")
    sleep(3.5)
    guess = randint(0, 100)
    min = 0
    max = 100
    answ = ""
    step = 0
    while answ != "1":
        print("My number is: ", guess, "Do I guess?")
        print(f"{bcolors.WARNING}Enter '1', if I guessed")
        print("Enter '2', if it is too less")
        print(f"Enter '3', if it is too many{bcolors.RESET}")
        step += 1
        answ = input("Answer: ")
        if answ == "2":
            min = guess
            guess = randint(min+1, max-1)
        elif answ == "3":
            max = guess
            guess = randint(min+1, max-1)
        else:
            continue
    if (step == 1):
        print(f"{bcolors.OK}Congratulation!\nNumber was found in {step} move!{bcolors.RESET}")
    else:
        print(f"{bcolors.OK}Congratulation!\nNumber was found in {step} moves!{bcolors.RESET}")


gameGuess()
