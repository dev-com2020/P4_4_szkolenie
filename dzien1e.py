lista = [4, 5, 6]

for i in range(len(lista)):
    lista[i] += 10

print(lista)

nowa_lista = [i + 10 for i in lista]

print(nowa_lista)

zakupy = ['piwo', 'czekolada', 'piwo', 2023, 'piwo', 13.30]

zakupy_do_usuniecia = 'piwo'

# while zakupy_do_usuniecia in zakupy:
#     zakupy.remove(zakupy_do_usuniecia)

zakupy = [i for i in zakupy if i != zakupy_do_usuniecia]

print(zakupy)

for index, wartosc in enumerate(lista):
    print(f"index: {index} wartosc: {wartosc}")
    # print("index: %i wartosc: %i " % (index, wartosc))

wersja = 3.10
jezyk = "C++"
print("Używam %s w wersji %i" % (jezyk, wersja))
print("Używam pythona w wersji %f" % wersja)
print("Używam pythona w wersji %.2f" % wersja)
print("Używam {0} w wersji {1}".format(jezyk, wersja))

spec_string = """
    to jest tekst...🤩
        to jest tekst...🤩
            to jest tekst...🤩"""

print(spec_string)

krotka = ("Ania", "Gosia", "Jacek", "Adam")
imie1, *imie2, imie3 = krotka
print(imie1)
print(imie2)
print(imie3)

liczby = range(2, 6, 2)
lista = list(liczby)
print(liczby)

for i in liczby:
    print(i)

print(lista)

liczba = int(input("Podaj liczbę: "))

if liczba < 10:
    print("Liczba jest mniejsza od 10")
elif liczba == 10:
    print("Liczba to 10!")
    pytanie = input("Czy lubisz koty? (t/n)")
    if pytanie == 't':
        print("🐈")
    else:
        print("🐀")
else:
    print("Liczba jest większa od 10")

