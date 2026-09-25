# =============================================================================
# Atividade 13 - Organizador de Vagões (beecrowd 1162)
# -----------------------------------------------------------------------------
# Ideia: a ponte só troca dois vagões VIZINHOS de lugar, exatamente como o
# Bubble Sort. O número mínimo de trocas é o número de "inversões": pares
# (i, j) com i < j em que o vagão da posição i é maior que o da posição j.
# Como L <= 50, basta comparar todos os pares (dois laços).
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys

# Lê toda a entrada e separa em números (em formato de texto)
dados = sys.stdin.read().split()
# O primeiro valor é N, a quantidade de casos de teste
n = int(dados[0])
# Posição atual de leitura (logo após o N)
pos = 1

# Repete para cada caso de teste
for _ in range(n):
    # Lê L, a quantidade de vagões do trem
    l = int(dados[pos])
    # Avança a posição de leitura
    pos += 1
    # Lê os L vagões e converte cada um para inteiro
    vagoes = [int(x) for x in dados[pos:pos + l]]
    # Avança a posição de leitura em L
    pos += l
    # Contador de trocas necessárias
    trocas = 0
    # Percorre cada posição i do trem
    for i in range(l):
        # Percorre cada posição j que está depois de i
        for j in range(i + 1, l):
            # Se o vagão da frente é maior, esse par está fora de ordem
            if vagoes[i] > vagoes[j]:
                # Cada par fora de ordem exige exatamente uma troca
                trocas += 1
    # Imprime a frase pedida com o número de trocas
    print('Optimal train swapping takes ' + str(trocas) + ' swaps.')
