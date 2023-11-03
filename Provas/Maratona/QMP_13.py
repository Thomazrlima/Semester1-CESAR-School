print('Digite quantos pacientes serma cadastrados: ', end='')
num_paciente = int(input())

while num_paciente > 0:
    print('Digite o nome do paciente: ', end='')
    nome = input()
    print('Digite a idade do paciente: ', end='')
    idade = int(input())
    print('O paciente tem doença contagiosa?(S/N): ', end='')
    doenca_contagiosa = input()
    
    if idade >= 65:
        print('Atendimento de Prioridade!')
    else:
        print('Atendimento sem Prioridade!')
    
    if doenca_contagiosa.lower() ==  's' or doenca_contagiosa.lower() == 'sim':
        print('Paciente da sala Amarela!')
    else:
        print('Paciente da sala Branca')
    
    num_paciente -= 1

print('\n Atendimento Finalizado!')

