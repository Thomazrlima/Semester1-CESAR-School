def med(n1, n2):
    media = (n1+n2)/2
    return media
def status(med):
    if med > 6:
        print("Aprovado")
    elif med > 4:
        print("Verificação suplementar")
    else:
        print("Reprovado")
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
print(f"Sua média foi {med(n1,n2)}")
med = med(n1,n2)
status(med)