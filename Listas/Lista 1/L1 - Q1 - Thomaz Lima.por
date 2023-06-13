programa {
  funcao inicio() {
    real altura, comprimento, area, litros , lata
    
    escreva("Qual a altura da parede que você vai pintar? ")
    leia(altura)
    escreva("Por último, informe o comprimento da parede ")
    leia(comprimento)

    area = altura*comprimento
    litros = area/2
    lata = litros/18

    escreva("Sua parede tem ", area," m², e precisará de ", litros," de tinta, o que equivale a ", lata," latas.")

  }
}
