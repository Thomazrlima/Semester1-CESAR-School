import os
os.system('cls')
while True:
    try:
        dici,soma,n = {},0,1
        quant = int(input("Digite o número de pessoas que desejam fazer a doação: "))
        for i in range (quant):
            nome = input(f"Digite o nome da {i+1}° pessoa a fazer a doação: ")
            dici[nome] = int(input("Digite o valor da doação: "))
        for chave, valor in dici.items():
            soma += valor
            print(f"{n}° {chave} - {valor} R$")
            n+=1
        print(f"O total arrecadado foi: {soma} R$")
        break
    except ValueError:
        print("Digite um valor válido")