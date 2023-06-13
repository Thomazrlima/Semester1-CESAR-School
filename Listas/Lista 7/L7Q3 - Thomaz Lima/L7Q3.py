import os
os.system('cls')
armazem = []
def esc(armazem):
    with open('L7Q3.txt', 'w') as arq:
        armazem.sort()
        for i in range(6):
            arq.write(f"{armazem[i]}\n")
    with open('L7Q3.txt', 'r') as arq:
        print(arq.read())
while True:
    try:
        for i in range(6):
            nome = input(f"Digite seu nome {i+1}° pessoa: ")
            armazem.append(nome)
        esc(armazem)
        break
    except (RuntimeError, TypeError, NameError):
        print("Encontramos um problema, tente novamente")