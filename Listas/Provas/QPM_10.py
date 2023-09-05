l1 = float(input("Digite o tamanho do 1° lado: "))
l2 = float(input("Digite o tamanho do 2° lado: "))
l3 = float(input("Digite o tamanho do 3° lado: "))

if l1 < l2+l3 and l2 < l3+l1 and l3 < l1+l2:
    print("Isso sim é um triângulo")
else:
    print("Não foi dessa vez que vimos um triângulo")