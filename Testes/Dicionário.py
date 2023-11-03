import os
os.system("cls")

dici = {}

n = int(input("Digite até quantos números você deseja ver a raiz quadrada: "))

for i in range(n):
    dici[i] = i*i
print(dici)