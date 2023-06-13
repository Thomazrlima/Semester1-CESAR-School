programa{
inclua biblioteca Matematica --> mat
	funcao inicio(){
		inteiro idade, n, cont, soma = 0
		
		escreva("Digite quantas pessoas tem na sua turma ")
		leia(n)

		para(cont = 1; cont <= n; cont++){
			escreva("Digite a idade da ", cont, "° pessoa ")
			leia(idade)
			soma += idade
		}
		se(soma/n <25){
			escreva("Sua turma é jovem, a média de idades é somente ", mat.arredondar(soma/n ,2))
		}
		senao se(soma/n < 60){
		escreva("Sua turma é adulta, a média de idades é ", mat.arredondar(soma/n ,2))
		}
		se(soma/n > 60){
		escreva("Sua turma é idosa, a média de idades é ", mat.arredondar(soma/n ,2))
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 258; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */