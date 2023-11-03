n = int(input("Digite o primeiro número do intervalo "))
n1 = int(input("Digite o segundo número do intervalo "))
cont = n
soma = 0

while n <= n1:
    if n%2 != 0:
        n += 1
    soma += n
    n += 1
print("A soma final foi ", soma)