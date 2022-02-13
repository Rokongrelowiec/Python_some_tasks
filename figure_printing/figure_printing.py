class bcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'

def setColor():
    while True:
        print("Set your color")
        print(f"If you want {bcolors.FAIL}red{bcolors.RESET}, Enter 'R'")
        print(f"If you want {bcolors.WARNING}orange{bcolors.RESET}, Enter 'O'")
        print(f"If you want {bcolors.OK}green{bcolors.RESET}, Enter 'G'")
        print("If you do not want to change your color, Enter Q")
        print()
        ans = input("Set your color: ")
        ans = ans.strip()
        ans = ans.upper()
        if ans == "R":
            print(f"{bcolors.FAIL}")
            break
        elif ans == "O":
            print(f"{bcolors.WARNING}")
            break
        elif ans == "G":
            print(f"{bcolors.OK}")
            break
        elif ans == "Q":
            print(f"{bcolors.RESET}")
            break


def rectangular_triangle():
    x = int(input("Enter a number: "))
    i = 1
    while i < x+1:
        if i == 1 or i == 2 or i == x:
            print('x'*i)
        else:
            print('x'+' '*(i-2)+'x')
        i += 1


def square():
    x = int(input("Enter a number: "))
    i = 0
    while i < x:
        if i < x-1 and i > 0:
            print('x'+(x-2)*' '+'x')
        else:
            print(x*'x')
        i += 1


def diamond():
    while True:
        r = int(input("Enter a number: "))
        if r == 1:
            print('x')
        elif r <= 0:
            print('Try again')
        else:
            e = 1
            for i in range(r):
                if i == 0:
                    print(' '*r + 'x' + ' '*r)
                else:
                    print(' '*(r-i) + 'x'+' '*e + 'x' + ' '*(r-i))
                    e += 2
            print('x'+' '*e+'x')
            for i in range(1, r+1):
                if i == r:
                    print(' '*r + 'x' + ' '*r)
                else:
                    e -= 2
                    print(' '*i + 'x' + ' '*e + 'x'+ ' '*i)
        break

def triangle():
    while True:
        r = int(input("Enter a number: "))
        if r == 1:
            print('x')
        elif r <= 0:
            print('Try again')
        else:
            e = 1
            for i in range(r):
                if i == 0:
                    print(' ' * r + 'x' + ' ' * r)
                else:
                    print(' ' * (r - i) + 'x' + ' ' * e + 'x' + ' ' * (r - i))
                    e += 2
            print('x'+'x'*e+'x')
            break

while True:
    print("What you want to print?")
    print("Enter 'A', if you want to print square")
    print("Enter 'B', if you want to print rectangular triangle")
    print("Enter 'C', if you want to print diamond")
    print("Enter 'D', if you want to print triangle")
    print("Enter 'Q', if you want to exit")
    print()
    ans = input("Your answer: ")
    ans = ans.strip()
    ans = ans.lower()
    if ans == 'q':
        print(f"{bcolors.RESET}")
        break

    if ans == 'a':
        setColor()
        square()
        print(f"{bcolors.RESET}")
    elif ans == 'b':
        setColor()
        rectangular_triangle()
        print(f"{bcolors.RESET}")
    elif ans == 'c':
        setColor()
        diamond()
        print(f"{bcolors.RESET}")
    elif ans == 'd':
        setColor()
        triangle()
        print(f"{bcolors.RESET}")
    else:
        print('Something went wrong\nTry again\n')
