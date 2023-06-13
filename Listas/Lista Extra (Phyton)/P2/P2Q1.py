import os
os.system("cls")
a,b,c = [],[],[]

dados = int(input("Entrada de dados: "))
for i in range (dados):
    a.append(float(input(f"Digite o valor do {i+1}° Elemento de A: ")))
    b.append(float(input(f"Digite o valor do {i+1}° Elemento de B: ")))
    c.append(a[i]+b[i])
print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")