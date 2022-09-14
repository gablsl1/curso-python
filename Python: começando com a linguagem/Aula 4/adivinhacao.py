print('Bem vindo ao jogo de adivinhação!');

numero_secreto = 78;

chute = int(input('Digite o teu número: '));

acertou = numero_secreto == chute
numero_maior = chute > numero_secreto;
numero_menor = chute < numero_secreto;

if(acertou):
    print('Tu acertou!');
else:
    if (numero_maior):
        print('Tu errou, teu chute foi maior que o número secreto');
    elif(numero_menor):
        print('Tu errou, teu chute foi menor que o número secreto');
    
print('Fim do jogo');