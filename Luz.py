print("Bem vindo ao sistema de cálculo de conta da Celpe")
uso = float(input("Digite o seu consumo de energia elétrica no mês em Kw "))

if uso <= 500:
    conta = uso*0.02
elif uso <= 1000:
    conta = uso*10
else:
    conta = uso*35
print("Sua conta de energia ficou em ", conta, " R$, com o adicional da taxa de serviço fica em", conta+5, "R$")