m, lista, soma, soma1, maior = [[],[],[]], [], 1, 0, 0

for l in range(3):
    for c in range(3):
        m[l].append(int(input(f"Digite o número da posição [{l},{c}]: ")))
        soma1 += m[l][c]
        if l == c:
            soma *= m[l][c]
        if c == 1:
            if maior < m[l][c]:
                maior = m[l][c]
for l in range (3):
    for c in range(3):
        if m[l][c] > soma1/9:
            lista.append(m[l][c])
print("O produto dos Elementos da diagonal pruncipal é igual a",soma)
print(f"A média de todos os Elementos da Matriz é igual a {soma1/9:.2f}")
print("O maior valor da segunda coluna é:",maior)
print("Os valores maiores que a média são:",lista)