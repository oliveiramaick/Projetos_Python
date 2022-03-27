import forca
import adivinhacao

def game():
    wellcome()

    jogo = int(input("Escolha o jogo: "))

    if jogo == 1:
        forca.game()
    elif jogo == 2:
        adivinhacao.play_game()

def wellcome():
    print("")
    print ("####################")
    print ("##Escolha seu Jogo##")
    print ("####################")
    print("")
    print("[1] Jogo da Forca")
    print("")
    print("[2] Jogo de Adivinhação")
    print("")

if(__name__ == "__main__"):
    game()
