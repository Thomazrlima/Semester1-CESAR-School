programa{
	funcao inicio(){
		inteiro n, cont, resul = 1
		
		escreva("Digite o número que você deseja ver o fatorial ")
		leia(n)
		
		para(cont = n; cont >= 2; cont--){
			resul *= cont
		}
		escreva("O resultado do fatorial é ", resul)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 164; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */