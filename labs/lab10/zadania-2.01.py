# SŁOWNIKI
# ZADANIE 1

'''grocery={}
grocery={"mleko":1, 
         "chleb":2}
print(grocery)

grocery["woda"]=5
print(grocery)

for val in grocery.values():
    print(val)

for key in grocery.keys():
    print(key)

    
programmingLangauges = {1:"Python",
                        2:"CSharp",
                        3:"PHP"}
#if value exists, it returns the value
print(programmingLangauges.get(1))
#if value doesn't exist, it returns None
print(programmingLangauges.get(4))
print(programmingLangauges.values())
print(programmingLangauges.pop(3))
print(programmingLangauges)
if 2 in programmingLangauges:
    del programmingLangauges[2]
print(programmingLangauges)


letters = ['a','b','c','d']
numbers = [1,2,3,4]
myDict = dict(zip(letters,numbers))
print(myDict)

programmingLangauges = {1:"Python",
                        5:"Java",
                        3:"PHP"}

for key in sorted(programmingLangauges):
    print(key,programmingLangauges[key])'''


# ZADANIE 2
# print("ZADANIE 2")


def is_permutation(l1, l2):

    if len(l1) != len(l2):
        return False

    # słowniki zliczające wystąpienia w obu listach
    dict_count_l1 = {}
    dict_count_l2 = {}

    for elem in l1:
        dict_count_l1[elem] = dict_count_l1.get(elem, 0) + 1

    for elem in l2:
        dict_count_l2[elem] = dict_count_l2.get(elem, 0) + 1

    if dict_count_l1 == dict_count_l2:
        return True
    else:
        return False


l1 = [1, 2, 4, 7, 9]
l2 = [4, 2, 7, 9, 9]

# print(is_permutation(l1, l2))
# print()


# ZADANIE 3
# print("ZADANIE 3")


songs_dict = {
    "Calling Out": 3,
    "Is U": 4,
    "Good Lies": 5,
    "Skulled": 3,
    "Calon": 5
}

# for title, score in songs_dict.items():
#     if score == 5:
#         print(title)


# ZADANIE 4
# print("ZADANIE 4")


def replace(d, v, e):
    for key, value in d.items():
        if value == v:
            d[key] = e


d = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

v = 2
e = 10

# print(d)
# replace(d, v, e)
# print(d)
# print()


# ZADANIE 5
# print("ZADANIE 5")


def invert(d):
    dInv = {}

    for key, value in d.items():
        value_found = False

        for unique_value, keys_list in dInv.items():
            if unique_value == value:
                keys_list.append(key)
                value_found = True
                break

        else:
            dInv[value] = [key]

    return dInv


d = {
    "a": 1,
    "b": 2,
    "c": 2,
    "d": 4,
    "e": 7,
    "f": 1
}

# print(d)
# print(invert(d))


'''def invert(d):
    dInv = {}
    dInv_values = []

    for key, value in d.items():
        if value not in dInv:
            dInv[value] = [key]
        else:
            dInv[value].append(key)
    
    return dInv'''


# ZADANIE 6
# print("ZADANIE 6")


def ceasar_cipher(message, shift):
    alphabet = ["A", "Ą", "B", "C", "Ć", "D", "E", "Ę", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "Ó", "P", "Q", "R", "S", "Ś", "T", "U", "V", "W", "X", "Y", "Z", "Ź", "Ż"]
    cipher_dict = {}

    # tworzenie słownika
    for i in range(len(alphabet)):
        char = alphabet[i]
        new_char = (i + shift) % 32
        cipher_dict[char] = alphabet[new_char]

    # szyfrowanie wiadomości
    encrypted_message = ""
    for char in message:
        encrypted_char = cipher_dict.get(char, char)
        encrypted_message += encrypted_char

    return encrypted_message


message_to_encode = "MĘŻNY BĄDŹ, CHROŃ PUŁK TWÓJ I SZEŚĆ FLAG"
shift = 3
encoded_message = ceasar_cipher(message_to_encode, shift)

# print("oryginalna wiadomość:", message_to_encode)
# print("zakodowana wiadomość:", encoded_message)


# ZADANIE 7
# print("ZADANIE 7")


def ceasar_decipher(encrypted_message, shift):
    alphabet = ["A", "Ą", "B", "C", "Ć", "D", "E", "Ę", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "Ó", "P", "Q", "R", "S", "Ś", "T", "U", "V", "W", "X", "Y", "Z", "Ź", "Ż"]
    decipher_dict = {}

    # tworzenie słownika
    for i in range(len(alphabet)):
        char = alphabet[i]
        new_char = (i - shift) % 32
        decipher_dict[char] = alphabet[new_char]

    # odszyfrowanie wiadomości
    deciphered_message = ""
    for char in encrypted_message:
        decrypted_char = decipher_dict.get(char, char)
        deciphered_message += decrypted_char

    return deciphered_message


