# WEJŚCIÓWKA

def last_index(list, char):
    i = 0
    index = []

    while i < len(list):
        if list[i] == char:
            index.append(i)
        i += 1

    if len(index) == 0:
        return -1
    else:
        index = index[-1]
        return index


print(last_index([1, 2, 3, 2, 2], 2))


# def replace_char(list, index, replace_char):
# zamienić zadany element z ostatnim indeksem z poprzedniej funkcji (użyć ją) na wprowadzony znak

