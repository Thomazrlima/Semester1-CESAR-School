import os
os.system("cls")
m, info, somasal, somatra = [[], [], []], ["Salário", "Vale transporte", "Vale alimentação"], 0, 0

for l in range (3):
    for c in range (3):
        m[l].append(float(input(f"Digite os dados do {l+1}° estagiário [{l}][{c}] ({info[c]}): ")))
        if c == 0:
            somasal += m[l][c]
        if c == 1:
            somatra += m[l][c]
print("Salários/Transporte/Alimentação")
for l in range (3):
    for c in range (3):
        print(f"[{m[l][c]:^7}]", end = "")
    print()
print("A média salarial é de {:.2f}".format (somasal/3))
print("A soma dos valores pagos por vale transporte é:",somatra)