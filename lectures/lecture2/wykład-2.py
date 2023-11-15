# WSTĘP DO PROGRAMOWANIA WYKŁAD 2

# funkcje wbudowane, globalne np. print(), len()
# string, integer, float, double, boolean, variable

number_of_users = 50    # instrukcja przypisania 
number = 3.5
message = "Hello\nWorld!"
isFriday = True 

result = number_of_users * number
                        # bad smell of code
# result2 = number_of_users * isFriday --> trzeba uważać na typ zmiennej 
# result3 = 3 * "aaa" --> konkatenacja łancucha znaków ze zmienną liczbową

print(message)
print(number)
print(isFriday)
print(result)

# instrukcja warunkowa 

print("--------START--------")

ocena = 4
if ocena >= 4:         # >, <, >=, <=, ==, !=
    print("dobry")
    print("mam 4 lub więcej")
    if ocena >= 5:            #lub elif [warunek]:
        print("bardzo dobry")
        print("mam 5!")
elif ocena < 3:
    print("niezaliczone")
else:
    print("przeciętny lub zły")
    print("mam 3 lub mniej")

print("---------END---------")

message2 = "Hello " + "World!"
print(len(message2))
print(message2[1])

