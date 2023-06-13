programa{
	inclua biblioteca Matematica --> mat
	funcao inicio(){
		inteiro cont, cand, somavoto = 0, somaidade = 0, idade, branco = 0, maior = 0, menor = 9999, voto = 0

		para(cont = 1; cont <= 6; cont++){
			escreva("Pedro PTP(1)\t Edu FDS(2)\t Evaldo TNC(3)\t Branco/Nulo(4)\n")
			escreva("Em qual candidato você deseja votar? ")
			leia(cand)
			escreva("Por fim, digite sua idade ")
			leia(idade)
			limpa()
			
			escolha(cand){
				caso 1:
				somavoto++
				se(maior < idade)
				{
					maior = idade
				}
				se(menor > idade)
				{
					menor = idade
				}
				pare
				caso 2:
				somaidade += idade
				voto++
				pare
			}
			se(voto == 0)
			{
				voto = 1
			}
			se(cand == 4)
			{
				branco++
			}
		}
		escreva("\nAuditoria completa, o todal de votos para o candidado 1 foi(foram) ", somavoto, "\n")
		escreva("A média de idade dos eleitores do 2° foi ", somaidade/voto, "\n")
		escreva("O total de votos nulos foi aproximadamente ", mat.arredondar((branco*100)/6 ,1), "%\n")
		escreva("Por fim, a maior idade dos eleitores do 1° candidato foi, ", maior, " e a menor foi, ", menor, "\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 803; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */