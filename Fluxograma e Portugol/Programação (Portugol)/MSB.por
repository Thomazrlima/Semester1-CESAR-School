programa {
  funcao inicio() {
    real n1, n2, resultado
    caracter operacao

    escreva("Escolha um número ")
    leia(n1)
    escreva("Escolha outro número ")
    leia(n2)
    escreva("Escolha uma operação para realizar com os 2 números(B,M,S) ")
    leia(operacao)

    escolha(operacao){
      caso 'S':
      caso 's':
      resultado = n1+n2
      escreva("O resultado foi ", resultado)
      pare
      caso 'M':
      caso 'm'
      resultado = n1*n2
      escreva ("O resultado foi ", resultado)
      pare
      caso 'B'
      caso 'b'
      resultado = n1-n2
      escreva("O resultado foi ", resultado)
      pare
      caso contrario
      escreva("Preste mais antenção!")
      pare
    }
  }
}
