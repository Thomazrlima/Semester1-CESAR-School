import os
os.system('cls')
while True:
    try:
        n = int(input("Digite de qual número você deseja ver a raiz quadrada: "))
        print(f"A raiz quadrada do seu número é {n**(1/2)}")
        break
    except ValueError:
        print("Digite um número inteiro válido válido!")