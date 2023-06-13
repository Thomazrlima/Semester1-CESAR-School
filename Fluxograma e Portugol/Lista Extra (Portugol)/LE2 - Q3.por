programa
{
	funcao inicio()
	{
		inteiro n = 0, menor = 90999999 , maior = 0, cont=0, valor = 1, div = 0

		para(inteiro i = 0; i != -1;cont++)
		{
			escreva("Digite um número ")
			leia(i)

			se(i == 0)
			{
				menor = i
				maior = i
				
			}
			senao se(maior < i e i>=0 )
			{
				maior = i
			}
			senao se(menor > i e i >= 0)
			{
				menor = i
			}
		}
		
		n = maior
		
		enquanto(n >= menor)
		{
			se(n == 1 ou n == 2)
			{
				escreva(n,"\n")
				n--
			}
			senao
			{
				enquanto(valor <= n)
				{
					se(n%valor == 0)
					{
						div++
					}
					valor++
				}
				
				se(div == 2)
				{
					escreva(n, "\n")
				}
				n--
				valor = 1
				div = 0
				
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 370; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */