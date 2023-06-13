programa{
inclua biblioteca Matematica --> mat
	funcao inicio(){
		inteiro cont, idade, voto, soma = 0, idade4 = 0, cont4 = 0, maior = 0, menor = 9999999

		escreva("Bem vindo ao sistema de avaliação de eventos C.E.S.A.R. School\n")

		para(cont = 1; cont <= 5; cont++)
		{
			escreva("Digite a sua idade ")
			leia(idade)
			escreva("De uma nota de 1 até 5 qual o seu nível de satisfação com a semana e imersão ")
			leia(voto)

			escolha(voto)
			{
				caso 5:
				soma++
				caso 1:
				idade4 += idade
				cont4++
			}
			se(menor > idade)
			{
				menor = idade
			}
			se(maior < idade)
			{
				maior = idade
			}
		}
		escreva("O total de pessoas que deu nota máxima foi ", soma, ", a média de idade das pessoas que não ficaram nem um pouco satisfeitas foi ", mat.arredondar(idade4/cont4 ,2), ", o mais velho a responder tem ", maior, " anos e o mais novo ", menor)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 511; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */