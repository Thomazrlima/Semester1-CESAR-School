programa {
	funcao inicio() {
		inteiro cont, cont2, cont3
		
		escreva("Digite o número que você deseja ver a tabuada ")
		leia(cont3)
		escreva("Digite com qual número que você deseja inciar ")
		leia(cont)
		escreva("Digite com qual número que você deseja parar ")
		leia(cont2)
		
		para( ; cont <= cont2; cont++){
		    escreva(cont3, " x ", cont, " = ", cont3* cont, "\n")
		}
		
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 265; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */