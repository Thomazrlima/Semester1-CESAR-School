import os
os.system("cls")
erro, dire, esqu = 0,0,0

while True:
    curva = input("Digite para qual lado é a curva: ")
    if curva == 'sair':
        break
    else:
        if curva == 'esq' or curva == 'e' or curva == 'esquerda':
            esqu += 1
        elif curva == 'dir' or curva == 'd' or curva == 'direita':
            dire += 1
        else:
            erro += 1
print(f"O total de curvas para a direita foi {dire}, já para a esquerda {esqu}, e um total de {erro} erros")