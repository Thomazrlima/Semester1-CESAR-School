vezes = int(input())
for i in range (vezes):
    ps = input().strip().split(' ')
    dec = ''
    for p in ps:
        if len(p) != 0:
            dec += p[0]
    print(dec)