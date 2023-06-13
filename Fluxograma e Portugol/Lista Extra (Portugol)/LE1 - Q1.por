programa{
	funcao inicio(){
		inteiro base, ex, cont, resultado, base1
		escreva("Digite o número que será a base ")
		leia(base)
		escreva("Digite o número qeu será o expoente ")
		leia(ex)
		base1 = base

		para(cont = 1; cont <= ex; cont++){
			resultado = base1*base
			base1 = resultado
		}
		escreva("O resultado da operação é ", base1)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 210; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */