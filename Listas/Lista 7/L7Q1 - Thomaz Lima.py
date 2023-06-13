import os
os.system('cls')
vetor,igual,menor,maior = [], 0,0,0
while True:
    try:
        for i in range(10):
            vetor.append(float(input(f"Digite o {i+1}° número: ")))
            if i > 0:
                if vetor[i] == vetor[0]:
                    igual+=1
                elif vetor[i] > vetor[0]:
                    maior+=1
                elif vetor[i] < vetor[0]:
                    menor+=1
        print(f"{igual} números são iguais ao primeiro elemento, {maior} maiores e {menor} menores")
        break
    except ValueError:
        print("Digite um número válido")