import random

def jogar():
    
    palavra_secreta = escolha_palavra()
    
    letras_acertadas = incializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0
    
    
    print("\n\nBem vindo no jogo da Forca!\n")
    print("Dica!!")
    
    
    ##Laço
    while(not enforcou and not acertou):
        
        chute = pede_chute()
        
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
           
            
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print("\n")
        print(letras_acertadas)
        
    if(acertou):
        print("\nVocê Ganhou!! :) ")
    else:
        (print("\nVocê Perdeu :("))
    print("Fim de jogo\n")
   
def marca_chute_correto():
    index = 0 
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1   
    
def pede_chute():
    chute = input("\nQual letra você deseja chutar? ")
    chute = chute.strip().upper()
    return chute 
    
def escolha_palavra():
    arquivo = open ("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
        
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def incializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()