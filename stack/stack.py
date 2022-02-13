class bcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'

def stack():
    lst = []
    while True:
        print(f"{bcolors.WARNING}Enter: '1' to add 3 numbers on stack")
        print("Enter: '2' to remove 3 numbers")
        print("Enter: '3' to look up list")
        print(f"Enter: '4' to end {bcolors.RESET}")
        answer = input("What you want to do: ")
        if (answer == "1"):
            for e in range(0, 3):
                insert = int(input(f"{bcolors.WARNING}Enter {e+1} number on a stack: {bcolors.RESET}"))
                lst.append(insert)
            print(f"{bcolors.OK}{lst}{bcolors.RESET}")
        elif(answer == "2"):
            check1 = int(input(f"{bcolors.WARNING}Check number 1 on a stack: {bcolors.RESET}"))
            check2 = int(input(f"{bcolors.WARNING}Check number 2 on a stack: {bcolors.RESET}"))
            check3 = int(input(f"{bcolors.WARNING}Check number 2 on a stack: {bcolors.RESET}"))
            if (check1 in lst and check2 in lst and check3 in lst):
                if (lst[-3] == check1 and lst[-2] == check2 and lst[-1] == check3):
                    print(f"{bcolors.OK}Found 3 numbers on stack/this 3 numbers have popped!{bcolors.RESET}")
                    lst.remove(lst[-3])
                    lst.remove(lst[-2])
                    lst.remove(lst[-1])
                elif (check1 in lst and check2 in lst and check3 in lst):
                    print(f"{bcolors.OK}These numbers are deeper on a stack!{bcolors.RESET}")
            else:
                print(f"{bcolors.FAIL}Stack does not contain these numbers!{bcolors.RESET}")
        elif(answer == "3"):
            if not lst:
                print(f"{bcolors.WARNING}Stack is empty!{bcolors.RESET}")
            else:
                print(f"{bcolors.OK}{lst}{bcolors.RESET}")
        elif(answer == "4"):
            break

stack()
