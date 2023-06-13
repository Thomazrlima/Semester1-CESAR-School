print("Bem vindo ao sistema de cálculo de salário da concessionária tampinha \n")
salario_fixo = float(input("Digite o valor do seu salário fixo "))
comissao = float(input("Digite o valor da sua comissão por carro "))
venda = float(input("Digite o valor total de suas vendas "))
carro = int(input("Digite o número de carros por você vendidos "))

novo_salario = salario_fixo + (comissao*carro) + (venda*0.05)

print("Seu novo salário será ", novo_salario)