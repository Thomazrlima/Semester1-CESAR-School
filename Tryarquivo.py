a = []
try:
    with open ('Eymael.txt', 'r+') as arq:
        lista = arq.read()
        lista = list(lista)
        for i in lista:
            if i == 'a':
                i = 'A'
        arq.writelines(lista)
        a = arq.readlines()
        print(a)
except FileNotFoundError:
    print("Esse arquivo não existe!")