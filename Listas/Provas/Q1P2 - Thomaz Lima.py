import os
os.system('cls')
dici,soma = {}, 0
while True:
    try:
        for c in range(5):
            nome = input("Digite seu nome: ").capitalize()
            dici[nome] = input("Digite o número de curtidas da suas fotos separado por espaço: ").strip().split(' ')
        for nome, valores in dici.items():
            for i in range (3):
                n = int(valores[i])
                soma += n
            print(f"O usuário {nome} teve em média {(soma/3):.2f} curtidas")
            soma = 0
        break
    except ValueError:
        print("Digite um valor válido")