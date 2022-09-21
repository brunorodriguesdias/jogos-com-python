import random
import jogos

print("************ Bem vindo ************\n")
numero_secreto = random.randrange(1000, 10000)
quantidade_tentativas = 0
rodada = 1

print("*** Tutorial ***\n"
      "*** Tente adivinhar um número entre 1000 e 9999 ***\n"
      "*** A cada acerto, será liberado a dia do número acertado ***\n"
      "*** Boa sorte ***\n")

print("*** Selecione o nível desejado ***\n"
      "*** (1) - Fácil (12 tentativas) ***\n"
      "*** (2) - Médio (09 tentativas) ***\n"
      "*** (3) - Difícil (06 tentativas) ***\n")
nivel = int(input("Digite o nível desejado: "))

if (nivel == 1):
    quantidade_tentativas = 12
elif (nivel == 2):
    quantidade_tentativas = 9
elif (nivel == 3):
    quantidade_tentativas = 6
else:
    if (nivel < 1 or nivel > 3):
        print("*** Opção inválida tente novamente! ***\n")
        nivel = int(input("Digite o nível escolhido novamente: "))
print(numero_secreto)
print("Tentativa {} de {}".format(rodada, quantidade_tentativas))
tentativa = int(input("\nDigite sua tentativa: "))

while (tentativa < 1000 or tentativa >= 10000):
    print("*** Número invalido, escolha um número entre 1000 e 9999! ***\n")
    tentativa = int(input("Digite a tentativa novamente: "))

if (tentativa == numero_secreto):
    print("\n*** Parabéns, você acertou o número secreto! ***")
else:
    if(tentativa != numero_secreto):
        tentativa = str(tentativa)
        numero_secreto = str(numero_secreto)
