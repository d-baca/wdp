# WSTĘP DO PROGRAMOWANIA WYKŁAD 7

# bubble sort

list = [7, 9, 2, 1, 10, 11, 5, 3, 7]

for j in range(len(list) - 1): # pętla "na zewnątrz"
    for i in range(len(list) - 1 - j):
        if list[i] > list[i + 1]:
            # print("zamieniam", tab[i], tab[i + 1])
            pom = list[i + 1]
            list[i + 1] = list[i]
            list[i] = pom
    print("etap", j, list)
print("finalny wynik", list)


# for j in range(len(tab) - 1):
#     for i in range(len(tab) - 1 - j):
#        print("zakres", 0, "-", i)
#     print()


# funkcja z wykładu 5


import random


def generate_random_list(length_min, length_max, min_elem, max_elem):
    length = random.randint(length_min, length_max)
    result = []
    for index in range(length):
        result.append(random.randint(min_elem, max_elem))
    return result


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

