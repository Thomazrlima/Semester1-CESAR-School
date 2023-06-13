casa = input("Digite o nome do time da casa: ")
fora = input("Digite o nome do time visitante: ")
gc = int(input("Digite quantos gols o time da casa marcou: "))
gf = int(input("Digite quantos gols o time visitante marcou: "))

if gc > gf:
    print(casa,"Ganhou a partida por ",gc,"x",gf)
elif gf > gc:
    print(fora,"Ganhou a partida por ",gf,"x",gc)
else:
    print("O jogo acabou em Empate ",gc,"x",gf," foi o resultado da partida")