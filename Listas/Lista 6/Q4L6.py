def prt(vetor, nota, moeda):
    print("NOTAS:")
    for i in range (6):
        print(vetor[i], nota[i])
    print("MOEDAS:")
    for i in range (6):
        print(vetor[i+6], moeda[i])
vetor, nota = [0,0,0,0,0,0,0,0,0,0,0,0], ["nota(s) de R$ 100.00", "nota(s) de R$ 50.00", "nota(s) de R$ 20.00", "nota(s) de R$ 10.00", "nota(s) de R$ 5.00", "nota(s) de R$ 2.00"]
valor, moeda = float(input()), ["moeda(s) de R$ 1.00", "moeda(s) de R$ 0.50", "moeda(s) de R$ 0.25", "moeda(s) de R$ 0.10", "moeda(s) de R$ 0.05", "moeda(s) de R$ 0.01"]
valor = valor*100
while True:
    if valor - 10000 > 0:
        vetor[0] += 1
        valor = valor-10000
    elif valor - 5000 > 0:
        vetor[1] += 1
        valor = valor-5000
    elif valor - 2000 > 0:
        vetor[2] += 1
        valor = valor-2000
    elif valor - 1000 > 0:
        vetor[3] += 100
        valor = valor-1000
    elif valor - 500 > 0:
        vetor[4] += 1
        valor = valor-500
    elif valor - 200 > 0:
        vetor[5] += 1
        valor = valor-200
    elif valor - 100 > 0:
        vetor[6] += 1
        valor = valor-100
    elif valor - 50 > 0:
        valor = valor-50
        vetor[7] += 1
    elif valor - 25 > 0:
        vetor[8] += 1
        valor = valor-25
    elif valor - 10 > 0:
        vetor[9] += 1
        valor = valor-10
    elif valor - 5 > 0:
        vetor[10] += 1
        valor = valor-5
    elif valor - 1 >= 0:
        vetor[11] += 1
        valor = valor-1
    if valor <= 0:
        break
prt(vetor, nota, moeda)