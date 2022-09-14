import forca;
import adivinhacao;

print('******************************************')
print('***** Bem vindo(a), escolha seu jogo *****')
print('******************************************')

print('(1) Forca (2) Adivinhação')
jogo = int(input('Qual jogo?'))

if (jogo == 1):
    print('Jogo forca')
elif (jogo == 2):
    print('Jogo adivinhação')