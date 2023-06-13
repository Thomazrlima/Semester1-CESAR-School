maior_vel, novo, cont = 0, 0, 0

while True:
    nome = input("Digite o nome do carro: ")
    if nome == 'n' or nome == 'N':
        break
    else:
        ano = int(input("Digite o ano do carro: "))
        vel = float(input("Digite a velocidade máxima do carro (em Km/h): "))
        if novo < ano:
            novo = ano
            anonome = nome
        if maior_vel < vel:
            maior_vel = vel
            velnome = nome
    cont += 1
print("No total",cont,"carros foram registrados, o mais novo é",anonome,"lançado em",novo)
print("O mais rápido é o",velnome,"que chega a",maior_vel,"km/h")