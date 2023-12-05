# binary search
import random
print()
print("BINARY SEARCH")


def binary_search(list, x):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return False


list = []
for i in range(100):
    list.append(random.randint(1, 100))
result = binary_search(list, 89)
print(result)
print()


# ZADANIE 1
print("ZADANIE 1")


# sposób z pętlą for


def generate_random_for(n):
    result_list = []

    for i in range(n):
        result_list.append(random.randint(1, 100))

    return result_list


print(generate_random_for(5))
print()


# sposób bez pętli for (z pętlą while)

def generate_random_while(n):
    result_list = []
    # i = len(result_list)

    while len(result_list) < n:
        result_list.append(random.randint(1, 100))
        # i += 1

    return result_list


print(generate_random_while(5))
print()


# ZADANIE 2
print("ZADANIE 2")


# sposób z pętlą for

def generate_random_sorted_for(n):
    result_list = []
    result_list.append(random.randint(1, 10))

    for i in range(1, n):
        result_list.append(random.randint(
            result_list[i - 1], 2 * result_list[i - 1]))

    return result_list


print(generate_random_sorted_for(5))
print()


# sposób bez pętli for (z pętlą while)

def generate_random_sorted_while(n):
    result_list = []
    result_list.append(random.randint(1, 10))
    i = 1

    while i < n:
        result_list.append(random.randint(
            result_list[i - 1], 3 * result_list[i - 1]))
        i += 1

    return result_list


print(generate_random_sorted_while(6))
print()


# ZADANIE 3
print("ZADANIE 3")


# sposób z pętlą for

def last_for(list, x):
    last_index = 0

    for i in range(len(list)):
        if list[i] == x:
            last_index = i

    return f"ostatnie wystąpienie liczby {x} jest na miejscu o indeksie {last_index}"


list = [1, 2, 2, 3, 2, 3, 3, 3, 6, 2]
result = last_for(list, 3)
print(result)
print()


# sposób bez użycia pętli for (z pętlą while)

def last_while(list, y):
    last_index = 0
    i = 0

    while i < len(list):
        if list[i] == y:
            last_index = i
        i += 1

    return f"ostatnie wystąpienie liczby {y} jest na miejscu o indeksie {last_index}"


list = [5, 3, 2, 6, 2, 1, 6, 7]
result = last_while(list, 6)
print(result)
print()


list2 = [1, 2, 2, 2, 3, 5, 8, 8, 9, 9, 11, 11, 34]
result2 = last_while(list2, 9)
print(result2)
print()


# ZADANIE 4
print("ZADANIE 4")


# sposób bez użycia pętli for (z pętlą while)

def last_sorted_while(list, x):
    last_index = None
    mid = 0
    start, end = 0, len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        if list[mid] == x:
            last_index = mid
            start = mid + 1  # powinien być while
        elif list[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return f"ostatnie wystąpienie liczby {x} jest na miejscu o indeksie {last_index}"


sorted_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6]
result = last_sorted_while(sorted_list, 6)
print(result)
print()


# sposób z pętlą for

def last_sorted_for(list, y):
    last_index = None
    start, end = 0, len(list)
    mid = (start + end) // 2

    for mid in range(start, end):
        if list[mid] == y:
            last_index = mid
        elif list[mid] > y:
            end = mid - 1
        else:
            start = mid + 1

    return f"ostatnie wystąpienie liczby {y} jest na miejscu o indeksie {last_index}"


sorted_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 8]
result = last_sorted_for(sorted_list, 6)
print(result)
print()


# ZADANIE 5
print("ZADANIE 5")


# sposób z pętlą for

def count_elements_for(list, x):
    smaller = 0
    equal = 0
    bigger = 0
    for element in list:
        if element < x:
            smaller += 1
        elif element == x:
            equal += 1
        else:
            bigger += 1
    return f"{smaller} mniejszych od {x}\n{equal} równych {x}\n{bigger} większych od {x}"


