programa{
	funcao inicio(){
		inteiro n1,n2, soma = 0
		
		escreva("Digite o primeiro número do intervalo ")
		leia(n1)
		escreva("Digite o segundo número do intervalo ")
		leia(n2)

		enquanto(n1 < n2){
			se(n1%2 == 0){
				n1 += 2
				soma += n1
				se(n2%2 != 0){
					n2 -= 1
				}
			}
			senao{
				n1 += 1
				soma += n1
			}
			escreva(n1, "\n")
		}
		escreva("A soma final foi ", soma)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 280; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */