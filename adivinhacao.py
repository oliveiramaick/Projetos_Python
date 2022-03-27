import random


def play_game():
    wellcome()

    tentativas_totais = level()

    num_aleatorio = random.randint(1, 101)
    pontos = 1000
    # print (num_aleatorio) #ESTÁ AQUI PARA TESTE DO CÓDIGO

    for rodada in range(1, (tentativas_totais + 1)):
        print("")
        print("### Tentativa {} de {}.".format(rodada, tentativas_totais))
        chute = int(input(">>> Digite um valor entre 1 e 100: "))
        pontos = pontos - chute
        acertou = chute == num_aleatorio

        if chute < 1 or chute > 100:
            print("Número fora do intervalo aceito.")
            continue

        if rodada == tentativas_totais:
            pontos_perdidos = 1000 - pontos
            print_lose(num_aleatorio, pontos_perdidos)

        if acertou:
            print_win(pontos)
            break
        elif chute > num_aleatorio:
            print("")
            print("Chutou alto.")
        elif chute < num_aleatorio:
            print("")
            print("Chutou baixo.")


def wellcome():
    print("")
    print("####################")
    print("Jogo de Adivinhação.")
    print("####################")
    print("")


def level():
    tentativas_totais = 0
    nivel = int(input("Escolha um nível: [1] - Fácil    [2] - Médio   [3] - Díficil     >  "))
    if nivel == 1:
        tentativas_totais = 15
    elif nivel == 2:
        tentativas_totais = 10
    elif nivel == 3:
        tentativas_totais = 5
    else:
        print("Nível incorreto")
    return tentativas_totais


def print_win(pontos):
    print("                           ")
    print("Parabéns \o/  Você venceu!!!")
    print("Você fez {} pontos.".format(pontos))
    print("                        ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("            ")
    print("Fim do Jogo!")


def print_lose(num_aleatorio, pontos_perdidos):
    print("                           ")
    print("Puxa, você perdeu!")
    print("O número era {} e você fez {} pontos".format(num_aleatorio, pontos_perdidos))
    print("                            ")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("            ")
    print("Fim do Jogo!")


if __name__ == "__main__":
    play_game()
