import os
os.system("cls")

resultados = [[],[],[],[],[],[]]
vetor = []
camisa = [1,2,3,4,5,6]
soma1, soma2, soma3, soma4, soma5, soma6, maior = 0,0,0,0,0,0,0

while True:

    n = int(input("Digite o número do melhor jogador na sua opinião: "))
    
    if n >= 1 and n <=6:
        vetor.append(n)
    elif n == 0:
        break
    else:
        print("Esse jogador não esteve em campo, por favor dogite um número válido")

print(f"O total de votos computados foi {len(vetor)}")

for i in range (len(vetor)):
    if vetor[i] == 1:
        soma1 += 1
    elif vetor[i] == 2:
        soma2 += 1
    elif vetor[i] == 3:
        soma3 += 1
    elif vetor[i] == 4:
        soma4 += 1
    elif vetor[i] == 5:
        soma5 += 1
    else:
        soma6 += 1

for l in range (6):
    for c in range(3):
        if c == 0:
            resultados[l].append(camisa[l])
        if c == 1:
            if l == 1:
                resultados[l].append(soma1)
            elif l == 2:
                resultados[l].append(soma2)
            elif l == 3:
                resultados[l].append(soma3)
            elif l == 4:
                resultados[l].append(soma4)
            elif l == 5:
                resultados[l].append(soma5)
            else:
                resultados[l].append(soma6)
        if c == 2:
            if l == 1:
                resultados[l].append((soma1/len(vetor)*100))
            elif l == 2:
                resultados[l].append((soma2/len(vetor)*100))
            elif l == 3:
                resultados[l].append((soma3/len(vetor)*100))
            elif l == 4:
                resultados[l].append((soma4/len(vetor)*100))
            elif l == 5:
                resultados[l].append((soma5/len(vetor)*100))
            else:
                resultados[l].append((soma6/len(vetor)*100))
print("  N° / Votos / Porcentagem dos Votos")
for l in range (6):
    for c in range(3):
        print(f"{resultados[l][c]:^7}", end = "")
        if c == 1:
            if maior  < resultados[l][c]:
                maior = resultados[l][c]
                melhor = l
    print("%")
print(f"Total de votos {len(vetor)}")
print(f"O Melhor jogador da partida foi {melhor} com {maior} votos, o que representou {(maior/len(vetor))*100}%")