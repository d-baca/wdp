'''matrix = []
n = 13

for i in range(1, n+1):
    row = []
    for j in range(1, i+1):
        row.append(j)
    matrix.append(row)

for row in matrix:
    while len(row) != n:
        row.append("")

print(matrix)'''


# ZADANIE 1
print("ZADANIE 1")


def greater_num(a, b):
    if a > b:
        return a
    elif a == b:
        return "podane wartości są takie same"
    else:
        return b


result = greater_num(5, 7)
print(result)
print()


# ZADANIE 2
print("ZADANIE 2")

result1 = greater_num(8, 3)
result2 = greater_num(result1, 5)
print(result2)
print()


# ZADANIE 3
print("ZADANIE 3")


def list_elements_sum(list):
    elem_sum = 0
    for elem in list:
        elem_sum += elem
    return elem_sum


list1 = [1, 2, 3, 4, 5]
result = list_elements_sum(list1)
print(result)
print()


# ZADANIE 4
print("ZADANIE 4")


def list_elements_mul(list):
    elem_mul = 1
    for elem in list:
        elem_mul *= elem
    return elem_mul


list1 = [1, 2, 3, 4, 5]
result = list_elements_mul(list1)
print(result)
print()


# ZADANIE 5
print("ZADANIE 5")


def reversed_word_function(word):
    reversed_word = word[::-1]
    return (reversed_word)


word = "wirus"
result = reversed_word_function(word)
print(result)
print()

# ------------ drugi sposób (bez użycia ::-1) ------------ 

def reversed_string_function(original_string):
    reversed_string = ""

    for char in original_string:
        reversed_string = char + reversed_string

    return reversed_string

original_string = "wirus"
result = reversed_string_function(original_string)
print(result)
print()


# ZADANIE 6
print("ZADANIE 6")


def is_in_range(number):
    if number in range(1, 1001):
        return True
    else:
        return False


number = 345
result = is_in_range(number)
print(result)
print()


# ZADANIE 7
print("ZADANIE 7")


def no_duplicates_function(list_with_duplicates):
    list_without_duplicates = []

    for i in range(len(list_with_duplicates)):
        is_duplicate = False

        for j in range(i):
            if list_with_duplicates[j] == list_with_duplicates[i]:
                is_duplicate = True
                break

        if is_duplicate == False:
            list_without_duplicates.append(list_with_duplicates[i])

    return list_without_duplicates


list = [1, 1, 1, 4, 7, 3, 2, 2, 4]
result = no_duplicates_function(list)
print(result)
print()


# ZADANIE 8
print("ZADANIE 8")


def is_prime(number):
    num_of_divisors = 0
    for i in range(1, number + 1):
        if number % i == 0:
            num_of_divisors += 1

    if num_of_divisors == 2:
        return True
    else:
        return False


number = 13
result = is_prime(number)
print(result)
print()


# ZADANIE 9
print("ZADANIE 9")


def even_elements_function(list):
    even_elements_list = []
    for i in list:
        if i % 2 == 0:
            even_elements_list.append(i)
    return even_elements_list


list1 = [1, 5, 32, 23, 6, 2]
result = even_elements_function(list1)
for even in result:
    print(even)
print()


# ZADANIE 10
print("ZADANIE 10")


def is_pangram(pangram):
    alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    is_or_no = True

    for char in alphabet_list:
        if char not in pangram:
            is_or_no = False
            break
        
    return is_or_no


pangram_test = "The quick brown fox jumps over the lazy dog"
result = is_pangram(pangram_test)
print(result)
print()


# ZADANIE 11
print("ZADANIE 11")


def years_to_minutes_converter(years):
    year_to_minutes = 525948766
    convertion = years * year_to_minutes
    print(years, "lat(a) to", convertion, "minut")


years_to_minutes_converter(1)
print()


# ZADANIE 12
print("ZADANIE 12")
print()
# def is_sorted(list):
    
# list = [1, 2, 4, 7, 3, 2, 1, 8]

# ZADANIE 13
print("ZADANIE 13")


def if_contains(list, element):
    result = False
    for i in list:
        if i == element:
            result = True
    return result


element = 5
list = [1, 2, 6, 3, 8, 9, 0, 4, 5]
result = if_contains(list, element)
print(result)
print()


# ZADANIE 14
print("ZADANIE 14")


def if_sorted_list_contains(list, element):
    # binary search
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == element:
            return mid
        elif list[mid] > element:
            high = mid - 1
        else:
            low = mid + 1
    return False


list = [1, 23, 45, 72, 530, 891, 926]
element = 891
result = if_sorted_list_contains(list, element)
print("element znajduje się na liście na miejscu:", result)
print()


# ZADANIE 15
print("ZADANIE 15")


def replace_two_elements(list):
    list[2], list[4] = list[4], list[2]
    return list


list = [1, 2, 3, 4, 5]
result = replace_two_elements(list)
print(result)
print()


# ZADANIE 16
# suma długości dowolnie wybranych dwóch odcinków będzie większa od długości trzeciego z odcinków
print("ZADANIE 16")


def is_positive(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return "wszystkie wprowadzone liczby są dodatnie"
    else:
        return "któraś liczba jest ujemna, wszystkie muszą być dodatnie!"


def triangle_function(a, b, c):
    positive_result = is_positive(a, b, c)
    print(positive_result)
    
    if a + b > c and a + c > b and b + c > a:
        return 1
    else:
        return 0


result = triangle_function(10, 10, 10)
print(result)
print()