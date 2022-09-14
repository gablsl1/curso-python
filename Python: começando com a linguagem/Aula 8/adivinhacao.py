print('Bem vindo ao jogo de adivinhação!');

total_de_tentativas = 3;

for rodada in range(1, total_de_tentativas + 1):
    #String interpolation / Intrapolação de string
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas));
    
    numero_secreto = 78;

    chute = int(input('Digite um número entre 1 e 100: '));
    
    if(chute < 1 or chute > 100 ):
        print('Tu deve digitar um número entre 1 e 100')
        continue 

    acertou = numero_secreto == chute
    numero_maior = chute > numero_secreto;
    numero_menor = chute < numero_secreto;

    if(acertou):
        print('Tu acertou!');
        break;
    else:
        if (numero_maior):
            print('Tu errou, teu chute foi maior que o número secreto');
        elif(numero_menor):
            print('Tu errou, teu chute foi menor que o número secreto');
        
    print('Fim do jogo');