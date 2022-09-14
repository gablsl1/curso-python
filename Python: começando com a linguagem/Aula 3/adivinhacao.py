print('Bem vindo ao jogo de adivinhação!');

numero_secreto = 78;

# A função int converte uma str para int
chute = int(input('Digite o teu número: '));

if(numero_secreto == chute):
    print('Tu acertou! =)');
else:
    print('Tu errou =(');