encrypted_message = "ÓHCPA DĆFB, EKTQŃ SXŁN WZRM L UĄGVĘ IOCJ"
shift = 3
deciphered_message = ceasar_decipher(encrypted_message, shift)

# print("zakodowana wiadomość:", encrypted_message)
# print("rozszyfrowana wiadomość:", deciphered_message)


# ZADANIE 8
# print("ZADANIE 8")

def roman_to_decimal(roman_numeral):

    roman_dictionary = {"I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000}
    decimal_number = 0

    for i in range(len(roman_numeral)):
        current_val = roman_dictionary[roman_numeral[i]]

        if i < len(roman_numeral) - 1 and roman_dictionary[roman_numeral[i + 1]] > current_val:
            decimal_number -= current_val
        else:
            decimal_number += current_val

    return decimal_number


roman_numeral = "MDCD"
# print(roman_to_decimal(roman_numeral))
# print()


# ZADANIE 9
# print("ZADANIE 9")


cars = [
    {
        "marka": "BMW",
        "model": "M2 F87",
        "rok_produkcji": 2021
    },

    {
        "marka": "BMW",
        "model": "M3 G80",
        "rok_produkcji": 2023
    },

    {
        "marka": "BMW",
        "model": "M4 G82",
        "rok_produkcji": 2023
    }
]

person = [
    {
        "imię": "Jan",
        "naziwsko": "Kowalski",
        "rok_ur": 1967,
        "samochody": [cars[0], cars[2]]
    },

    {
        "imię": "Dawid",
        "nazwisko": "Nowak",
        "rok_ur": 1992,
        "samochody": [cars[1]]
    }
]

# print(person[0]["samochody"])
# print()


# ZADANIE 10
# print("ZADANIE 10")


Polska = {
    "stolica": "Warszawa",
    "liczba_mieszkancow": 38000000,
    "jezyk_urzedowy": "polski"
}

Niemcy = {
    "stolica": "Berlin",
    "liczba_mieszkancow": 83000000,
    "jezyk_urzedowy": "niemiecki"
}

Francja = {
    "stolica": "Paryż",
    "liczba_mieszkancow": 67000000,
    "jezyk_urzedowy": "francuski"
}


# ZADANIE 11
# print("ZADANIE 11")


miasto1 = {
    "nazwa": "Warszawa",
    "liczba_mieszkancow": 1765,  # w tysiącach
    "powierzchnia_km2": 517
}

miasto2 = {
    "nazwa": "Sopot",
    "liczba_mieszkańców": 37,
    "powierzchnia_km2": 17
}

panstwo = {
    "nazwa": "Polska",
    "ludność": 38000,
    "stolica": miasto1,
    "miasta": [miasto1, miasto2]
}


# ZADANIE 12
# print("ZADANIE 12")


uczen1 = {
    "imię": "Jan",
    "nazwisko": "Kowalski",
    "przedmiot": "matematyka",
    "ocena": 4
}

uczen2 = {
    "imię": "Dawid",
    "naziwsko": "Nowak",
    "przedmiot": "fizyka",
    "ocena": 3
}

oceny = [1, 2, 3, 4, 5, 6]
przedmioty = ["język angielski", "fizyka", "matematyka", "biologia"]

uczen3 = {
    "imię": "Andrzej",
    "nazwisko": "Jakiś",

    "wyniki": {
        "przedmiot1": przedmioty[0],
        "ocena": oceny[4],

        "przedmiot2": {
            "nazwa": przedmioty[3],
            "ocena": oceny[2]
        }
    }
}

# print(f"Przedmiot 2: {uczen3['wyniki']['przedmiot2']['nazwa']}, Ocena: {uczen3['wyniki']['przedmiot2']['ocena']}")
# print()


# ZADANIE 14 ROZDZIAŁ 11 PODRĘCZNIK
# print("ZADANIE 14 ROZDZIAŁ 11 PODRĘCZNIK ")


d = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]

# a)

for dict in d:
    for key, value in dict.items():
        if key == "phone" and value.endswith("8"):
            print(f"{dict['name']}")
print()

# b)

for dict in d:
    for key, value in dict.items():
        if key == "email" and value == '':
            print(f"{dict['name']}")
print()

