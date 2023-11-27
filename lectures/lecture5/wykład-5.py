# WSTĘP DO PROGROGRAMOWANIA WYKŁAD 5

# definiowanie funkcji, która zwraca element o największej wartości i najmniejszej wartości

import random
print()
print(":::::::::: min max function ::::::::::")


def min_max(a_list):
    if len(a_list) == 0:
        return None
    my_min = a_list[0]
    my_max = a_list[0]
    for element in a_list:
        if element <= my_min:
            my_min = element
        if element >= my_max:
            my_max = element
    # TUPLE - krotka
    return (my_min, my_max)


(a_min, a_max) = min_max([1, 64, 18, 19, 3, -6])
print(a_min, a_max)
print()


# funkcje z biblioteki, pakietu (nie są globalne, domyślne)
print(":::::::::: random number generator ::::::::::")
print(random.randint(0, 54))
print()


print(":::::::::: random list generator function ::::::::::")


def generate_random_list(length_min, length_max, min_elem, max_elem):
    length = random.randint(length_min, length_max)
    result = []
    for index in range(length):
        result.append(random.randint(min_elem, max_elem))
    return result


list1 = generate_random_list(0, 5, -10, 10)
list2 = generate_random_list(1, 10, -100, 100)
list3 = generate_random_list(5, 20, 0, 10)

print(list1)
print(min_max(list1))
print()

print(list2)
print(min_max(list2))
print()

print(list3)
print(min_max(list3))
print()


# zadanie domowe - generator macierzy, który podaje liczbę wierszy i kolumn oraz zakresy
print(":::::::::: random matrix generator function ::::::::::")


def matrix_generator(min_length, max_length, min_element, max_element):
    length = random.randint(min_length, max_length)
    result_matrix = []
    for i in range(length):
        row_values = []
        for j in range(length):
            row_values.append(random.randint(min_element, max_element))
        result_matrix.append(row_values)
    return result_matrix


matrix1 = matrix_generator(2, 6, -10, 10)
print(matrix1)
print()


# napisz funkcję, która sprawdza, czy lista zawiera zadany element

print(":::::::::: find if element is in list function ::::::::::")


def if_contains(list, element):
    result = False
    for e in list:
        if e == element:
            result = True
    return result

# wersja zoptymalizowana funkcji


def if_contains2(list, element):
    for e in list:
        if e == element:
            return True
    return False


element = random.randint(0, 5)
print(list1, element)
print(if_contains2(list1, element))
print()


# napisz funkcję, która zwróci co drugi element z listy

print(":::::::::: return every two elements from list function ::::::::::")


def every_two_elements(list):
    result = []
    for index in range(0, len(list), 2):
        # if index % 2 == 0:              # można pozbyć się if'a poprzez krok w range'u
        result.append(list[index])
    return result


list = generate_random_list(8, 20, -10, 10)
print(list)
print(every_two_elements(list))
print()


print(":::::::::::::: bubble sort ::::::::::::::")

def bubble_sort(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1 - j):
            if list[i] > list[i + 1]:
                pom = list[i + 1]
                list[i + 1] = list[i]
                list[i] = pom


# optymalizacja (czysta funkcja)

def bubble_sort2(a_list):
    list = a_list.copy() # shallow copy
    for j in range(len(list) - 1):
        for i in range(len(list) - 1 - j):
            if list[i] > list[i + 1]:
                pom = list[i + 1]
                list[i + 1] = list[i]
                list[i] = pom
    return list

list1 = generate_random_list(0, 5, -10, 10)
list2 = generate_random_list(1, 10, -100, 100)
list3 = generate_random_list(5, 20, 0, 10)


print("oryginalna lista:",list3)
list3_ory = list3.copy()
list3.sort()
print("posortowana metodą sort():",list3)
print("posortowana metodą bubble_sort2:",bubble_sort2(list3_ory))
