nome = input("Insira o nome do primeiro jogador: ")
nome1 = input("Insira o nome do segundo jogador: ")

variante = input("Primeiro jogador selecione: Par/Impar ")
num = int(input("Informe o valor jogado pelo primeiro jogador "))
num1 = int(input("Informe o valor jogado pelo segundo jogador "))

soma = num + num1

if soma % 2 == 0:
    print("O resultado foi Par")
    if variante == "par":
        print("Vencedor foi", nome)
    else:
        print("Vencedor foi", nome1)
else:
    print("O resultado foi Impar")
    if variante == "Impar":
        print("Vencedor foi", nome)
    else:
        print("Vencedor foi", nome1)
