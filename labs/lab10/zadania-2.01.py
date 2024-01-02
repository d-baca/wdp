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
print("ZADANIE 7")










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






