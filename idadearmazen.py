import os
os.system('cls')

nomes,idades = [], []
def armazen ():
    while True:
        nome = input("Digite o nome que você deseja adicionar: ").capitalize()
        idade = int(input("Digite a idade dessa pessoa: "))
        if nome == 'Maria':
            continue
        if idade == -1:
            break
        nomes.append(nome)
        idades.append(idade)
armazen()
print(nomes)
print(idades)