
import random
import sys

my_dict = {"upper_left": "", "upper_middle": "", "upper_right": "" , "middle_left": "", "middle_middle": "", "middle_right": "", "bottom_left": "", "bottom_middle": "", "bottom_right": ""}

def exibir_tabuleiro ():
    print(my_dict["upper_left"] + "|", my_dict["upper_middle"] + "|", my_dict["upper_right"] + "|",)

    print(my_dict["middle_left"] + "|", my_dict["middle_middle"] + "|", my_dict["middle_right"] + "|",)

    print(my_dict["bottom_left"] + "|", my_dict["bottom_middle"] + "|", my_dict["bottom_right"] + "|",)

print("Vamos começar a jogar Jogo da Velha")

vez_do_jogador = random.randint(0,1) #jogador 0 é "O" e jogador 1 é "X"
simbolo_do_jogador = ["O", "X"]

def mudanca_vez_jogador ():
    global vez_do_jogador
    if vez_do_jogador == 0:
        vez_do_jogador = 1
    else:
        vez_do_jogador = 0

while True: #ao longo de todo jogo, enquanto ele não terminar
    try:
        print("É a vez do jogador", simbolo_do_jogador[vez_do_jogador])
        exibir_tabuleiro()

        posicao = input("Onde você quer adicionar o seu símbolo? ")
        
        while True:
            tabuleiro = my_dict.get(posicao)
            if tabuleiro == "":
                break
            if tabuleiro is None:
                posicao = input ("Essa posição não existe. Digite novamente onde deseja adicionar seu símbolo ")
            elif len(tabuleiro) > 0:
                posicao = input ("Essa posição já está ocupada. Digite novamente onde deseja adicionar seu símbolo ")

        my_dict[posicao] = simbolo_do_jogador[vez_do_jogador]

        combinacoes = [
            ['upper_left', 'upper_middle', 'upper_right'],
            ['middle_left', 'middle_middle', 'middle_right'],
            ['bottom_left', 'bottom_middle', 'bottom_right'],
            ['upper_left', 'middle_middle', 'bottom_right'],
            ['upper_right', 'middle_middle', 'bottom_left'],
            ['upper_left', 'middle_left', 'bottom_left'],
            ['upper_middle', 'middle_middle', 'bottom_middle'],
            ['upper_right', 'middle_right', 'bottom_right']
        ]
        posicao_jogador = []
        for k,v in my_dict.items():
            if v == simbolo_do_jogador[vez_do_jogador]:
                posicao_jogador.append (k)

        for combinacao in combinacoes:
            count = 0
            for posicao in posicao_jogador:
                if posicao in combinacao:
                    count += 1
                else:
                    break
            if count == 3:
                exibir_tabuleiro()
                print ("Voce é vencedor")
                sys.exit()
        
        mudanca_vez_jogador()

    except KeyboardInterrupt:
        break
