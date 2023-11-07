# ZADANIE 1: Sprawdź, co robi następujący program.

#a)
for i in range(15):
    print(i)
print()

#b) 
for i in range(2,15):
    print(i)
print()

#c)
for i in range(2,15,4):
    print(i)
print()

#d)
n = 4
print("rozmiar:", n)
for j in range(1, n+1):
    print((n-j)*"-", end="")
    print(j*"+")
print()


# ZADANIE 2

n = 5
print("rozmiar:", n)

for j in range(1, n+1):
    print((n-(j-1))*"*")
print()


# ZADANIE 3 

n = 5
print("rozmiar:", n)

for j in range(1, n+1):
    print((n-j)*" ", end="")
    print(j*"*")
print()


# ZADANIE 4

n = 5
print("rozmiar:", n)

for j in range(1, n+1):
    print(j*"*")
print()


# ZADANIE 5

n = 5
print("rozmiar:", n)

for j in range(1, n+1):
    print(j*" ", (n-(j-1))*"*")
print()


# ZADANIE 6

n = 5
print("rozmiar:", n)

for j in range(1, n+1):
    print(j*" *")
print()


# ZADANIE 7

n = 6
print("rozmiar:", n)

for j in range(1, n+1):
    print((n-j)*" ", end="")
    print(j*" *")
print("    |___|")
print()


# ZADANIE 8

silnia = 1
for i in range(1, 5):
    silnia *= (i + 1)

print("silnia podanej liczby wynosi:", silnia)
print()


# ZADANIE 9

suma = 0
for i in range(1, 11):
    suma += i

print("suma liczb od 1 do 10 wynosi:", suma)
print()


# ZADANIE: 10 1+0, 2+1, 3+2, 4+3, 5+4, 6+5, 7+6, 8+7, 9+8, 10+9

suma = 0

for i in range(1, 11):
    suma = 2*i - 1
    print("suma liczby aktualnej i poprzedniej wynosi:", suma)
print()


# ZADANIE 11 1, 1+2, 1+2+3, 1+2+3+4, ...

suma = 0

for i in range(1, 11):
    suma += i
    print(suma, end=", ")
print()


# ZADANIE 12
# 1, -1, 2, -2, 4, -4, 8, -8, 16, -16

liczby1 = 0
liczby2 = 0

for i in range(0, 5):
    liczby1 = 2**i
    liczby2 = -(2**i)
    print(liczby1, liczby2, end=", ")
print()

# ZADANIE 13 liczby pierwsze 2, 3, 5, 7, 11, 13, ... (1-800)

# _______________________________________
# |                                     |
# | liczba_dzielnikow = 0               |
# | n = 800                             |
# |                                     |
# | for i in range(1, n+1):             |
# |     if n+1 % i == 0 and i % 1 == 0: |
# |        liczba_dzielnikow += 1       | ---> Schemat sprawdzający, czy liczba jest pierwsza
# |                                     |
# | if liczba_dzielnikow == 2:          |
# |     print("liczba pierwsza")        |
# | else:                               |
# |     print("liczba złożona")         |
# |_____________________________________|

n = 800

for n in range(2, n + 1):
    liczba_pierwsza = True
    for i in range(2, n):
        if n % i == 0:
            liczba_pierwsza = False
            break
    if liczba_pierwsza:
        print(n, end=", ")
print()

# ZADANIE 14

a = 123
b = 84

# __________________________________
# |                                |
# | def NWD(a, b):                 |
# |     while a != b:              |
# |         if a > b:              |
# |             a -= b             |
# |         else:                  | ---> Schemat Euklidesa przy użyciu opcji definiowania funkcji
# |             b -= a             |
# |                                |
# |     return a                   |
# |                                |
# | print("NWD wynosi:", NWD(a,b)) |
# |________________________________|

for i in range(b, 0, -1):
    if a % i == 0 and b % i == 0:
        nwd = i
        break

print("NWD wynosi:", nwd)
print()

# ZADANIE 15

m = 10
n = 10

print("tabliczka mnożenia m*n")
for i in range(1, m + 1):
    for j in range(1, n + 1):
        wynik = i * j
        print(wynik, end=" | ")
print()


# ZADANIE 16

n = 49

znalezione = False

for a in range(1, int(n**0.5) + 1):
    for b in range(a, int(n**0.5) + 1):
        if a**2 + b**2 == n:
            znalezione = True
            break
    if znalezione:
        break

if znalezione:
    print(n,"=",a,"^2 +",b,"^2")
else:
    print("Liczby", n, "nie można rozłożyć na sumę dwóch kwadratów liczb naturalnych.")
print()


# ZADANIE 17

n = 1000

for i in range(100, n):
    if (i // 100) < ((i // 10) % 10) and ((i // 10) % 10) < (i % 10):
        print(i, end=", ")
print()

