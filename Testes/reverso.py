def f (n):
    n1 = str(n)
    return n1[::-1]
n = int(input("Digite seu número: "))
print(f"Seu número reverso é {f(n)}")