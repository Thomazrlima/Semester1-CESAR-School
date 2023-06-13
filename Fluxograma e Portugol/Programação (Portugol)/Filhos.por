programa {
	funcao inicio() {
		inteiro cont = 1, soma = 0, soma1 = 0, filhos
		
		enquanto(cont <= 10){
		    escreva("Quantos filhos você tem? ")
		    leia(filhos)
		    cont++
		    se(filhos <= 2){
		    soma++}
		    senao{
		    soma1++}
		}
		 escreva(soma, " mulheres tem até 2 filhos e ", soma1, " mulheres tem mais de 2 filhos")
	}
}
