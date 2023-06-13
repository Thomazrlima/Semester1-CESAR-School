import os
os.system('cls')
def f (frase):
    palavras = len(frase.split())
    return palavras
frase = input("Digite sua frase: ")
print(f"O total de palavras na sua frase é {f(frase)}")