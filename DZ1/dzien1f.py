def nic_ciekawego():
    print("Hej!")


def katalog(imie, wiek):
    return f"imie: {imie.upper()}, wiek: {wiek}"


def katalog2(wiek, imie=''):
    return imie, wiek


nic_ciekawego()
print(katalog("Tomek", 40))
print(katalog("Ania", 30))
print(katalog("Adam", 20))

lista = []
lista.append(katalog("Adam", 20))
lista.append(katalog2(23))
lista.append(katalog2(23, imie="Krystian"))
print(lista)
