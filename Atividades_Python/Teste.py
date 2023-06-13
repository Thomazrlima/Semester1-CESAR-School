import os
os.system("cls")
vetor, vetor1, vetor2 = [], [], []
for i in range (1, 4):
    vetor.append(input("Digite o nome do carro: "))
    vetor2.append(int(input("Digite o ano do carro: ")))
    vetor1.append(float(input("Digite o valor do carro: ")))
    os.system("cls")
print("   Modelo:\t    Ano:   Valor:")
for i in range (0, 3):
    print(f"{vetor[i]:^16}{vetor2[i]:^12}{vetor1[i]}")