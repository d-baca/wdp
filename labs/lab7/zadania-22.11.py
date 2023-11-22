# binary search

import random


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


import random


def generate_random_list(n):
    result_list = []
    for i in range(n):
        result_list.append(random.randint(1, 100))
    return result_list


print(generate_random_list(5))
print()


# ZADANIE 2
print("ZADANIE 2")


def generate_random_sorted_list(n):
    result_list = []
    result_list.append(random.randint(1,10))
    for i in range(1, n):
        result_list.append(random.randint(i - 1, 2 * (i - 1)))
    return result_list 


print(generate_random_sorted_list(5))
print()


# ZADANIE 3
print("ZADANIE 3")

def last_rep(list, x):
    list2 = []
    # odwraca listę 
    for i in range(len(list) - 1, -1, -1):
        list2.append(list[i])
        # wyszukuje pierwszy powtarzający się element na odwróconej liście 
        # (czyli ostatni na oryginalnej liście)
        if i == x:                          
            print(list2[x])             


list = [1, 2, 3, 2, 2]
#          ^ 
#          |

result = last_rep(list, 2)
print(result)
