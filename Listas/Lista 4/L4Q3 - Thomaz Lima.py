import os
os.system("cls")
m, v, soma, soma1, soma2 = [[], [], []], [], 0, 0, 0

for l in range (3):
    for c in range (3):
        m[l].append(float(input(f"Digite o valor da posição [{l}][{c}]: ")))
        if c == 0:
            soma += m[l][c]
        elif c == 1:
            soma1 += m[l][c]
        else:
            soma2 += m[l][c]
v.append(soma)
v.append(soma1)
v.append(soma2)
for l in range (3):
    for c in range (3):
        print(f"[{m[l][c]:^6}]", end = "")
    print()
print(v)