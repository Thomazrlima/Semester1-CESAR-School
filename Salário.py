print("Bem vindo ao sistema de ajuste de salários da empresa do malvado Doofenshmirtz")
ano = int(input("Digite o ano em que você foi contratado "))
tempo = int(input("Digite quantos anos fazem desde o seu último reajuste "))
salario = float(input("Digite o seu salário "))

if 2023 - ano >= 10:
    if 2023 - ano >= 2:
        print("Você não pode receber o reajuste")
    else:
        print("O seu reajuste será de ", salario*1.3)
elif 2023 - ano >= 5:
    if 2023 - ano >= 2:
        print("Você não pode receber o reajuste")
    else:
        print("O seu reajuste será de ", salario*1.2)
else:
    if 2023 - ano >= 2:
        print("Você não pode receber o reajuste")
    else:
        print("O seu reajuste será de ", salario*1.1)