# Algoritmo que transforma um número na base decimal para a base binária (com o uso de Pilha)
# Autor: Gabriel Novais
# Data: 17/09/2025

from collections import deque

decimal = int(input())
pilhaBinaria = deque()

print("Decimal:",decimal)

if(decimal == 0):# Não é feito a divisão por 0
    pilhaBinaria.append(0)

while int(decimal):
    pilhaBinaria.append(decimal % 2)# Adicionando o resto da divisão
    decimal = int(decimal / 2)# Dividindo o valor

while(len(pilhaBinaria) < 8):
    pilhaBinaria.append(0)

print("Binário: ", end="")

while pilhaBinaria:# Retirando os elementos da pilha e imprimindo do topo a base
    print(pilhaBinaria.pop(), end="")
