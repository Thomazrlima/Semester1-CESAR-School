senha = input("Informe a Senha a ser utilizada: ")
tem_masc = False
tem_minsc = False
tem_num = False
tem_chac_esp = False
for letra in senha:
    if letra.islower():
        tem_minsc = True
    if letra.isupper():
        tem_masc = True
    if letra.isnumeric():
        tem_num = True
    if letra in ['$','*','%','|']:
        tem_chac_esp = True

if tem_masc and tem_minsc and tem_num and tem_chac_esp:
    print('Senha válida')
else:
    print('Senha inválida')
