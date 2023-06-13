programa{
inclua biblioteca Matematica --> mat
	funcao inicio(){
		real divida
		caracter operacao

		escreva("Bem vindo ao programa de renegociamento de Dívida do Serasa\n")
		escreva("Digite o valor da dívida que você deseja renegonciar ")
		leia(divida)
		escreva("Valor da Dívida:\tJuros:\t \tQuantidade de parcelas: \tValor das Parcelas:\n")
		escreva(divida,"\t\t\t", divida-divida, "\t\t", "1 \t\t\t\t", divida, "\n")
		escreva(divida*1.10, "\t\t\t", mat.arredondar((divida*1.10)-divida , 2), "\t\t", "3 \t\t\t\t", mat.arredondar(divida*1.10/3, 2), "\n")
		escreva(divida*1.15, "\t\t\t", mat.arredondar((divida*1.15)-divida ,2), "\t\t", "6 \t\t\t\t", mat.arredondar(divida*1.15/6, 2), "\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 708; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */