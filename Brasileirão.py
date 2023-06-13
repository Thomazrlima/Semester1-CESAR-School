import os
os.system("cls")
tabela = ("Sport","Botafogo", "Fortaleza","Palmeiras","Internacional","Fluminense","Cruzeiro","Grêmio","São Paulo","Vasco")
print("G4")
for i in range (4):
    print(tabela[i])
print("Z4")
for i in range (6, 10):
    print(tabela[i])
print(f"O são paulo está na {tabela.index('São Paulo') + 1}° lugar")
print("Tabela em ordem alfabética")
tab = list(tabela)
tab.sort()
print(tab)