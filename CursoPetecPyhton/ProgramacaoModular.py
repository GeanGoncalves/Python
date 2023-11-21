def somar_pares_multiplicar_ímpares(numeros):
    soma = 0
    multiplicacao = 1
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
        else:
            multiplicacao *= numero
    
    return soma, multiplicacao


numeros = [i for i in range (1,6)]
soma, multiplicacao = somar_pares_multiplicar_ímpares(numeros)
print("Soma dos numeros pares:", soma)
print("Multiplicação dos números ímpares:", multiplicacao)