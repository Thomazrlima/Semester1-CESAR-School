import os
os.system("cls")

peso,soma = [], 0
print("Bem-vindo ao sistema de cálculo de peso de uma empresa do malvado Doofenshmirtz")
venda = int(input("Quantos produtos você vendeu no dia? "))
for i in range (0, venda):
    peso.append(float(input(f"Digite o valor da sua {i+1}° venda: ")))
    soma += peso[i]

    if i == 0:
        menor = peso[i]
        maior = peso[i]
    if peso[i] < menor:
        menor = peso[i]
    if peso[i] > maior:
        maior = peso[i]
print("A média dos pesos foi {:.2f} KG".format(soma/venda))
print("O maior foi",maior,"KG e o menor",menor,"KG")
print("O total arrecadado foi {:.2f} R$".format(soma*4.35))