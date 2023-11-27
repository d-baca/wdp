# WSTĘP DO PROGRAMOWANIA WYKŁAD 6

# słowniki

silnik = {
    "pojemność_silnika": 3000,
    "producent": "BMW",
    "spalanie": 12
}

bmwM3 = {
    "marka": "BMW",
    "model": "M3 G80",
    "rok_produkcji": 2023,
    "czy_ciężarowy": False,
    "silnik": silnik
}

bmwM4 = {
    "marka": "BMW",
    "model": "M4 G82",
    "rok_produkcji": 2023,
    "czy_ciężarowy": False,
    "silnik": silnik
}

panJan = {
    "imię": "Jan",
    "nazwisko": "Przysłowiowy-Kowalski",
    "rok_ur": 1967,
    "samochód": [bmwM3, bmwM4]
}


# wywoływanie

print(panJan["nazwisko"])
print(panJan["rok_ur"])
print()

panJan["rok_ur"] = 1978
print(panJan)
print()

if not bmwM3["czy_ciężarowy"]:
    print("osobowy")
print()


# panśtwa, miasta, stolice

# miasta

miasto1 = {
    "nazwa": "Gdańsk",
    "liczba_mieszkańców": 486  # w tysiącach
}

miasto2 = {
    "nazwa": "Gdynia",
    "liczba_mieszkańców": 244
}

miasto3 = {
    "nazwa": "Sopot",
    "liczba_mieszkańców": 37
}

miasto4 = {
    "nazwa": "Warszawa",
    "liczba_mieszkańców": 1765
}

# państwa

państwo1 = {
    "nazwa": "Polska",
    "ludność": 38000,
    "stolica": miasto4,
    "miasta": [miasto1, miasto2, miasto3, miasto4]
}

# definiowanie funkcji tworzenia miast


def stwórz_miasto(nazwa, ludność):
    return {
        "nazwa": nazwa,
        "liczba_mieszkańców": ludność,
    }


państwo2 = {
    "nazwa": "Niemcy",
    "ludność": 80000,
    "stolica": stwórz_miasto("Berlin", 3600),
    "miasta": [stwórz_miasto("Bon", 327), stwórz_miasto("Hamburg", 1841), stwórz_miasto("Kolonia", 1000)]
}

db = [państwo1, państwo2]


def dodaj_państwo(baza, nazwa, ludność, stolica, miasta):
    baza.append({
        "nazwa": nazwa,
        "ludność": ludność,
        "stolica": stolica,
        "miasta": miasta
    })

###################
# wiek = 34       #
# def policz():   #
#     global wiek #
#     # ...       #
#     wiek = 67   #  zmienne globalne, odczyt
#     # ...       #
#     return 24   #
# policz()        #
# print(wiek)     #
###################


dodaj_państwo(db, "Czechy", 10500, stwórz_miasto("Praga", 1357),
              [stwórz_miasto("Budiejowice", 94.5), stwórz_miasto("Brno", 380)])
print(db)
print()


# znajdź (tj. napisz funkcję, która wyznaczy) państwo z najludniejszą stolicą.

# znajdź (tj. napisz funkcję, która wyznaczy) największe miasto w bazie.

# znajdź państwo z największą liczbą ludności w miastach.


def suma_mieszkańców_miast(db):
    suma = 0
    for kraj in db:
        for miasto in kraj["miasta"]:
            suma += miasto["liczba_mieszkańców"]
    return suma


print(suma_mieszkańców_miast(db))
print()

