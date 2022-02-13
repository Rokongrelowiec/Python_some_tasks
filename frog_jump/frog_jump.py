def frog(x, y, d):
    if x == y:
        return "y does not matter, frog is already there"
    else:
        i = 0
        while x < y:
            i += 1
            x += d
    return f'Steps: {i}'
print(frog(10, 85, 30))
print(frog(13, 1021, 11))
