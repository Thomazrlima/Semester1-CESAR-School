programa{
	funcao inicio(){
		inteiro n1, n2, n3

		escreva("Digite o número que você deseja ver a tabuada ")
		leia(n1)
		escreva("Digite com que número você deseja começar ")
		leia(n2)
		escreva("Digite com que número você deseja terminar ")
		leia(n3)

		se(n3 < n2){
			escreva("Deixa de ser burro, animal")
		}

		para(;n2 <= n3; n2++)
		{
			escreva(n1, " x ", n2, " = ", n1*n2, "\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 379; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */