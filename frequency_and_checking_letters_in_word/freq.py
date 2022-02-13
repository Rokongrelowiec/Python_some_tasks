def dictionary():
    text = input("Text: ")
    dict = {}
    for i in text:
        if i in dict.keys():
            dict[i] = dict[i]+1
        else:
            dict[i] = 1
    print(dict)
dictionary()

def frequency():
    text = input("Text: ")
    letter = input("Letter: ")
    tmp = 0
    for i in text:
        if i == letter:
            tmp += 1
    print(round(tmp/len(text)*100, 2), "%")
frequency()
