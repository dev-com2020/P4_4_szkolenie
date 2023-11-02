import os

# f = open("dane.txt", 'w')
# f.write("Pierwsza linia plus znak nowej linii\n")
# f.write("dane1  dane2   dane3\n")
# f.close()
#
# f = open("dane.txt", 'a')
# f.write("dane7  dane8   dane9\n")
# f.close()

f = open("dane.txt", 'r')
linia1 = f.readline()
linia2 = f.readline()
linia3 = f.readline()
f.close()
print(linia1, linia2, linia3)

print(os.getcwd())
# os.mkdir('wyniki')
os.rmdir('wyniki')
dir_path = 'D:/'
print(os.listdir(dir_path))


