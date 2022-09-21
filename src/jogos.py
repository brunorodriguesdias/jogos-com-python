import pedra
import mastemind
def jogos():

    print("\n************ Bem vindo ************\n"
          "*** Escolha o jogo que deseja jogar  ***\n"
          "(1)-Pedra, papel ou tesoura  (2)-Mastermind\n")

    jogo_escolhido = int(input("Digite a opção desejada: "))

    if (jogo_escolhido == 1):
        pedra.jogar()
    elif (jogo_escolhido == 2):
        mastemind.jogar()

if (__name__ == "__main__"):
    jogos()
