print("Bem vindo ao cálculo de preço do cinema Politeama")
idade = int(input("Digite sua idade: "))

if idade <= 4 or idade >= 60:
    valor = 0
elif idade > 4 and idade < 18:
    valor = 20
else:
    valor = 30
print("O valor do seu ingresso em reais é", valor)