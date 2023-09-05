a,b,c = map(float,input().split())
vetor = [a,b,c]
vetor.sort(reverse=True)
a,b,c = vetor
def tipo(lado1,lado2,lado3):
    if (lado1 == lado2 == lado3):
        print("TRIANGULO EQUILATERO")
    elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
        print("TRIANGULO ISOSCELES")
if (a >= (b+c)):
    print("NAO FORMA TRIANGULO")
elif (a*a > ((b*b)+(c*c))):
    print("TRIANGULO OBTUSANGULO")
    tipo(a,b,c)
elif (a*a < ((b*b)+(c*c))):
    print("TRIANGULO ACUTANGULO")
    tipo(a,b,c)
elif (a*a == ((b*b)+(c*c))):
    print("TRIANGULO RETANGULO")