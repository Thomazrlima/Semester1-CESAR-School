import os
os.system("cls")
m, prod, soma, menor, = [[],[],[]], 1, 0, []

for l in range (3):
    for c in range (3):
        m[l].append(float(input(f"Digite o valor a ser inserido na posição [{l}][{c}]: ")))
        soma += m[l][c]

med = soma/9
maior_c2 = m[0][2]

for l in range (3):
    for c in range (3):
        if c == l:
            prod *= m[l][c]
        if c == 1:
            if maior_c2 < m[l][c]:
                maior_c2 = m[l][c]
        if m[l][c] <= med:
            menor.append(m[l][c])
        print(f"[{m[l][c]:^7}]", end = "")
    print()
print("o produto dos elementos da diagonal principal é:", prod)
print("A média de todos os elementos da matriz é: ", med)
print("O maior valor lido da segunda coluna é:", maior_c2)
print("Os valores menores ou iguais a média são:", menor)