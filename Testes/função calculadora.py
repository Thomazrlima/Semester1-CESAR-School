import os
os.system('cls')
def calc(n1,n2,escolha):
    if escolha == 'divisão':
        if n1 > n2:
            r = n1/n2
        else:
            r = n2/n1
    elif escolha == 'multiplicação':
        r = n1*n2
    elif escolha == 'subtração':
        r = n1-n2
    else:
        r = n1+n2
    return r
n1, n2= float(input("Digite o 1° número da sua operação: ")), float(input("Digite o 2° número da sua operação: "))
escolha = input("Digite a opecarção que você deseja fazer: ")
if escolha == 'divisão' or escolha == 'multiplicação' or escolha == 'subtração' or escolha == 'soma':
    print(calc(n1,n2,escolha))
else:
    print("Operação inválida")