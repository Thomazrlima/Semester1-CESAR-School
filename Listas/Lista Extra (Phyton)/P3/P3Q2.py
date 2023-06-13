import os
os.system('cls')
valores, soma = [], 0

def valorPagamento (val, dia):
    if dia != 0:
        val = val + (val*0.03) +  (val*(dia*0.01))
    return val

while True:
    try:
        val = float(input("Digite o valor da prestação a ser paga: "))
        valores.append(val)
        if val == 0:
            break
        dia = int(input("Digite a quantidade de dias em atraso: "))
        print(valorPagamento (val, dia))
        soma += valorPagamento (val, dia)
    except ValueError:
        print("Digite um número válido")
print(f"{len(valores)-1} Parcelas pagas no dia, Total: {soma}")