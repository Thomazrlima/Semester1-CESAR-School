programa{
	funcao inicio(){
		inteiro area, valor

		escreva("Bem vindo ao programa de cálclulo de IPTU da cidade de Recife\n")
		escreva("Digite a área do seu imóvel (em m2) ")
		leia(area)

		se(area < 200)
		{
			valor = area*1.5
		}
		senao se(area < 300)
		{
			valor = area*2
		}
		senao se(area < 500)
		{
			valor = area*4
		}
		senao{
			valor = area*5
		}
		escreva("O valor do seu IPTU foi ", valor)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 179; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */