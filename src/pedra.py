import random
import jogos
def jogar():

    print("************ Bem vindo ************\n")

    jogar_novamente = 1
    seus_pontos = 0
    pontos_adversario = 0

    rodada = 1

    print("*** Tutorial ***\n"
          "*** Pedra, Papel e Tesoura ***\n"
          "*** Pedra quebra tesoura. Papel enrola pedra. Tesoura corta papel ***")


    while (jogar_novamente == 1):
        objeto_adversario = random.randrange(1, 4)
        print("\n*** Escolha a sua opção: ***\n"
              "*** 1 - Pedra ***\n"
              "*** 2 - Papel ***\n"
              "*** 3 - Tesoura ***\n")
        objeto_jogador = int(input("Digite o objeto escolhido: "))

        if (objeto_jogador == 1):
            print("*** Você escolheu pedra ***")
        elif (objeto_jogador == 2):
            print("*** Você escolheu papel ***")
        elif (objeto_jogador == 3):
            print("*** Você escolheu tesoura ***")
        else:
            while (objeto_jogador < 1 or objeto_jogador > 3):
                print("*** Opção inválida tente novamente! ***\n")
                objeto_jogador = int(input("Digite o objeto escolhido novamente: "))

        if (objeto_adversario == 1):
            print("*** Computador escolheu pedra ***\n")
        elif (objeto_adversario == 2):
            print("*** Computador escolheu papel ***\n")
        else:
            print("*** Computador escolheu tesoura ***\n")

        if (objeto_jogador == 1 and objeto_adversario == 3 or objeto_jogador == 2 and objeto_adversario == 1 or objeto_jogador == 3 and objeto_adversario == 2):
            print("*** Você venceu ***\n")
            seus_pontos += 1
            print("*** Placar: seus pontos {} X {} pontos computador ***".format(seus_pontos, pontos_adversario))
        elif(objeto_jogador == objeto_adversario):
            print("*** Empate ***\n")
            print("*** Placar: seus pontos {} X {} pontos computador ***".format(seus_pontos, pontos_adversario))
        else:
            print("*** Você perdeu ***\n")
            pontos_adversario += 1
            print("*** Placar: seus pontos {} X {} pontos computador ***".format(seus_pontos, pontos_adversario))

        jogar_novamente = int(input("Deseja jogar novamente?\n"
                                    "(1)-Sim (2)-Voltar para o menu principal (3)-Encerrar\n"
                                    "Digite sua opção: "))

        if (jogar_novamente < 1 or jogar_novamente > 3):
            jogar_novamente = int(input("Opção inválida, digite novamente: "))
        elif (jogar_novamente == 2):
            jogos.jogos()
        elif (jogar_novamente == 3):
            print("\n*** Fim de jogo! ***")


if (__name__ == "__main__"):
    jogar()