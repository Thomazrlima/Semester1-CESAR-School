print("Bem vindo ao sistema financeiro do banco da empresa do malvado Doofermitz")
valorcasa = float(input("Digite o valor da casa: "))
salrio = float(input("Digite seu salário: "))
anos = int(input("Digite o número de anos que você deseja pagar: "))

prestacao =  valorcasa/(anos*12)

if prestacao <= salrio*0.3:
    print("Parabéns, seu empréstimo foi aprovado, o valor da sua parcela será: ",prestacao)
else:
    print("Infelizmente você teve o empréstimo negado")