import random
import jogos
def jogar():

    numero_secreto = random.randrange(1000, 10000)
    jogar_novamente = 1

    print("************ Bem vindo ************\n")
    print("*** Tutorial ***\n"
          "*** Tente adivinhar um número entre 1000 e 9999 ***\n"
          "*** A cada acerto, será liberado a dia do número acertado ***\n"
          "*** Boa sorte ***\n")

    while (jogar_novamente == 1):
        print(numero_secreto)
        tentativa = int(input("Digite sua tentativa: "))
        if(tentativa == numero_secreto):
            print("*** Incrível, você acertou o número secreto em apenas 1 tentativa! ***\n")
        else:
            numero_tentativas = 0
            while (tentativa != numero_secreto):
                numero_tentativas += 1
                contador = 0
                tentativa = str(tentativa)
                numero_secreto = str(numero_secreto)
                acertos = ['_'] * 4
                for i in range (0, 4):
                    if (tentativa[i] == numero_secreto[i]):
                        contador += 1
                        acertos[i] = tentativa[i]
                    else:
                        continue
                if(contador < 4 and contador != 0):
                    print(f"Você não acertou, mas você acertou {contador} digito(s)!\n"
                          "*** Esses são os números corretos na sua tentativa ***")
                    for j in acertos:
                        print(j, end=' ')
                    print("\n")
                    tentativa = int(input("Digite sua nova tentativa: "))
                elif(contador == 0):
                    print("*** Você não acertou nenhum dos números! ***")
                    tentativa = int(input("Digite sua nova tentativa: "))
                if (tentativa == numero_secreto):
                    print("*** Parabéns, você acertou! ***")
                    print(f"Você levou apenas {numero_tentativas} tentativas")

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