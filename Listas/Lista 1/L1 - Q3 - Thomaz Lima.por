programa {
  funcao inicio() {
    real n1, n2, n3, media

    escreva("Digite a nota da primieira avaliação ")
    leia(n1)
    escreva("Digite a nota da segunda avaliação ")
    leia(n2)
    escreva("Digite a nota da terceira avaliação ")
    leia(n3)

    media = (n1*2 + n2*3 + n3*5)/10

    se(media >= 7){
      escreva("O Aluno foi aprovado, média ", media)}
    senao{
      escreva("O Aluno foi reprovado ", media)
    }
  }
}
