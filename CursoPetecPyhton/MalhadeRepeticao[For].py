n = int (input("Digite um número: "))
soma_quad = 0

for i in range(1,n+1):
    soma_quad += i**2

print(f"A soma dos Quadrados de 1 á {n} é igual a {soma_quad}")