def reverseWord():
    word = input("Enter word: ")
    word = word[::-1]
    word = "".join(word)
    print(word)

reverseWord()

def diagonally_letters():
    word = input("Enter words: ")
    word1 = ""
    word2 = ""
    e = 0
    for i in word:
        if e%2 == 0:
            word1 = word1 + i + " "
        else:
            word2 = word2 + " " + i
        e += 1
    print(word1)
    print(word2)

diagonally_letters()


def letters_below():
    a = input("Enter words: ")
    lst = list(a)
    lst1 = []
    lst2 = []
    e = 0
    for i in lst:
        if e%2 == 0:
            lst1.append(i)

        else:
            lst2.append(i)
        e += 1
    print(" ".join(lst1))
    print(" ".join(lst2))

letters_below()


def double_second_letter():
    word = input("Enter your word: ")
    e = 0
    lst = []
    for i in word:
        if i == " ":
            e = 0
            lst.append(i)
            continue
        else:
            e += 1
            if e == 2:
                e = 0
                lst.append(i*2)
            else:
                lst.append(i)
    lst = "".join(lst)
    print(lst)

double_second_letter()

def concatenate(*args):
    word = ""
    e = 0
    for i in args:
        if e == 0:
            word += i
        else:
            word += "-" + i
        e += 1
    return word

print(concatenate("I", "love", "Python", "!"))

