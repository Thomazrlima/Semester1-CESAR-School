programa {
  funcao inicio() {
    real preco, km

    escreva("Digite a distância que você deseja percorer ")
    leia(km)

    se(km <= 200){
      preco = km*0.5
      escreva("O preço da sua passagem é ", preco, " R$")
    }
    senao{
      preco = km*0.45
      escreva("O preço da sua passagem é ", preco, " R$")
    }
    
  }
}
