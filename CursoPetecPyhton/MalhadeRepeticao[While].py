import random

numero_aleatorio = random.randint(1,5)
escolha = 0

while escolha != numero_aleatorio:
    escolha = int(input("Escolha um número até 5: "))
    if escolha == numero_aleatorio:
        print("Parabéns!")
    elif abs(escolha - numero_aleatorio) == 1:
        print("Quase :/")
    else:
        print("Errou :(")