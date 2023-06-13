import os
os.system('cls')
print("Bem-vindo ao super caixinator virtual do supermercado da empresa do malvado Doofenshmirtz")
soma = 0
preco = 1
while preco != 0:
    preco = float(input("Digite o valor do seu produto "))
    if preco < 0:
        print("Digite um valor válido")
    if preco > 0:
        soma += preco
if soma >= 1000:
    soma = soma*0.9
    print("Desconto de 10% Aplicado")
print("Sua conta ficou em ",soma," R$, obrigado pela preferência")