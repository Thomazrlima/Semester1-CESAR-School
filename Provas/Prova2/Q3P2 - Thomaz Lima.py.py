import os
os.system('cls')
tabuleiro = []
def calc(tabuleiro):
    for i in range (len(tabuleiro)):
        soma = 0
        if i == 0:
            soma += (tabuleiro[i] + tabuleiro[i+1])
        elif i == (len(tabuleiro) - 1):
            soma += (tabuleiro[i] + tabuleiro[i-1])
        else:
            soma += (tabuleiro[i] + tabuleiro[i+1] + tabuleiro[i-1])
        print(soma)
while True:
    try:
        tam = int(input("Digite o tamanho do tabuleiro: "))
        for i in range(tam):
            tabuleiro.append(int(input(f"Digite a disposição do tabuleiro {i+1}° casa: ")))
        calc(tabuleiro)
        break
    except ValueError or tam < 1 or tam > 50:
        print("Digite um valor válido")