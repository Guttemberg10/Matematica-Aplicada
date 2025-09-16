# Algoritmo que monta o triângulo de Pascal
# Autor: Gabriel Novais
# Data: 16/09/2025

def combinacaoSimples(n, p):
    fatorial_n = 1
    fatorial_p = 1
    fatorial_np = 1

    multiplicar = n
    # Laço que calcula o fatorial de N:
    while(multiplicar != 0):
        fatorial_n = fatorial_n * multiplicar
        multiplicar -=1
    
    multiplicar = p
    # Laço que calcula o fatorial de P:
    while(multiplicar != 0):
        fatorial_p = fatorial_p * multiplicar
        multiplicar -=1

    multiplicar = n-p
    # Laço que calcula o fatorial de N-P:
    while(multiplicar != 0):
        fatorial_np = fatorial_np * multiplicar
        multiplicar -=1

    combinacao = (fatorial_n) / (fatorial_p * fatorial_np)
    return int(combinacao)


j = 0# Variável que controla o p
quantidadeDeLinhas = int(input("Digite a quantidade de linhas que deseja ver: "))

for contador_linhas in range(quantidadeDeLinhas):
    for p in range(j+1):
        print(combinacaoSimples(contador_linhas, p), end="  ")
    
    j+=1
    print("\n", end="")