vezes = int(input())
vantagens = {'papel': ["pedra", "spock"], 'tesoura': ["papel", "lagarto"], 'pedra': ["tesoura", "lagarto"], 'spock': ["pedra", "tesoura"], 'lagarto': ["papel", "spock"]}
for i in range (vezes):
    rajesh, sheldon = input().strip().split(' ')
    if rajesh in vantagens[sheldon]:
        print("sheldon")
    elif rajesh == sheldon:
        print("empate")
    else:
        print("rajesh")