
import random


def game():

    wellcome()

    palavra_secreta = secret_word()

    letra_certa = ["_" for letras in palavra_secreta]  #PARA CADA "LETRA" DENTRO DA "PALAVRA SECRETA" O 'FOR' ADICIONA UM "_"
    print(letra_certa)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = input_chute()

        if (chute in palavra_secreta):                      #IF CRIADO PARA CONTAGEM DOS ERROS E DESENHAR A FORCA
            verificando_chute(palavra_secreta, letra_certa, chute)
        else:
            erros += 1
            desenho_forca(erros)

        enforcou = erros == 7 
        acertou = "_" not in letra_certa                    #VENCE O JOGO QUANDO '_' NÃO ESTIVER MAIS PRESENTE DENTO DA VÁRIAVEL 'LETRA_CERTA'

        print(letra_certa)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def wellcome():
    print("")
    print("###########################")
    print("Bem vindo ao jogo da Forca!")
    print("###########################")
    print("")

def secret_word():                                          #CRIA A LISTA DE PALAVRAS A PARTIR DO ARQUIVO DE TEXTO "FRUTAS"
    arquivo = open ("frutas.txt", "r")
    palavras = []                                           #INICIA UMA LISTA VAZIA

    for linha in arquivo:
        linha = linha.strip()                               #Retorna uma cópia da string com os caracteres iniciais e finais removidos
        palavras.append(linha)                              #ADICIONA CADA LINHA DO ARQUIVO "FRUTAS" NA LISTA PALAVRAS
    arquivo.close()

    numero = random.randrange(0, len(palavras))             #EXTRAI UM NUMERO ALEATÓRIO TENDO COMO BASE A QUANTIDADE DE LINHAS DENTRO DA LISTA "PALAVRAS"
    palavra_secreta = palavras[numero].upper()              #UTILIZA O NÚMERO ALEATÓRIO PARA BUSCAR A PALAVRA CORRESPONDENTE A TAL NÚMERO DENTRO DO ÍNDICE DE PALAVRAS. CAPTALIZA A PALARA ".UPPER"
    return palavra_secreta                                  #RETRONA PARA A FUNÇÃO A PALAVRA SORTEADA

def input_chute():
    chute = input ("Digite uma letra: ")
    chute = chute.strip().upper()                           #STRIP PARA REMOVER QUALQUER OUTRO CARACTER QUE NÃO SEJA A LETRA E UPPER PARA QUE FIQUE MAIÚSCULA.
    return chute

def verificando_chute(palavra_secreta, letra_certa, chute):
    position = 0                                            #EM CADA ITERAÇÃO É VERIFICADO UMA POSIÇÃO, UMA LETRA DENTRO DA LISTA 'LETRA_CERTA'
    for letra in palavra_secreta:                           #PARA CADA 'LETRA' DENTRO DA 'PALAVRA_SECRETA'
        if (chute == letra):                                #SE O 'CHUTE' FOR IGUAL A UMA 'LETRA'
            letra_certa[position] = letra
        position += 1                                       #TEM A MESMA FUNÇÃO DE "POSITON = POSITION + 1"

def desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("")
    print("Parabéns, você ganhou!")
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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


if __name__ == "__main__":
    game()