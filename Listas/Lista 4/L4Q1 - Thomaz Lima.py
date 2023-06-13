import os
os.system("cls")
a, b, c, par, impar, cont = [], [], [], 0, 0, 0

print("Bem-vindo ao vetorinator de uma empresa do malvado Doofenshmirtz")

for i in range (0,5) :
    a.append(float(input(f"Digite o valor do {i+1}° número do vetor a: ")))
for i in range (0,5) :
    b.append(float(input(f"Digite o valor do {i+1}° número do vetor b: ")))
c = a+b
menor = c[0]

for i in range (0, 10):
    if c[i]%2 != 0:
        impar += c[i]
        cont += 1
    if c[i]%2 == 0:
        par += c[i]
    if menor > c[i]:
        menor = c[i]

print(c)
print("A soma dos números pares do vetor C é:",par)
print("A média dos números ímpares do vetor C é: {:.2f}".format(impar/cont))
print("O menor valor do vetor C é:",menor)