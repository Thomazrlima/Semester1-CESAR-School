anoatual = int(input("Digite o ano atual: "))
maior, menor = 0, 0
for i in range (0, 5):
    ano = int(input("Digite o ano em que você nasceu: "))
    if (anoatual - ano) < 18:
        menor += 1
    else:
        maior += 1
print(maior, "Pessoas são maiores de idade e ",menor," pessoas são menores de idade")