# WSTĘP DO PROGRAMOWANIA WYKŁAD 3 

# pętle z wykorzystaniem polecenia while

message = "Hello " + " World!"

liczba_powtorzen = len(message)
licznik = 0

print("----------- przed pętlą -----------")
while licznik < liczba_powtorzen:
    print("wykonuję", licznik, "iterację")
    print("DZISIAJ JEST PIĄTEK")
    licznik += 1 
print("------------ po pętli ------------")



# tworzenie list

lista = ["jeden", "dwa", "trzy", "cztery"]

print("ilość elementów na liście wynosi:", len(lista))
print("pierwszy element na liście to:", lista[0])
print("drugi element na liście to:", lista[1])
print("ostatni element na liście to:", lista[-1]) 
# print(lista[4]) ELEMENT NIE ISTNIEJE! (out of range)
# ostatni element może zostać wywołany poprzez następujące polecenie: print(lista[len(lista - 1)])


index = 0

print("----------- przed pętlą - indeksy z while -----------")
while index < len(lista):
    print(lista[index], end=" ")
    index += 1
print("\n------------ po pętli - indeksy z while ------------")



# pętle z wykorzystaniem polecenia for 

print("\n----------- przed pętlą - indeksy z for -----------")
for i in range(len(lista)):
    print(lista[i], end=" ")
print("\n------------ po pętli - indeksy z for ------------")

# print(list(range(1, 10)))



# tablica dwuwymiarowa

macierz2x3 = [[1, 2, 3],
              [4, 5, 6]]    # lista, której elementami są inne listy

#print(macierz2x3[0][1])

index_wiersz = 0 
index_kolumna = 0
while index_wiersz < len(macierz2x3):
    print("wiersz:", macierz2x3[index_wiersz])
    index_kolumna = 0
    while index_kolumna < len(macierz2x3[index_wiersz]):
        print(macierz2x3[index_wiersz][index_kolumna])
        index_kolumna += 1
    index_wiersz += 1







