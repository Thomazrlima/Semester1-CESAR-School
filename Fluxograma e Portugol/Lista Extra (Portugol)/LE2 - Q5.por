programa{
	funcao inicio(){
		inteiro n1, maior = 0, menor = 9999999, cont = 1

		enquanto(cont <= 3){
		escreva("Digite o ", cont,"° número ")
		leia(n1)
		se(n1 > maior){
			maior = n1
		}
		se(n1 < menor){
			menor = n1
		}
		cont++
		}
		escreva("O maior dos três números é ", maior, " e o menor é ", menor)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 271; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */