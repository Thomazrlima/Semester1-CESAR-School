import math
n = int(input("Digite a quantidade de equações que você deseja descobrir o resultado "))

for i in range (1,n+1):
    a = float(input("Digite o valor do a: "))
    if a == 0:
        print("Essa não é uma equação do seundo grau")
    else:
        b = float(input("Digite o valor do a: "))
        c = float(input("Digite o valor do a: "))
        delta = (b**2)-4*a*c
        r = (-(b) + (delta)**0.5)/2*a
        rl = (-(b) - (delta)**0.5)/2*a
        if delta < 0:
            print("Essa equação não possui raizes")
        elif delta == 0:
            print("Essa equação só possui uma raiz, que é", r)
        elif delta > 0:
            print("As raizes são: ",r," e ",rl)