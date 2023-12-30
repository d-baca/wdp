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


# print(power_recursion(5, 0))
# print()


# ZADANIE 8
# print("ZADANIE 8")


def NWD(a, b):
    if a == b or b == 0:
        return a
    if a == 0:
        return b
    elif a < b:
        return NWD(a, b-a)
    else:
        return NWD(b, a-b)


a = 6
b = 4

# print(NWD(a, b))
# print()


# ZADANIE 9
# print("ZADANIE 9")


def num_sum_recursion(n):
    if n == 0:
        return 0
    else:
        return n % 10 + num_sum_recursion(n//10)


# n = 24064
# print(num_sum_recursion(n))
# print()


# ZADANIE 10
# print("ZADANIE 10")


def head(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return head(lst[:-1])


# lst = [1, 5, 3, 2, 8]
# print(head(lst))
# print()


# ZADANIE 11
# print("ZADANIE 11")


def tail(lst):
    if len(lst) <= 1:
        return []
    else:
        return [lst[1]] + tail(lst[1:])


# lst = [1, 5, 3, 2, 8]
# print(tail(lst))
# print()


# ZADANIE 12
# print("ZADANIE 12")
    

def IsEmpty(lst):
    if len(lst) == 0:
        return True
    else:
        return False


def rewers(lst):
    if IsEmpty(lst):
        return []
    else:
        return rewers(tail(lst)) + [head(lst)]


lst = [41, 5, 9, 2, 18]
reversed_lst = rewers(lst)

print("oryginalna lista:", lst)
print("lista w odwróconej kolejności:", reversed_lst)
print("czy pusta?", IsEmpty(reversed_lst))
