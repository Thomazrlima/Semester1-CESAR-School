import os
os.system('cls')
soma = 0

with open('sus.txt', 'r') as arq:
    arquivo = arq.read().split()
for i in range (len(arquivo)):
    arquivo[i] = str(arquivo[i])
    if arquivo[i] != 0:
        if arquivo[i] > arquivo[i-1]:
            soma += 1
print(soma)