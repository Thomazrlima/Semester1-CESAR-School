lista = [10 , 3 , 2 , 7 , 1 , 9 , 6]

for i in range(len(lista)):
    min = i
    for j in range(i+1,len(lista)):
        if lista[min] > lista[j]:
         min = j
    temp = lista[i]
    lista[i] = lista[min]
    lista[min] = temp
    print(lista)
print("Lista final",lista)