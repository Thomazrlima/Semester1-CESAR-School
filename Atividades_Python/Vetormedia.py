vetor = []
for i in range (1,6):
    vetor.append(float(input("Digite a nota do primeiro aluno: ")))

media = sum(vetor)/len(vetor)
print("A média da turma foi:", media)

for valor in vetor:
    if valor > media:
        print('{0}° = {1}'.format(vetor.index(valor)+1, valor))