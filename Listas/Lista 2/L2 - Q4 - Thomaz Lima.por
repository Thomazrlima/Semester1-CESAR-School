programa {
	inclua biblioteca Matematica --> mat
	funcao inicio() {
	real peso
	caracter planeta
	
		escreva("Digite o seu peso em KG ")
          leia(peso)
          escreva("Suas Opções são\n")
          escreva("N°1 - Mercúrio\n")
          escreva("N°2 - Vênus\n")
          escreva("N°3 - Marte\n")
          escreva("N°4 - Júpiter\n")
          escreva("N°5 - Saturno\n")
          escreva("N°6 - Urano\n")
          escreva("Digite o planeta do sistema solar que você deseja visitar ")
		leia(planeta)
		
          escolha(planeta){
          caso '1':
          escreva(mat.arredondar((peso/10)*0.37, 2), " Seria o seu peso em Mercúrio")
          pare
          caso '2':
          escreva(mat.arredondar((peso/10)*0.88, 2), " Seria o seu peso em Vênus")
          pare
          caso '3':
          escreva(mat.arredondar((peso/10)*0.38, 2), " Seria o seu peso em Marte")
          pare
          caso '4':
          escreva(mat.arredondar((peso/10)*2.64, 2), " Seria o seu peso em Júpiter")
          pare
          caso '5':
          escreva(mat.arredondar((peso/10)*1.15, 2), " Seria o seu peso em Urano")
          pare
          caso '6':
          escreva(mat.arredondar((peso/10)*1.17, 2), " Seria o seu peso em Urano")
          pare
          caso contrario:
          escreva("Digite uma opção válida")
          pare
          }
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1211; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */