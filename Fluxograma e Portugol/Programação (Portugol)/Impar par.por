programa {
  funcao inicio() {
    inteiro n1
    caracter operacao
    real resultado

    escreva("Escolha um número inteiro ")
    leia(n1)
    escreva("Escolha uma ação para realizar com o número, A(Dobrar), B(Elevar ao Quadrado), C(Indentificar se é par ou ímpar) ")
    leia(operacao)

    escolha(operacao){
    caso 'A':
    caso 'a':
    resultado = n1*2
    escreva("O dobro desse número é ", resultado) pare
    caso 'B':
    caso 'b':
    resultado = n1*n1
    escreva("Esse número ao quadrado é ", resultado) pare
    caso 'C':
    caso 'c':
    resultado = n1 %2
    se(resultado == 1) {
      escreva("O seu número é Ímpar")
    }
    senao {
      escreva("Seu número é par")
    } pare
    caso contrario
    escreva("Operação inválida")
    }
  }
}
