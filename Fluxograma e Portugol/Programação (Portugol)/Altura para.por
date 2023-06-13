programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    inteiro jogadores, cont
    real media, altura, soma=0
    
    escreva("Quantos jogadores você treina? ")
    leia(jogadores)
    para(cont=1; cont <= jogadores; cont++){
      escreva("Digite a altura do jogador ", cont, " (com 2 casas decimais) ")
      leia(altura)
      soma += altura
     }
     media = mat.arredondar(soma/jogadores,2)
     escreva("A média de altura do seu time é de ", media)
  }
}
