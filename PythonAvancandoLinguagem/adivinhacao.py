import random

def jogar():

    ##Variaveis
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000


    print("\n\nBem vindo no jogo de Adivinhação!")


    ##Nível de dificuldade
    print("Qual nível de dificuldade?")
    print("(1) Fácil \n(2) Médio \n(3) Difícil")
    nivel = int(input("Difine o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        print("Você digitou um numero diferente das opções!\n")
        
    ##Laço
    for rodada in range (1,total_de_tentativas +1):
        print("\nTentativa {} de {}" .format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute)
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar digitar um número entre 1 e 100!")
            continue 


        ##Condições
        acertou = chute == numero_secreto 
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        
        
        if (acertou):
            print("Você acertou e fez {} pontos!\n" .format(pontos))
            break
        else: 
            if(maior):
                print("Você errou! Seu chute foi maior do que o número secreto")
            elif(menor):
                print("Você errou! Seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        
    print("Fim de jogo\n")
    
if(__name__ == "__main__"):
    jogar()