while True:
    nome = input('Digite o nome do Atleta: ')

    if nome == 'sair':
        break

    dist, salt, i = [], [], 1

    while i <= 5:
        for sus in range(5):
            dist.append(float(input(f"Digite a distância do salto {i}°: ")))
            salt.append(i)
            i += 1
        for sus2 in range(5):
            print(salt[sus2],"° Salto:",dist[sus2])
        print("Média dos saltos: {:.2f} m".format(sum(dist)/5))