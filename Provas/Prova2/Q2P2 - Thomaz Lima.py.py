import os
os.system('cls')
soma = 0
frase = input("Digite sua frase: ").strip().split(' ')
for i in range(len(frase)):
    for c in frase[i]:
        if c == 'e':
            soma+=1
if soma == 0:
        print("Não existe")
else:
    print(f"Existem {soma} e nessa frase")
print(f"Exstem {len(frase)} palavras nessa frase")
if len(frase) < 3:
     print("Essa frase não tem 3° palavra")
else:
    print(frase[2])