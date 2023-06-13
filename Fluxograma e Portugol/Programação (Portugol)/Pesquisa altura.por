programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    inteiro cont, contf = 0, contm = 0
    real media, media1, altura, soma = 0.0, soma1 = 0.0, maior = 0, menor = 3
    caracter sexo

    para(cont=1; cont <= 5; cont++){
      escreva("Digite o seu sexo (F/M) ")
      leia(sexo)
      escreva("Digite sua altura ")
      leia(altura)
      se(altura > maior){
        maior = altura
      }
      se(altura < menor){
        menor = altura
      }
      se(sexo == 'F' ou sexo == 'f'){
        soma += altura
        contf++
      }
      senao{
        soma1 += altura
        contm++
      }
      }
    media = mat.arredondar(soma/contf,2)
    media1 = mat.arredondar(soma1/contm,2)
    escreva(contf, " Mulheres responderam essa pesquisa, e a média de suas alturas foi de ", media, "\n")
    escreva(contm, " Homens responderam essa pesquisa, e a média de suas alturas foi de ", media1, "\n")
    escreva(maior, " foi a maior altura da pesquisa, e ", menor, " foi a menor registrada")
  }
}
