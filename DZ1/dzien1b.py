zakupy = ['piwo', 'czekolada', 2023, 13.30]

print(type(zakupy))
print(zakupy)
print(zakupy[0])
print(zakupy[:2])
print(zakupy[-2:])

zakupy.append(159753)
zakupy.insert(0, 'książka')
zakupy.pop()
zakupy.remove('piwo')
print(zakupy)

oceny = [6, 3, 4, 5, 2, 3, 1]
oceny.sort()
oceny.reverse()
print(oceny)

krotka = (5, 4, 3, 6, 1, 2)
print(krotka[0])
print(krotka[0:2])
oceny = list(krotka)
oceny.reverse()
print(oceny)
krotka = tuple(oceny)
print(krotka)

liczba = "0"
liczba = (int("0"))
print(type(liczba))

imie = "Tomek"
print(imie)
print(imie[0])
print(imie[0:3])
print(imie.upper())
print(len(imie))

slownik = {1: "jeden",
           2: "dwa",
           "trzeci": '3',
           4: ['Tomek', 'Adam', "Ania"]}

print(slownik[1])
print(slownik['trzeci'])
print(slownik[4][1])
print(slownik.get(2))
print(slownik.get(5, "niedostępne"))
# tutaj dowolny tekst opisujący kod
# print(slownik[5])
print(slownik.items())

keys = ['a', 'b', 'c']
val = [1, 2, 3]
new_dict = dict.fromkeys(keys, val)
print(new_dict)

slownik.popitem()
slownik[5] = 456
slownik[1] = 3456
print(slownik)

zbior = {2, 4, 5, 7, 1, 7, 3}
zbior.add(2)
zbior.add(22)
print(zbior)
