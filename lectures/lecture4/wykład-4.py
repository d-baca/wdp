# WSTĘP DO PROGRAMOWANIA WYKŁAD 4

# tablica dwuwymiarowa z zagnieżdżonymi pętlami for

macierz = [[1, 2, 3],
              [4, 5, 6]]    # lista, której elementami są inne listy


print("\n----------- pętle zagnieżdżone - for - START ----------")

for wiersz in range(len(macierz)):
    for kolumna in range(len(macierz[wiersz])):
        print(macierz[wiersz][kolumna])

print("----------- pętle zagnieżdżone - for - END ----------")
print()


# definiowanie funkcji 

print("----------- przed zdefiniowaniem funkcji ------------")

def print_matrix(dowolna_macierz):
    for wiersz in range(len(dowolna_macierz)):
        for kolumna in range(len(dowolna_macierz[wiersz])):
            print(dowolna_macierz[wiersz][kolumna])
        print()
print()

print_matrix(macierz)
    
print("----------- po zdefiniowaniu i wywołaniu funkcji ------------")
print()


print_matrix([[-1, -2, -3], [-4, -5, -6]])
my_matrix = [[4], [8]]
print_matrix(my_matrix)


# definiowanie funkcji, która zwraca element o największej wartości 

print("----------- przed zdefiniowaniem funkcji ------------")
print()

def find_max(list):
    if len(list) == 0:
        return None 
    my_max = list[0]
    for element in range(len(list)):
        if list[element] > my_max:
            my_max = list[element]
    return my_max

list1 = [77, 3, -9, 23, 45, 9]

print(find_max(list1))
print(find_max([])) # -> nie zadziała, jeżeli nie zdefiniujemy przypadku, gdy lista jest pusta (ponieważ lista nie ma elementu o indeksie 0)
print()

print("----------- po zdefiniowaniu i wywołaniu funkcji ------------")
print()

result = find_max(list1)
print(result * 2)
print()
