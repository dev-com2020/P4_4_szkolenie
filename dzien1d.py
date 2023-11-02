x = 4
if x < 5:
    y = -1
    z = 5
elif x > 5:
    y = 1
    z = 11
else:
    y = 0
    z = 10

print(x)
print(y)
print(z)

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    if licznik > 10:
        break

print(licznik)

counter = 0
while counter < 5:
    print("Licznik wynosi:", counter)
    counter += 1

lista = []
print("Podaj liczbę, którą chcesz umieścić w liście")
print("Wpisz 'stop' aby zakończyć program")
while True:
    wejscie = input()
    if wejscie == 'stop':
        break
    lista.append(int(wejscie))

print("Twoja lista ->", lista)