list = [1, 21, 5, 4, 3, 5, 5, 67, 7, 88, 29]
result = count_elements_for(list, 5)
print(result)
print()


# sposób bez użycia pętli for (z pętlą while)

def count_elements_while(list, y):
    smaller = 0
    equal = 0
    bigger = 0
    i = 0
    while i < len(list):
        if list[i] < y:
            smaller += 1
        elif list[i] == y:
            equal += 1
        else:
            bigger += 1
        i += 1
    return f"{smaller} mniejszych od {y}\n{equal} równych {y}\n{bigger} większych od {y}"


list = [1, 21, 5, 4, 3, 5, 5, 67, 7, 88, 29]
result = count_elements_while(list, 5)
print(result)
print()


# ZADANIE 6
print("ZADANIE 6")
print()

'''
def count_sorted_while(list, x):        # naprawić
    smaller, equal, bigger = 0, 0, 0
    start = 0
    end = len(list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if list[mid] < x:
            smaller += 1
            start = mid + 1
        elif list[mid] == x:
            equal += 1
            start = mid + 1
        else:
            bigger += 1
            end = mid - 1
    
    return f"{smaller} mniejszych od {x}\n{equal} równych {x}\n{bigger} większych od {x}"


list1 = [1, 2, 2, 3, 4, 5, 5, 5, 5, 5, 7, 9]
res = count_sorted_while(list1, 5)
print(res)
print()'''


# ZADANIE 7 wyznaczyć miejsce zerowe funkcji f(x) = x^3 - 2*x^2 + x - 7, przyjmuję, że znajduje się w przedziale [0, 3].
print("ZADANIE 7")


# f(0) = -7 i f(3) = 5
a = 0
b = 3
epsilon = 0.0001

while abs(a - b) > epsilon:
    root = (a + b) / 2

    if abs(root**3 - 2 * root**2 + root - 7) <= epsilon:
        break
    elif (root**3 - 2 * root**2 + root - 7) * (-455) < 0:  # f(x1) * f(a)
        b = root
    else:
        a = root

print(root)
print()


# ZADANIE 8
print("ZADANIE 8")


def does_sqrt_exist(lst, x):
    d, g = 1, x

    while d <= g:
        j = (d + g) // 2

        if j * j == x:
            return f"exists"
        elif j * j < x:
            d = j + 1
            # przesuwamy się w prawo jeżeli szukana wartość nie znajduje się po lewej
        else:
            g = j - 1
            # przesuwamy się w lewo jeżeli szukana wartość nie znajduje się po prawej

    return f"do not exist"


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
           14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
result = does_sqrt_exist(my_list, 23)
print(result)
print()


'''def does_sqrt_exist(lst, x):
    j = 1

    while j * j <= x:
        if j * j == x:
            return f"exists"
        elif j * j < x:
            j += 1

    return f"do not exist"


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
           14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
result = does_sqrt_exist(my_list, 9)
print(result)
print()'''


# ZADANIE 9
print("ZADANIE 9")


def sort_by_picking(lst):
    res_list = []

    while len(lst) > 0:
        max_elem = lst[0]

        # find max
        for i in range(len(lst)):
            if lst[i] > max_elem:
                max_elem = lst[i]
        
        lst.remove(max_elem)
        res_list.append(max_elem)

    return res_list[::-1]


my_list = [1, 6, 3, 8, 9, 8, 11]
res = sort_by_picking(my_list)
print(res)
print()


# ZADANIE 10
print("ZADANIE 10")
# [1, 6, 3, 8, 9] -> [(1, 6), 3, 8, 9] -> [1, (6, 3)->(3, 6), 8, 9] -> [1, 3, (6, 8), 9] -> [1, 3, 6, (8, 9)] -> [1, 3, 6, 8, 9]


def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                # auxiliary_variable = list[j + 1]
                # list[j + 1] = list[j]
                # auxiliary_variable = list[j]
    return list


list = [1, 6, 3, 8, 9, 8]
result = bubble_sort(list)
print(result)
print()
