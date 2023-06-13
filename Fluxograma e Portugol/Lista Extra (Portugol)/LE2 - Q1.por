programa{
	inclua biblioteca Matematica --> mat
	funcao inicio(){
		real tempo, km
		
		escreva("Digite a distância que você deseja percorrer(km) ")
		leia(km)
		escreva("Digite o tempo que você tem disponível para a prática da atividade(horas) ")
		leia(tempo)
		escreva("Para a pártica desse exercício no tempo desejado você deve manter um rítimo de, ", mat.arredondar((km*1000)/(tempo*3600) ,2), " m/s")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 398; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */