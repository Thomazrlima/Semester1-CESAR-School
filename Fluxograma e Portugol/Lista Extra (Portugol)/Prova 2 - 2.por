programa{
	funcao inicio(){
		real peso, ex, multa
		inteiro cont

		escreva("Bem vindo ao programa de envio dos Correios\n")

		para(cont = 1; cont <= 3; cont++)
		{
			escreva("Digite o ", cont, " peso ")
			leia(peso)
				se(peso > 500)
				{
					ex = peso - 500
					se(ex <= 100)
					{
						multa = ex*5
					}
					senao se(ex <= 500)
					{
						multa = ex*8
					}
					senao se(ex <= 1000)
					{
						multa = ex*10
					}
					senao
					{
						multa = ex*15
					}
					escreva("O valor da sua multa nesse produto é de ", multa, "\n")
				}
			senao
			{
				escreva("Esse produto não será multado\n")
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 550; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */