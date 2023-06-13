programa{
	funcao inicio(){
		inteiro n, cont1 = 0, cont2 = 0, cont3 = 0, cont4 = 0

		faca{
			escreva("Digite um número ")
			leia(n)
			se(n >=0 e n <= 25){
				cont1++
			}
			senao se(n <= 50){
				cont2++
			}
			senao se(n <= 75){
				cont3++
			}
			senao se(n <= 100){
				cont4++
			}
		}enquanto(n > 0)
		escreva(cont1, " número(s) estão entre 0 e 25, ", cont2, " número(s) estão enre 26 e 50", cont3, " número(s) estão entre 51 e 75 e por fim, ", cont4, " número(s) estão entre 76 e 100")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 88; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */