programa {
  funcao inicio() {
    real dias, km, preco
    cadeia nome

    escreva("Digite o nome do titular do cartão ")
    leia(nome)
    escreva("Digite a quantidade de dias que você passou com o veículo ")
    leia(dias)
    escreva("Digite quantos Km você rodou com o veículo (precisão de 1 casa decimal) ")
    leia(km)

    preco = (km*0.2)+(dias*90)

    escreva(nome, " o seu valor a pagar é ", preco, " R$")
  }
}
