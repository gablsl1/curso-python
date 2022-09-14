import random
import secrets;

print('Bem vindo ao jogo de adivinhação!');

numero_secreto = random.random.randrange(1,11);
total_de_tentativas = 0;
pontos = 1000

print('Qual nível de dificuldade?');
print('(1) Facíl (2) Médio (3) Dificil');
nivel = int(input('Defina um nível: '));

if (nivel == 1):
    total_de_tentativas = 20;
elif (nivel == 2):
    total_de_tentativas = 10;
else:
    total_de_tentativas = 5;

for rodada in range(1, total_de_tentativas + 1):
    #String interpolation / Intrapolação de string
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas));
    
    numero_secreto = 78;

    chute = int(input('Digite um número entre 1 e 10: '));
    
    if(chute < 1 or chute > 10 ):
        print('Tu deve digitar um número entre 1 e 10')
        continue 

    acertou = numero_secreto == chute
    numero_maior = chute > numero_secreto;
    numero_menor = chute < numero_secreto;

    if(acertou):
        print('Tu acertou e fez {} pontos!'.format(pontos));
        break;
    else:
        if (numero_maior):
            print('Tu errou, teu chute foi maior que o número secreto');
        elif(numero_menor):
            print('Tu errou, teu chute foi menor que o número secreto');
            pontos_perdidos = abs(numero_secreto - chute);
            pontos -= pontos_perdidos;
        
    print('Fim do jogo');