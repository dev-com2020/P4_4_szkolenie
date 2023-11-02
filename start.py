from pakiet import kalk as k

print(k.dodaj(4, 5))
print(k.odejmij(4, 5))
print(k.pomnoz(4, 5))
print(k.dodaj2(5, 5))
print(k.dziel(50, 2))


def suma(*x):
    if len(x) == 0:
        return "nie mam czego sumować"
    else:
        return sum(x)


print(suma())
print(suma(5, 5))
print(suma(5, 5, 10, 50))
