programa{
inclua biblioteca Matematica --> mat
	funcao inicio(){
		inteiro cont, func
		real salario, soma = 0, soma1 = 0

		escreva("Bem vindo ao sistema de cálculo de salários\n")
		escreva("Digite o número de funcionários da sua empresa ")
		leia(func)

		para(cont = 1; cont <= func; cont++)
		{
			escreva("Digite o salário do seu ", cont, "° funcionário ")
			leia(salario)
			soma += salario
			soma1 += mat.arredondar(salario*0.08, 2)
		}
		escreva("Devido ao aumento dos salários em 8% a empresa terá que pagar uma folha de ", soma, " que representa um acréscimo de ", soma1)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 446; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */