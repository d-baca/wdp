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
'''

# ZADANIE 2

print()
print("ZADANIE 2")
vowel_list = ["a", "ą", "e", "ę", "i", "o", "u" "ó",
              "y", "A", "Ą", "E", "Ę", "I", "O", "U", "Ó", "Y"]
word = "RabArBAr"
i = 0
for vowel in word:
    if vowel in vowel_list:
        i += 1
print("ilość samogłosek w słowie wynosi:", i)
print()


# ZADANIE 3

print("ZADANIE 3")
num_list = [23, 65, 28, 2, 4, 94]
sum = 0
for num in num_list:
    sum += num
print(sum)
print()


# ZADANIE 4

print("ZADANIE 4")
num_list = [2, 7, 10, 4]
mul = 1
for num in num_list:
    mul *= num
print(mul)
print()


# ZADANIE 5

print("ZADANIE 5")
num_list = [2, 84, 271, 8, 591]
max_element = num_list[0]
for element in range(len(num_list)):
    if num_list[element] > max_element:
        max_element = num_list[element]
print(max_element)
print()


# ZADANIE 6

print("ZADANIE 6")
num_list = [235, 434, 124, 850, 321]
min_element = num_list[0]
for element in range(len(num_list)):
    if num_list[element] < min_element:
        min_element = num_list[element]
print(min_element, num_list.index(min_element))
print()


# ZADANIE 7

print("ZADANIE 7")
num_list = [4, 7, 2, 9, 6, 8]
max_element = num_list[0]
second_max_element = num_list[0]
for element in range(len(num_list)):
    if num_list[element] > max_element:
        max_element = num_list[element]
    elif num_list[element] > second_max_element:
        second_max_element = num_list[element]
print(second_max_element, num_list.index(second_max_element))
print()

# ZADANIE 8

print("ZADANIE 8")
print()
words_list = ["laptop", "butelka", "lampa", "ala", "jo"]
for word in words_list:
    if len(word) > 3:
        print(word)
print()


# ZADANIE 9

print("ZADANIE 9")
list1 = ["butelka", 289, 27, "telefon"]
list2 = [8848, "biurko", 345, "butelka"]
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

print("ZADANIE 10")
num_list = [12, 483, 2821, 248, 76]
for num in num_list:
    if num % 2 != 0:
        print(num, end=" ")
print()


# ZADANIE 11

print()
print("ZADANIE 11")
jedności = ["", "jeden", "dwa", "trzy", "cztery",
            "pięć", "sześć", "siedem", "osiem", "dziewięć"]
nastki = ["", "jedenaście", "dwanaście", "trzynaście", "czternaście",
          "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"]
dziesiątki = ["", "dziesięć", "dwadzieścia", "trzydzieści", "czterdzieści",
              "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
setki = ["", "sto", "dwieście", "trzysta", "czterysta",
         "pięćset", "sześćset", "siedemset", "osiemset", "dziewięćset"]
liczba = 372

for liczba in range(liczba, liczba + 1):
    słownie = ""

    # Zapisanie oryginalnej liczby
    oryginalna_liczba = liczba

    # Konwersja setek
    słownie += setki[liczba // 100] + " "
    liczba %= 100

    # Konwersja dziesiątek i jedności
    if liczba >= 10 and liczba < 20:
        słownie += nastki[liczba - 10]
        liczba = 0  # Zerujemy liczbę, bo już obsłużyliśmy jednostki w przypadku nastek
    else:
        słownie += dziesiątki[liczba // 10] + " "
        liczba %= 10
        słownie += jedności[liczba]

    print(oryginalna_liczba, "=", słownie)
print()


# ZADANIE 12

print("ZADANIE 12")
word = "rabarbar"
pattern = "ab"

found = False

for i in range(len(word) - len(pattern) + 1):
    match = True
    for j in range(len(pattern)):
        if word[i + j] != pattern[j]:
            match = False
            break
    if match:
        found = True
        break

if found:
    print("TAK")
else:
    print("NIE")
print()


# ZADANIE 13

print("ZADANIE 13")
palindromes = ["kajak", "anna", "oko", "afsasf"]

for word in palindromes:
    for i in range(len(word) // 2):
        if word[i] == word[len(word) - 1 - i]:
            print("słowo", word, "to palindrom.")
            break
    else:
        print("słowo", word, "to nie palindrom.")
print()


# ZADANIE DODATKOWE 1
print("ZADANIE DODATKOWE 1")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 6, 4, 2, 9, 11, 34, 3, 2, 2, 2, 5]
common_elements = 0

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            common_elements += 1
            break

print(common_elements)
print()


# ZADANIE DODATKOWE 2
print("ZADANIE DODATKOWE 2")

