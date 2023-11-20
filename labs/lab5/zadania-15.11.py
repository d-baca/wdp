# WEJŚCIÓWKA 15.11.2023
tab = [1, 2, 3, 4, 1, 2, 3, 4, 1, 0, 1]
x = 1
for i in range(len(tab)):
    if tab[i] == x:
        print(x, i)
print()

# -------------------------------------

# ZADANIE 1
print("ZADANIE 1")

num_list = [12, 4, 37, 84, 9, 92, 201]
for index in range(len(num_list)):
    if index % 2 == 0:
        print(num_list[index])
print()


# ZADANIE 2
print("ZADANIE 2")

words_list = ["abc", "cdef", "ghij", "kjkl"]
for word in words_list:
    print([[word, len(word)]], end=" ")
print()


# ZADANIE 3
print()
print("ZADANIE 3")

num_list = [1, 5, 3, 6, 4]
n = 4
for num in num_list:
    if n == num:
        print("TAK")
    elif n not in num_list:
        print("NIE")
        break
print()


# ZADANIE 4
print("ZADANIE 4")

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# for index in range(len(list)):
#    list[index].reverse()
# print(list)
# print()

reversed_list = []
for index in list:
    reversed_list.append(index[::-1])
print(reversed_list)
print()

# ZADANIE 5
print("ZADANIE 5")

list = ["pierwszy", "drugi", "trzeci", "ostatni"]
print(list)
list[0], list[-1] = list[-1], list[0]
print(list)
print()


# ZADANIE 6
print("ZADANIE 6")

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

diagonal_sum = 0
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if row == column:
            diagonal_sum += matrix[row][column]
print(diagonal_sum)
print()


# ZADANIE 7
print("ZADANIE 7")

matrix = [[1, 2, 4, 6],
          [2, 3, 4, 5],
          [12, 3, 4, 5]]

# tworzy nową macierz wynikową
result_matrix = [[0 for result_column in range(
    len(matrix[0]))] for result_row in range(len(matrix))]
scalar = 3

# mnoży każdy element macierzy przez podany skalar
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        result_matrix[row][column] = matrix[row][column] * scalar

# wyświetla wynik mnożenia macierzy przez skalar
for final_row in result_matrix:
    print(final_row)
print()

# ---------------------------------------------------- ALBO ----------------------------------------------------
# Mnoży każdy element macierzy przez podany skalar
# result_matrix = [[element * scalar for element in row] for row in matrix]

# Wyświetla wynik mnożenia macierzy przez skalar
# for final_row in result_matrix:
#     print(final_row)


# ZADANIE 8
print("ZADANIE 8")

num_list = []
reversed_list = []
for i in range(1, 21):
    num_list.append(i)
num_list2 = num_list[::-1]
num_list3 = [num_list, num_list2]
print(num_list3)
print()


# ZADANIE 9
print("ZADANIE 9")

list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

# list1.pop()
# for index in range(len(list2)):
#    list1.append(list2[index])
# print(list1)

list1[-1:] = list2
print(list1)
print()


# ZADANIE 10
print("ZADANIE 10")

matrix = [[1, 5, 8],
          [6, 4, 1],
          [4, 8, 9]]

# max_sum = sum(matrix[0][j] for j in range(len(matrix[0])))
# max_sum = matrix[0][0] + matrix[0][1] + matrix[0][2]

# min_sum = sum(matrix[0][j] for j in range(len(matrix[0]))) # min_sum = matrix[0][0] + matrix[0][1] + matrix[0][2]
# min_sum = matrix[0][0] + matrix[0][1] + matrix[0][2]

# ustala wartość maksymalnej sumy na sumę elementów pierwszej listy w macierzy
max_sum = 0
for element in matrix[0]:
    max_sum += element

# ustala wartość minimalnej sumy na sumę elementów pierwszej listy w macierzy
min_sum = 0
for element in matrix[0]:
    min_sum += element

# znajduje sumę maksymalną i minimalną
for i in range(len(matrix)):
    row_sum = 0
    for j in range(len(matrix[i])):
        row_sum += matrix[i][j]

    # aktualizuje maksymalną i minimalną sumę
    if row_sum > max_sum:
        max_sum = row_sum
    if row_sum < min_sum:
        min_sum = row_sum

print("Suma maksymalna:", max_sum)
print("Suma minimalna:", min_sum)
print()


# ZADANIE 11
print("ZADANIE 11")
print()

matrix = [[7, 2, 8, -1],
          [1, 3, 2, 0],
          [-5, 9, 5, -7]]

transposed_matrix = []

# iteruje po kolumnach oryginalnej macierzy
for i in range(len(matrix[0])):
    # inicjalizuje pusty wiersz dla macierzy transponowanej
    transposed_row = []

    # iteruje po wierszach oryginalnej macierzy
    for j in range(len(matrix)):
        # dodaje element z macierzy oryginalnej do macierzy transponowanej
        transposed_row.append(matrix[j][i])

    # dodaje transponowany wiersz do macierzy transponowanej
    transposed_matrix.append(transposed_row)

# wyświetla macierz oryginalną
print("Macierz oryginalna:")
for row in matrix:
    print(row)
print()

# wyświetla macierz transponowaną
print("Macierz transponowana:")
for row in transposed_matrix:
    print(row)


# lista comprehension
# transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# for row in transposed_matrix:
#     print(row)
print()


# ZADANIE 12
print("ZADANIE 12")

num_list = [4, 3, 8, 7, 9, 9]
max_value = num_list[0]
second_max_value = num_list[0]

for element in range(len(num_list)):
    if num_list[element] > max_value:
        max_value, second_max_value = num_list[element], max_value
    elif num_list[element] > second_max_value and num_list[element] != max_value:
        second_max_value = num_list[element]
print(second_max_value)
print()


# ZADANIE 13
print("ZADANIE 13")

import random
list = []
for i in range(10):
    list.append(random.randint(1, 100))
print("Losowo wygenerowana lista liczb:", list)
print()

# bubble sort
list_length = len(list)
while list_length > 1:
    swap = False
    for i in range(0, list_length - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            swap = True
    list_length -= 1
    if swap == False:
        break
print("Losowo wygenerowana i posortowana lista liczb:", list)
print()

# ZADANIE 14
print("ZADANIE 14")

list1 = [1, 4, 13, 34, 78]
list2 = [3, 5, 20, 87, 200]
list3 = list1 + list2

# bubble sort
list_length = len(list3)
while list_length > 1:
    swap = False
    for i in range(0, list_length - 1):
        if list3[i] > list3[i + 1]:
            list3[i], list3[i + 1] = list3[i + 1], list3[i]
            swap = True
    list_length -= 1
    if swap == False:
        break
print(list3)

