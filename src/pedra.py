import random

print("************ Bem vindo ************")
objeto_adversario = random.randrange(1, 4)
rodada = 1

print("*** Tutorial ***\n"
    "*** Pedra, Papel e Tesoura ***\n"
    "*** Pedra quebra tesoura. Papel enrola pedra. Tesoura corta papel ***\n")

print("*** Escolha a sua opção: ***\n"
          "*** 1 - Pedra ***\n"
          "*** 2 - Papel ***\n"
          "*** 3 - Tesoura ***\n")
objeto_jogador = int(input("Digite o objeto escolhido: "))

if (objeto_jogador == 1):
        print("*** Você escolheu pedra ***")
elif(objeto_jogador == 2):
        print("*** Você escolhei papel ***")
elif(objeto_jogador == 3):
        print("*** Você escolhei pedra ***")
else:
        print("*** Número inválido tente novamente! ***")