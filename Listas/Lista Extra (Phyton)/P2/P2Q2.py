import os
os.system("cls")
fibo = [1,1]

quant = int(input("Quantos elementos da sequência de Fibonacci você deseja ver? "))
for i in range (quant):
    print(f"{fibo[i]}", end = " ")
    if i >= 1:
        fibo.append(fibo[i]+fibo[i-1])