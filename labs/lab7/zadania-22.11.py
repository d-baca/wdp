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
            start = mid + 1
        elif list[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return f"ostatnie wystąpienie liczby {x} jest na miejscu o indeksie {last_index}"


sorted_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7]
result = last_sorted_while(sorted_list, 7)
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


sorted_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6]
result = last_sorted_for(sorted_list, 4)
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


def count_sorted(sorted_lst, x):
    # w tej funkcji (głównej) zebrane są wszystkie informacje, tzn. ile równych x, mniejszych od x, większych od x.
    if x > sorted_lst[-1]:
        return len(sorted_lst), 0, 0
    elif x < sorted_lst[0]:
        return 0, 0, len(sorted_lst)

    def first_occurrence_function(lst, target):
        # wyszukuje indeks pierwszego wystąpienia wartości target w posortowanej liście.
        # jeśli target nie istnieje, zwraca 0.

        start = 0
        end = len(lst) - 1
        first_occurrence = 0

        while start <= end:
            mid = (start + end) // 2

            if lst[mid] < target:
                start = mid + 1
            elif lst[mid] == target:
                first_occurrence = mid
                end = mid - 1  # przesuwamy się do "lewej" strony listy
            else:
                end = mid - 1

        return first_occurrence  # pierwsze wystąpienie wartości target
    

    def last_occurrence_function(lst, target):
        # wyszukuje indeks ostatniego wystąpienia wartości target w posortowanej liście.
        # jeśli target nie istnieje, zwraca 0.

        start = 0
        end = len(lst) - 1
        last_occurrence = 0

        while start <= end:
            mid = (start + end) // 2

            if lst[mid] < target:
                start = mid + 1
            elif lst[mid] == target:
                last_occurrence = mid
                start = mid + 1  # przesuwamy się do "prawej" strony listy
            else:
                end = mid - 1

        return last_occurrence  # ostatnie wystąpienie wartości target
             
    def count_occurrences_function(lst, target):
        # zlicza liczbę wystąpień wartości target w liście (posortowanej).

        first_occurrence = first_occurrence_function(lst, target)
        last_occurrence = last_occurrence_function(lst, target)

        if first_occurrence != 0 and last_occurrence != 0:
            return last_occurrence - first_occurrence + 1
        else:
            return 0

    count_smaller = first_occurrence_function(sorted_lst, x)
    count_equal = count_occurrences_function(sorted_lst, x)
    count_bigger = len(sorted_lst) - last_occurrence_function(sorted_lst, x) - 1


    return count_smaller, count_equal, count_bigger


sorted_list = [1, 2, 2, 3, 4, 5, 5, 5, 5, 5, 7, 9]
x = 6
res = count_sorted(sorted_list, x)
print(f"Liczba elementów mniejszych od {x}: {res[0]}")
print(f"Liczba elementów równych {x}: {res[1]}")
print(f"Liczba elementów większych od {x}: {res[2]}")
print()


# ZADANIE 7 wyznaczyć miejsce zerowe funkcji f(x) = x^3 - 2*x^2 + x - 7, przyjmuję, że znajduje się w przedziale [0, 3].
print("ZADANIE 7")


# f(0) = -7 i f(3) = 5
a = 0
b = 3

# f(-7)
c = -7

epsilon = 0.0001
    
while abs(a - b) > epsilon:
    root = (a + b) / 2

    if abs(root**3 - 2 * root**2 + root - 7) <= epsilon:
        break
    elif (root**3 - 2 * root**2 + root - 7) * (c**3 - 2 * c**2 + c - 7) < 0:  # f(x1) * f[f(a)]
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
            # przesuwamy się w prawo jeżeli szukana wartość nie znajduje się po "lewej"
        else:
            g = j - 1
            # przesuwamy się w lewo jeżeli szukana wartość nie znajduje się po "prawej"

    return f"do not exist"


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
           14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
result = does_sqrt_exist(my_list, 23)
print(result)
print()

'''
# linear search

def does_sqrt_exist(lst, x):
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
print()
'''

# ZADANIE 9
print("ZADANIE 9")


# sposób bez użyca .append i .remove


def sort_by_picking_max(lst):
    n = len(lst)

    for i in range(n - 1, 0, -1):
        max_index = 0
        
        for j in range(1, i + 1):
            if lst[j] > lst[max_index]:
                max_index = j

        lst[i], lst[max_index] = lst[max_index], lst[i]
    
    return lst


my_list = [1, 6, 3, 8, 9, 8, 11]
res = sort_by_picking_max(my_list)
print(res)
print()

'''
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
'''

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


# ZADANIE 11
print("ZADANIE 11")

# sposób z pętlą for


def circular_shift(lst, k):
    n = len(lst)
    # shifted_lst = [0] * n
    shifted_lst = []

    for index in range(n):
        # shifted_lst[(index + k) % n] = lst[index]
        shifted_lst.append(lst[(index + (-k)) % n])

    return shifted_lst


my_list = [1, 6, 3, 8, 9, 8, 11, 14]
res = circular_shift(my_list, 2)
print(my_list)
print(res)
print()


# sposób bez użycia pętli for (z pętlą while)

def circular_shift_while(lst, k):
    n = len(lst)
    shifted_lst = []
    index = 0

    while index <= n:
        shifted_lst.append(lst[(index + (-k)) % n])

    return shifted_lst


my_list = [1, 6, 3, 8, 9, 8, 11, 14]
res = circular_shift(my_list, 2)
print(my_list)
print(res)
print()
