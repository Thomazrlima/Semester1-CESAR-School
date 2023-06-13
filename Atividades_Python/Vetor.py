vetor =[3.5,6.7,1.0,4.9]
vetor.insert(1, 2.3)
print(vetor)
vetor.pop()
print(vetor)
vetor[2] = 9.2
print(vetor)
vetor.sort()
print("Vetor =",vetor,len(vetor))
for valor in vetor:
    print('[{0}] = {1}'.format(vetor.index(valor),valor))