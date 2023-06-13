programa {
  funcao inicio() {
    real altura, peso, imc

    escreva("Digite o seu peso atual (Em Kg) ")
    leia(peso)
    escreva("Digite a sua altura (Em metros) ")
    leia(altura)

    imc = peso/(altura*altura)

    se(imc < 18.5){
      escreva("Você se encontra abaixo do peso ideal, seu IMC é de ", imc)}
    se(imc >= 18.5 e imc <= 25.0){
      escreva("Você se encontra no peso ideal, seu imc é de ", imc)}
    se(imc > 25 e imc <= 30.0){
      escreva("Você se encontra com sobrepeso, seu imc é de ", imc)}
    se(imc > 30 e imc <= 40.0){
      escreva("Você se encontra com obesidade, seu imc é de ", imc)}
    se(imc > 40){
      escreva("Você se encontra com obesidade mórbida, seu imc é de ", imc)
    }

    
  }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 637; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */