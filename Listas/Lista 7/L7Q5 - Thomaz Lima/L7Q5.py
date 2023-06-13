import os
os.system('cls')
n,n1 = [], []
def criar(nome,n):
    with open(nome, 'w') as arq:
        for j in range(6):
            arq.write(f"{n[j]}\n")
def mudar(n1):
    with open(nome, 'w') as arq:
        for j in range(6):
            arq.write(f"{n1[j]}")
nome = input("Digite o nome da seu arquivo: ")
nome = nome+'.txt'
for i in range(6):
    n.append(input(f"Digite seu nome e subrenome usuário {i+1}: "))
criar(nome,n)
for k in range(6):
    resp = input((f"{n[k]} você deseja alterar esse nome?: ")).lower()
    if resp == 'sim':
        novo = input("Digite o novo nome: ")
        with open(nome, 'r') as arq1:
            n1 = arq1.readlines()
            n1[k] = (f"{novo}\n")
        mudar(n1)
with open(nome, 'r') as arq:
    print(arq.read())