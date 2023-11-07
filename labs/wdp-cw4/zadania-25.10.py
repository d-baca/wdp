'''# ZADANIE 1
#a)
napis="ala ma kotA"
print(napis[0])
print(napis[2])
print(napis[1:3])
print(napis[1::3])
print(napis[::])
print(len(napis))
print(napis.lower())
print(napis.count(" "))

#b)
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [1, 3, 4, 5, 9]
print(lista1, lista2)
lista3 = [lista1, lista2]
lista4 = lista1 + lista2
print(lista3)
print(lista4)


#c)
lista1 = [1, 2, 3, 4, 5, 6]
for i in lista1:
    print(i)
for i in range(len(lista1)):
    print(lista1[i])


#d) 
import random 
print(random.randint(3, 9))


#e)
import random
lst = []
for i in range(10):
    lst.append(random.randint(1, 10))
# Prints random items
print(lst)


# ZADANIE 2

print()
samogłoski = ["a", "A", "ą", "Ą", "e", "E", "ę", "Ę", "i", "I", "o", "O", "u", "U", "ó", "Ó", "y", "Y"]
słowo = "DaniEl"
i = 0

for znak in słowo:
    if znak in samogłoski:
        i += 1
print("ilość samogłosek w słowie wynosi:", i)
print()


# ZADANIE 3

numbers_list = [1, 2, 4, 6, 8, 9]
sum = 0

for number in numbers_list:
    sum += number
print("suma elementów należących do listy wynosi:", sum)
print()


# ZADANIE 4

numbers_list = [1, 2, 4, 6, 8, 9]
mul = 1

for number in numbers_list:
    mul *= number
print("iloczyn elementów należących do listy wynosi:", mul)
print()


# ZADANIE 5

numbers_list = [1, 6, 12, 45, 89]
print("Największa wartość należąca do danej listy liczb wynosi:", max(numbers_list))
print()


# ZADANIE 6

numbers_list = [1, 6, 12, 45, 89]
min_value = min(numbers_list)

print("Najmniejsza wartość należąca do danej listy liczb wynosi:", min_value, "oraz jej indeks to:", numbers_list.index(min_value))
print()


# ZADANIE 7

numbers_list = [4, 7, 2, 9, 6, 8]
max_value1 = numbers_list[0]
max_value2 = 0

for number in numbers_list:
    if number > max_value1:
        max_value1, max_value2 = number, max_value1
    elif number > max_value2:
        max_value2 = number
print("Druga największa wartość na liście wynosi:", max_value2,
      "oraz jej indeks to:", numbers_list.index(max_value2))
print()


# ZADANIE 8

words_list = ["jeden", "dwa", "trzy", "cztery", "pięć"]

for word in words_list:
    if len(word) > 3:
        print(word, end=", ")
print()

# ZADANIE 9

list1 = [1, 56, 90, "a", "b", "c"]
list2 = [4, 89, 90, "c", "d", "e"]

similar_element = 0

for element in list1:
    if element in list2:
        similar_element = 1
if similar_element == 1:
    print("TAK")
else:
    print("NIE")
print()


# ZADANIE 10

numbers_list = [1, 4, 7, 8, 9, 11]

odd_numbers = []

for number in numbers_list:
    if number % 2 != 0:
        odd_numbers.append(number)
print(odd_numbers)
print()


# ZADANIE 11

.


# ZADANIE 12

.

'''
# ZADANIE 13

words_list = ["radar", "potop", "zakaz", "kajak", "zaraz"]

#palindromes = []

#for word in words_list:
#    if 
