import os
os.system("cls")

unidade = ["da unidade 1", "da unidade 2", "porcentagem"]
v = ["nota", "nota", "frequência"]
media = 0
materia =  ["FP", "IC", "SD"]
m = [[],[],[]]

for l in range (3):
    for c in range(3):
        m[l].append(float(input(f"Digite a sua {v[c]} {unidade[c]} em {materia[l]}: ")))
        if c == 0:
            media += m[l][c]

print("    U1     U2     FQ")
for l in range (3):
    print(f"{materia[l]}",end = "")
    for c in range(3):
        print(f"{m[l][c]:^7}", end = "")
    print("%")
print(f"Sua média na unidade 1 foi: {(media/3)}")