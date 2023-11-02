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
