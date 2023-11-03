import os
os.system("cls")
v = [1,2,3,4,5,6,7,8]
tabuleiro = [[],[],[],[],[],[],[],[]]

lin = int(input("Digite a linha em que a torre se encontra: "))
col = int(input("Digite a coluna em que a torre se encontra: "))

for l in range (8):
    for c in range (8):
        if c == col-1:
            tabuleiro[l].append('x')
        elif l == lin-1:
            tabuleiro[l].append('x')
        else:
            tabuleiro[l].append('-')
print(f" {1:^3}{2:^3}{3:^3}{4:^3}{5:^3}{6:^3}{7:^3}{8:^3}")
for l in range (8):
    print(f"{v[l]}",end = "")
    for c in range (8):
        print(f"{tabuleiro[l][c]:^3}", end = "")
    print()