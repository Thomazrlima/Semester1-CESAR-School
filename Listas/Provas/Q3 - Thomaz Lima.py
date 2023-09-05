import os
os.system("cls")

vetor, maior = [], 0

for i in range (5):
    vetor.append(int(input(f"Digite o {i+1} número da lista: ")))

for i in range (5):
    if vetor[0] < vetor[1]:
        maior = vetor [0]
        vetor[1] = vetor[0]
        maior = vetor[1]
    elif vetor[1] < vetor[2]:
        maior = vetor [1]
        vetor[2] = vetor [1]
        maior = vetor[2]
    elif vetor[2] < vetor[3]:
        maior = vetor [2]
        vetor[3] = vetor [2]
        maior = vetor[3]
    elif vetor[3] < vetor[4]:
        maior = vetor [3]
        vetor[4] = vetor [3]
        maior = vetor[4]
    elif vetor[4] > vetor[0]:
        maior = vetor [0]
        vetor[4] = vetor [0]
        maior = vetor[4]
print(vetor)