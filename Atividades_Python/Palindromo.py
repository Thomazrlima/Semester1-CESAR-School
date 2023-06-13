import os
os.system("cls")

print("Será que sua frase é um palindromo? Teste aqui: ")
pali = input().lower()
pali = pali.replace(' ', '')

if pali == pali[::-1]:
    print("Sua frase é um Palindromo! Parabéns?")
else:
    print("Não diga que a canção está perdida, Tenha fé em Deus, tenha fé na vida, Tente outra vez!")