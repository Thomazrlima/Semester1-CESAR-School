from random import randint
import os
os.system("cls")

tupla = []

for i in range (5):
    tupla.append(randint(0,100))
tupla = tuple(tupla)

print(f"Tupla = {tupla}")
print(f"O maior valor da tupla é {max(tupla)}")
print(f"O menor valor da tupla é {min(tupla)}")