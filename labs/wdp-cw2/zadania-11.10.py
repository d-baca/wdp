# ZADANIE 2: Napisz program, który policzy silnię podanej liczby naturalnej n (1 · 2 · · · · · n) przy użyciu pętli while.

n = 5
i = 1
silnia = 1

while i < n:
    silnia = silnia * (i + 1)
    i = i + 1

print("silnia podanej liczby wynosi: ", silnia)


# ZADANIE 3: Napisz program, który policzy sumę liczb od 1 do n, gdzie n jest podaną liczbą naturalną przy użyciu pętli while.

n = 5
i = 1
suma = 0

while i <= n:
    suma = suma + i
    i = i + 1

print("suma wynosi: ", suma)


# ZADANIE 4: Napisz program, który policzy sumę kwadratów liczb od 1 do n, gdzie n jest podaną liczbą naturalną (1^2 + 2^2 + . . . n^2)
#           (w rozwiązaniu można użyć tylko operatorów porównania, "+", "*” oraz tylko pętli while).

n = 3
i = 1
suma = 0

while i <= n:
    suma = suma + (i ** 2)
    i = i + 1

print("suma kwadratów wynosi: ", suma)


# ZADANIE 5: Napisz program, który policzy sumę sześcianów liczb od 1 do n, gdzie n jest podaną liczbą naturalną (1^3 + 2^3 + . . . n^3)
#           (w rozwiązaniu można użyć tylko operatorów porównania, "+", "*” oraz tylko pętli while).

n = 5
i = 1
suma = 0

while i <= n:
    suma = suma + (i ** 3)
    i = i + 1

print("suma sześcianów wynosi: ", suma)


# ZADANIE 6: Napisz program, który dla zadanej liczby n znajdzie liczbę jej dzielników.

n = 15
i = 1
dzielniki = 0

while i <= n:
    if n % i == 0:
        dzielniki = dzielniki + 1
    i = i + 1

print("ilość dzielników liczby n wynosi: ", dzielniki)


# ZADANIE 7: Napisz program, który dla podanych liczb a i b znajdzie liczbę znaków sumy a+b. (Nie korzystaj z funkcji len())

a = 5
b = 6
suma = a + b
znaki = 0

while suma > 0:
    suma = suma // 10
    znaki = znaki + 1

print("ilość znaków sumy liczb a i b wynosi: ", znaki)


# ZADANIE 8: Napisz program, który dla zadanej liczby n, następnie wyznaczy największą liczbę m taką, że: 1 + 2 + 3 + ... + m ≤ n (przy użyciu pętli while).

n = 10
i = 1
suma = 0
m = 0

while suma <= n:
    suma = suma + i
    m = i - 1
    i = i + 1

print("liczba m wynosi: ", m)


# ZADANIE 9: Napisz program, który dla zadanej liczby całkowitej w systemie dwójkowym wyświetli jej odpowiednik
#           w systemie dziesiątkowym. Wykonaj to zadanie bez korzystania z wbudowanych funkcji przeliczających
#           na inny system liczbowy.

liczba_dwójkowa = 1101
liczba_dziesiętna = 0
i = 1

while liczba_dwójkowa != 0:
    reszta = liczba_dwójkowa % 10
    liczba_dziesiętna = liczba_dziesiętna + (reszta * i)
    i = i * 2
    liczba_dwójkowa = int(liczba_dwójkowa / 10)

print("odpowiednik podanej liczby w systemie dziesiątkowym wynosi: ", liczba_dziesiętna)


# ZADANIE 10: Napisz program, który wyświetli wszystkie liczby mniejsze od 100 oraz większe od 1 które przy dzieleniu
#            przez 5 dają resztę 1 oraz przy dzieleniu przez 7 dają resztę 3.

n = 100
i = 1
# out = ''

while i < n:
    i = i + 1
    if i % 5 == 1 and i % 7 == 3:
        print(i, end=", ")
        # out += f'{i}, '

# print(out)


# ZADANIE DODATKOWE: Implementacja schematu mnożenia rosyjskich chłopów.

a = 4
b = 8
wynik = 0

while b > 0:
    if b % 2 == 1:
        wynik += a 
    a *= 2
    b /= 2

print(wynik)

