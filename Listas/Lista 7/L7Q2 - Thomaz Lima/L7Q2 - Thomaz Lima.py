import os
os.system('cls')
soma = 0

with open('L7.txt', 'r') as arq:
    arquivo = arq.read().split()
for i in range (len(arquivo)):
    v = True
    arquivo[i] = arquivo[i].replace(".", " ")
    arquivo[i] = arquivo[i].strip().split(' ')
    for j in arquivo[i]:
        if int(j) > 255:
            v = False
    if not v:
        print(f"{arquivo[i]} Esse IP é inválido")
    else:
        print(f"{arquivo[i]} Esse IP é válido")