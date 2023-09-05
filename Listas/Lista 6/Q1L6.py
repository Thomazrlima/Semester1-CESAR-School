while True:
    def roberto(n):
        robson = (n*2)/3
        return robson
    try:
        votos = []
        n = int(input())
        votos.append(((input())).split(' '))
        x = votos[0].count("1")
        if x >= roberto(n):
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break