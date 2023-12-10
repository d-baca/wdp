# ZADANIE 1
print()
print("ZADANIE 1")  # lst = [1,3,5,7,9,2] daje wynik lst = [1,2,3,5,7,9]


def insert_element(lst):
    last_element = lst[len(lst) - 1]

    for i in reversed(range(len(lst) - 1)):
        if last_element >= lst[i]:
            lst[i + 1] = last_element
            return lst
            break
        elif last_element < lst[i]:
            if i != 0:
                lst[i + 1] = lst[i]
            elif i == 0:
                lst[i + 1] = lst[i]
                lst[i] = last_element

    return lst


my_lst = [1, 3, 5, 7, 9, -1]
res = insert_element(my_lst)
print(res)
print()


# ZADANIE 2
print("ZADANIE 2")


def sort_inserted_elements(lst):
    res_list = [lst[0]] # lista z pierwszym elementem

    for i in range(1, len(lst)):
        res_list.append(lst[i])
        res_list = insert_element(res_list)
        # print(res_list)

    return res_list

my_lst2 = [1, 3, 5, 7, 9, 0]
res = sort_inserted_elements(my_lst2)
print(res)
print()


# ZADANIE 3 - ZROBIĆ ZE SWAPEM!
print("ZADANIE 3")

char_list = ["b", "b", "c", "c", "c", "c", "c", "c", "c", "b", "b", "b", "c"]
b_list = []
c_list = []

for char in range(len(char_list)):

    if char_list[char] == "b":
        b_list.append(char_list[char])

    elif char_list[char] == "c":
        c_list.append(char_list[char])
        
print(b_list + c_list)
print()


# ZADANIE 4
print("ZADANIE 4")


nested_lists = [[1, 2, 3, 4, 5], [5, 2, 3, 4, 1], [6, 7, 3, 14]]




