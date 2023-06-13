programa{
	funcao inicio(){
		inteiro hora, dia, min, seg

		escreva("Digite o número de dias que você estuda por semana ")
		leia(dia)
		escreva("Digite o número de horas ")
		leia(hora)
		escreva("Digite o número de minutos ")
		leia(min)
		escreva("Digite o número de segundos ")
		leia(seg)

		escreva("Você passa ", (dia*86400)+(hora*3600)+(min*60)+seg, " segundos estudando por semana")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 322; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */