cont = 0
soma = 0
while True:
    idade = int(input("Digite a idade do aluno: "))

    if idade == 999:
        break

    cont += 1
    soma += idade

print("A média de idade do grupo de", cont, " alunos foi", soma/cont)