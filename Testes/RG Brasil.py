m , soma = [[],[],[],[],[]], 0
rg = ["NO","NE","CO","SU","SE"]
print("As linhas representam as Regiões, e as colunas os trimestres")
for l in range(5):
    for c in range(4):
        m[l].append(int(input(f"Digite o número da posição [{l},{c}] da região {rg[l]}: ")))
        soma += m[l][c]
print("  \t1°\t2°\t3°\t4°")
for l in range (5):
    print(f'{rg[l]}  ', end='')
    for c in range(4):
        print(f"[{m[l][c]:^5}]".ljust(9), end = "")
    print()
print("O total de vendas foi:",soma)