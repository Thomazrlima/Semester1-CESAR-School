import os
os.system("cls")
v = [1, 1]
fibo = int(input("Quantos números da sequência de Fibonacci você deseja visualizar: "))

for i in range (fibo):
    print(v[i])
    if i >= 1:
        v.append(v[i]+v[i-1])