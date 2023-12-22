# REKURENCJA
# ZADANIA Z TABLICY

def f(x):
    if x == 1:
        return 1
    else:
        return x + f(x-1)


# print(f(5))
# print()


##########

def f2(x):
    if x < 1:
        return 0
    else:
        print(x)
        f2(x-1)
        print(x)


# print(f2(3))
# print()


##########

def f3(x):
    if x > 0:
        x -= 1
        f3(x)
        print(x)
        x -= 1
        f3(x)


# print(f3(3))
# print(f3(4))
# print()


##########

def f4(x):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f4(x-2) - f4(x-1)


##########

# ZADANIE 1
# print("ZADANIE 1")


def silnia(n):
    if n == 0:
        return 1
    else:
        return silnia(n - 1) * n


n = 5
# print(silnia(5))
# print()


# ZADANIE 2
# print("ZADANIE 2")


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# for e in range(6):
#    print(fib(e))


# ZADANIE 3 - suma elementów (1/k) od k=1 do n ---> 1 + 1/2 + 1/3 + 1/4 + ...
# print("ZADANIE 3")


def sigma(n):
    if n == 1:
        return 1
    else:
        return sigma(n-1) + 1/n


# print(sigma(2))
# print()


# ZADANIE 4
# print("ZADANIE 4")


def square_recursion(n):
    if n == 0:
        return 0
    else:
        return square_recursion(n-1) + n + n - 1


# print(square_recursion(3))
# print()


# ZADANIE 5
# print("ZADANIE 5")


def equal_recursion(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return equal_recursion(n-2) + n
    else:
        return equal_recursion(n-1)


# print(equal_recursion(9))
# print()


# ZADANIE 6
# print("ZADANIE 6")


def binary_recursion(lst, x, start, end):

    if start > end:
        return False
    mid = (start + end) // 2

    if lst[mid] == x:
        return mid
    elif lst[mid] < x:
        return binary_recursion(lst, x, mid+1, end)
    else:
        return binary_recursion(lst, x, start, mid-1)


lst = [1, 1, 2, 4, 6, 9, 10, 32, 454, 2135]
x = 1
result = binary_recursion(lst, x, 0, len(lst) - 1)

# if result != False:
#    print(f"target {x} found")
# else:
#    print(f"target {x} not found")
# print()


# ZADANIE 7
# print("ZADANIE 7")


def power_recursion(a, b):
    if b == 0:
        return 1
    else:
        return power_recursion(a, b-1) * a


#print(power_recursion(5, 0))
#print()
    

# ZADANIE 8
# print("ZADANIE 8")
    

