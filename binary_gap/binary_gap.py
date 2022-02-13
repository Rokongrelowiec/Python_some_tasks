class bcolors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'

def binaryGap(number):
    e = 0
    print("Binary number: ", bin(number)[2:])
    while True:
        if number - 2**e >= 0:
            e += 1
        else:
            break
    e -= 1
    binary_number = ""
    while e >= 0:
        if number - 2**e >= 0:
            number -= 2**e
            binary_number += "1"
            e -= 1
        else:
            binary_number += "0"
            e -= 1

    num = binary_number
    num = num.split("1")
    num = num[:len(num)-1]

    lst = []
    for i in num:
        if len(i) > 0:
            lst.append(len(i))

    c = 1
    for i in lst:
        print(f"{bcolors.OK}Binary gap: {c}, length: {i}{bcolors.RESET}")
        c += 1

binaryGap(4121)
binaryGap(123)
