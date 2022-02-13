
def fib(n):
    lst = [0, 1]
    if n == 1:
        return lst[0]
    elif n == 2:
        return lst[1]
    else:
        return fib(n-1)+fib(n-2)

num = int(input("Fibonacci number: "))
print(fib(num))

def fibonacci():
    a = int(input("Enter number of fibonacci sequence: "))
    fib1 = 1
    fib2 = 1
    if a == 1 or a == 2:
        print(f"Word with number: {a}, Equals: 1")
    else:
        for i in range(2,a):
            res = fib1 + fib2
            fib1, fib2 = fib2, res
        print(res)

fibonacci()
