import forca
import adivinhacao

print("\nMenu jogos!")

print("\n(1) Forca\n(2) Adivinhação")
jogo = int(input("\nQual jogo você quer jogar? "))

if (jogo == 1):
    forca.jogar()
    
elif(jogo == 2):
    adivinhacao.jogar()