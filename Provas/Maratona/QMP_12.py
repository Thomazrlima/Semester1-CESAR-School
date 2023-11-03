print('Programa de Supermercado')
print('Digite o numero de Produtos: 8')
num = 8
num_primeiro = num
maior_valor,menor_valor = 0,0
while num > 0:
    print('Digite o valor do {0}° produto!'.format(num))
    valor = float(input())
    if num == num_primeiro:
        maior_valor = valor
        menor_valor = valor
    else:
        if valor > maior_valor:
            maior_valor = valor
        elif valor < menor_valor:
            menor_valor = valor

    num -= 1
print('O maior valor é: ', maior_valor)
print('O menor valor é: ', menor_valor)

