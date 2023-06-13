vetor = []
vetor.append(input("Você conhece a vítima do furto? ").lower())
vetor.append(input("Esteve no local do furto? ").lower())
vetor.append(input("Mora perto da vítima? ").lower())
vetor.append(input("A vitima lhe devia? ").lower())
vetor.append(input("Já trabalhou com a vítima? ").lower())
if vetor.count("sim") == 5:
    print("Ladrão")
elif vetor.count("sim") >= 3:
    print("Cúmplice")
elif vetor.count("sim") == 2:
    print("Suspeito")
else:
    print("Inocente")