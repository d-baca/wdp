#ZADANIE 4:

x = 1
y = 4
if x == y:
    print("TAK")
else:
    print("NIE")



#ZADANIE 5:

x = 10330
if x % 2 == 0:
    print("zmienna jest parzysta")
else: 
    print("zmienna jest nieparzysta")



#ZADANIE 6:

x = 7
y = 7

if x > y:
    print("większa jest liczba x")
elif x < y:
    print("większa jest liczba y")
else:
    print("obie liczby mają taką samą wartość")



#ZADANIE 7:

x = 111
y = 111
z = 111

if x >= y and x >= z:
    print(x)
elif y >= x and y >= z:
    print(y)
else:
    print(z)



#ZADANIE 8:

a = 1
b = 1
c = 1

if a > b and a > c and b > c:
    print(c, b, a)
elif a > b and a > c and c > b:
    print(b, c, a)
elif b > a and b > c and a > c:
    print(c, a, b)
elif b > a and b > c and c > a:
    print(a, c, b)
elif c > a and c > b and a > b:
    print(b, a, c)
elif c > a and c > b and b > a:
    print(a, b, c)
elif a == b and c > a and c > b:
    print("a = b < c lub b = a < c")
elif a == c and b > a and b > c:
    print("a = c < b lub c = a < b")
elif b == c and a > b and a > c:
    print("b = c < a lub c = b < a")
else:
    print("-")



#ZADANIE 9:

a = 14             #y = ax + b
b = 5

if a != 0 and b != 0:
    print("miejsce zerowe to x = " + str(-b / a))
elif a == 0 and b != 0:
    print("brak miejsca zerowego")
elif a == 0 and b == 0:
    print("istnieje nieskończenie wiele miejsc zerowych")
elif a != 0 and b == 0:
    print("miejsce zerowe to x = 0")



#ZADANIE 10: 

from math import *

a = 10               #y=ax^2+bx+c    delta=b**2 - 4*a*c      x1 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
b = 1                                                     #x2 = (b - sqrt(b**2 - 4*a*c)) / (2*a)
c = -1

delta = b**2 - 4*a*c

if a != 0 and delta > 0:
    print("funkcja ma dwa miejsca zerowe: x1 = " + str((-b - sqrt(delta)) / (2*a)) + ", x2 = " + str((b - sqrt(delta)) / (2*a)))
elif a != 0 and delta == 0:
    print("funkcja ma jedno miejsce zerowe: x1=x2 = " + str((-b / 2*a)))
elif a != 0 and delta < 0:
    print("funkcja nie ma miejsc zerowych")
elif a == 0:
    print("to nie jest funkcja kwadratowa")
else:
    print("funkcja ma nieskończenie wiele rozwiązań")



#ZADANIE 11 :

liczba = int(input("Wprowadź liczbę całkowitą od 100 do 999: "))
jednosci = int(liczba % 10) 
dziesiatki = int(liczba / 10 % 10)
setki = int(liczba / 100 % 10)

if liczba >= 100 and liczba <= 999:
    print(jednosci, dziesiatki, setki)
else:
    print("Wprowadzona liczba nie mieści się w podanym zakresie")

