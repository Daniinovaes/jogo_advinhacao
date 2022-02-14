"""
This is going to be a simple guessing game where the computer will generate a random number between 1 to 13,
and the user has to guess it in 5 attempts.

Based on the user’s guess computer will give various hints if the number is high or low.
When the user guess matches the number computer will print the answer along with the number of attempts.
"""
import random

numero_1 = int(random.randrange(1, 13, 1))
numero_2 = int(random.randrange(1, 13, 1))
player_1 = input('Oi, qual o nome do jogador 1?\n')
player_2 = input('Oi, qual o nome do jogador 2?\n')
rodada_1= rodada_2 = 0

print('\n' + player_1 + ' vs ' + player_2 + '\n')
print(player_1+' estou escolhendo um número entre 1 e 13, tente acertar qual número é:')

while rodada_1 < 5:
    rodada_1 += 1
    palpite_1 = int(input(player_1 + ' qual o seu palpite?\n'))
    if palpite_1 < numero_1:
        print(player_1 + ' seu palpite é muito baixo!')
    elif palpite_1 > numero_1:
        print(player_1 + ' seu palpite é muito alto!')
    elif palpite_1 == numero_1:
        break

if palpite_1 == numero_1:
    print(player_1 + ' advinhou! Você acertou na Rodada ' + str(rodada_1) + '!')
else:
    print(player_1 + ' você não acertou o número ' + str(numero_1))

print('\n\n'+player_2+', agora é a sua vez. Estou escolhendo outro número entre 1 e 13, tente acertar:')

while rodada_2 < 5:
    rodada_2 += 1
    palpite_2 = int(input(player_2 + ' qual o seu palpite?\n'))
    if palpite_2 < numero_2:
        print(player_2 + ' seu palpite é muito baixo!')
    if palpite_2 > numero_2:
        print(player_2 + ' seu palpite é muito alto!')
    if palpite_2 == numero_2:
        break

if palpite_2 == numero_2:
    print(player_2 + ' advinhou! Você acertou na Rodada ' + str(rodada_2) + '!')
else:
    print(player_2 + ' você não acertou o número ' + str(numero_2))

if rodada_1 > rodada_2:
    print('\n' + player_2 + ' ganhou adivinhando em menos rodadas.\nO resultado foi: '+ player_2 + ' com '
          + str(rodada_2) + ' rodadas vs ' + player_1 + ' com ' + str(rodada_1) + ' rodadas.')
elif rodada_1 < rodada_2:
    print('\n' + player_1 + ' ganhou adivinhando em menos rodadas.\nO resultado foi: ' + player_1 + ' com '
          + str(rodada_1) + ' rodadas vs ' + player_2 + ' com ' + str(rodada_2) + ' rodadas.')
else:
    print('\n' + 'É um empate!\nO resultado foi: ' + player_1 + ' com '
          + str(rodada_1) + ' rodadas vs ' + player_2 + ' com ' + str(rodada_2) + ' rodadas.')