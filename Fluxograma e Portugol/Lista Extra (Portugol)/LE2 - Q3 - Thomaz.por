programa{	
	funcao inicio()
	{
	inteiro n = 0, cont, maior = 0, menor = 999999
	enquanto(n != -1)
	{
		escreva("Digite um número ")
		leia(n)
		se(n == -1)
		{
			pare
		}
		se(maior < n)
		{
			maior = n
		}
		se(menor > n)
		{
			menor = n
		}
	}
	para(cont = menor; cont <= maior; cont++)
	{
		se(cont == 2 ou cont == 3 ou cont == 5 ou cont == 7)
		{
			escreva(cont,"\n")
		}
		se(cont%2 != 0 e cont%3 != 0 e cont%5 != 0 e cont%7 != 0)
		{
			escreva(cont,"\n")
		}
	}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 380; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */