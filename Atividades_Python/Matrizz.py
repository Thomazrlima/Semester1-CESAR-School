m, soma, soma1 = [[],[],[]], 0, 0

for l in range(3):
    for c in range(3):
        m[l].append(int(input(f"Digite o número da posição [{l},{c}]: ")))
for i in range(3):
    for j in range(3):
        if m[i][j]%2 != 0:
            soma += m[i][j]
        if j == 0:
            soma1 += m[i][j]
        if i == 2:
            menor = m[2][0]
            if menor > m[i][j]:
                menor = m[i][j]
for i in range (3):
    for c in range(3):
        print(f"[{m[l][c]:^4}]", end = "")
    print()
print("Menor da linha 3 =",menor," | Soma dos primos =",soma," | Soma da primeira linha =",soma1)