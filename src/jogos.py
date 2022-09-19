import pedra
def jogos():

    print("\n************ Bem vindo ************\n"
          "*** Escolha o jogo que deseja jogar  ***\n"
          "(1)-Pedra, papel ou tesoura  (2)-Mastermind\n")

    jogo_escolhido = int(input("Digite a opção desejada: "))

    if (jogo_escolhido == 1):
        pedra.jogar()

if (__name__ == "__main__"):
    jogos()
