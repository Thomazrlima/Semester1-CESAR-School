import os
os.system("cls")
print(" Necessita da esfera = 1 //  Necessita de limpeza = 2")
print(" Necessita troca do cabo ou conector = 3 //  Quebrado ou inutilizado = 4")
ident, defeito, cont1, cont2, cont3, cont4 = [], [], 0, 0, 0, 0

total = int(input("Quantos Mouses foram encontrados? "))
for i in range (total):
    ident.append(int(input("Digite o número de indentificação do Mouse: ")))
    defeito.append(int(input("Digite o tipo do defeito: " )))
    if defeito[i] == 1:
        cont1+=1
    elif defeito[i] == 2:
        cont2+=1
    elif defeito[i] == 3:
        cont3+=1
    else:
        cont4+=1
print("Quantidade de mouses =",len(defeito))
print("Situação\t\t\tQuantidade\t\tPercentual")
print(f"1-Necessita da esfera    \t{cont1:^7}\t\t\t{cont1/len(defeito)*100:^7}")
print(f"2-Necessita de limpeza   \t{cont2:^7}\t\t\t{cont2/len(defeito)*100:^7}")
print(f"3-Novo cabo ou conector  \t{cont3:^7}\t\t\t{cont3/len(defeito)*100:^7}")
print(f"4-Quebrado ou inutilizado\t{cont4:^7}\t\t\t{cont4/len(defeito)*100:^7}")