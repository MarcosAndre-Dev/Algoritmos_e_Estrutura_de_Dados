# =============================================================================
# Atividade 11 - Pares e Ímpares (beecrowd 1259)
# -----------------------------------------------------------------------------
# Ideia: separar os números em duas listas (pares e ímpares), ordenar os
# pares em ordem crescente e os ímpares em ordem decrescente, e imprimir
# primeiro os pares e depois os ímpares.
# =============================================================================

# Importa o módulo sys para leitura rápida (N pode ser até 100 mil)
import sys

# Lê toda a entrada de uma vez e separa em números (em formato de texto)
dados = sys.stdin.buffer.read().split()
# O primeiro valor é N, a quantidade de números
n = int(dados[0])
# Lista que vai guardar os números pares
pares = []
# Lista que vai guardar os números ímpares
impares = []

# Percorre os N números que vêm depois do N
for i in range(1, n + 1):
    # Converte o valor lido para inteiro
    valor = int(dados[i])
    # Se o resto da divisão por 2 é zero, o número é par
    if valor % 2 == 0:
        # Guarda na lista de pares
        pares.append(valor)
    # Caso contrário, o número é ímpar
    else:
        # Guarda na lista de ímpares
        impares.append(valor)

# Ordena os pares em ordem crescente
pares.sort()
# Ordena os ímpares em ordem decrescente (reverse=True inverte a ordem)
impares.sort(reverse=True)
# Junta as duas listas: primeiro os pares, depois os ímpares
resultado = pares + impares
# Converte cada número em texto e imprime um por linha
print('\n'.join(str(valor) for valor in resultado))
