programa {
    inclua biblioteca Matematica --> mat
	funcao inicio() {
	    inteiro idade, contm = 0, contf = 0, velha = 0, cont = 1
	    caracter sexo
	    real media, soma = 0.0
	    
	    faca{
            escreva("Bem vindo ao progama online do IBGE \n")
	        escreva("Digite o seu sexo (M/F) ")
	        leia(sexo)
	        escreva("Digite a sua idade " )
	        leia(idade)
	        soma += idade
	        cont++
	    
	        se(sexo == 'f' ou sexo == 'F'){
	            se(velha < idade){
	            velha = idade
	            }
	            se(idade > 20){
	            contf++
	            }
	        }
	
	        senao{
	            contm++
	}
        }enquanto(cont <= 5)
        media = mat.arredondar(soma/5, 2)
        escreva("A média das idades da sua rua é ", media)
        escreva("\nAdemais, ", contm, " Homens responderam essa pesquisa")
        escreva("\nA mulher mais velha da rua tem ", velha," anos")
        escreva("\ne ", contf, " mulhere(s) tem maais de 20 anos")
}
}
