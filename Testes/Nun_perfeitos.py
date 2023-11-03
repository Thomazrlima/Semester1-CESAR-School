n = int(input("Digite o número que você deseja: "))
soma = 0

for i in range (1, n):
    if n%i == 0:
        soma += i
if soma == n:
        print("Seu número é PERFEITO!")
else:
        print("Seu número é imperfeito")
