programa{
	funcao inicio(){
		inteiro cont, cand, somavoto = 0, somaidade = 0, idade, branco = 0, maior = 0, menor = 9999, voto = 0

		para(cont = 1; cont <= 6; cont++){
			escreva("Pedro PTP(1)\t Edu FDS(2)\t Evaldo TNC(3)\t Branco/Nulo(4)\n")
			escreva("Em qual candidato você deseja votar? ")
			leia(cand)
			escreva("Por fim, digite sua idade ")
			leia(idade)
			limpa()
			se(maior < idade){
				maior = idade
			}
			se(menor > idade){
				menor = idade
			}
			escolha(cand){
				caso 1:
				somavoto++
				pare
				caso 2:
				somaidade += idade
				voto++
				pare
				caso 4:
				branco++ 
				pare
			}
		}
		escreva("Auditoria completa, o todal de votos para o candidado 1 foi, ", somavoto, ", a média de idade dos eleitores do 2° foi ", somaidade/voto, ", o total de votos nulos foi ", branco, ", e por fim, a maior idade foi, ", maior, " e a menor foi, ", menor)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 521; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */