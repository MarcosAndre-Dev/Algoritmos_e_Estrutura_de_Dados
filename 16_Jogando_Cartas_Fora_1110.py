# =============================================================================
# Atividade 16 - Jogando Cartas Fora (beecrowd 1110)
# -----------------------------------------------------------------------------
# Ideia: a pilha de cartas funciona como uma FILA (deque): tiramos do início
# (topo) e colocamos no fim (base). Enquanto houver 2 ou mais cartas:
#  1) descarta a carta do início;
#  2) move a nova carta do início para o fim.
# A carta que sobrar é a "Remaining card".
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys
# Importa o deque, uma fila que remove do início de forma rápida
from collections import deque

# Lê toda a entrada e separa em números (em formato de texto)
dados = sys.stdin.read().split()
# Lista com as linhas de resposta
saida = []

# Percorre cada número lido
for valor in dados:
    # Converte o valor para inteiro
    n = int(valor)
    # O valor 0 indica o fim da entrada
    if n == 0:
        # Encerra o laço
        break
    # Cria a fila com as cartas de 1 (topo) até n (base)
    cartas = deque(range(1, n + 1))
    # Lista com as cartas descartadas, na ordem em que saem
    descartadas = []
    # Repete enquanto houver 2 ou mais cartas
    while len(cartas) >= 2:
        # Remove a carta do topo e guarda como descartada
        descartadas.append(cartas.popleft())
        # Remove a nova carta do topo e coloca na base da pilha
        cartas.append(cartas.popleft())
    # Começa a primeira linha de saída
    linha1 = 'Discarded cards:'
    # Se houve cartas descartadas (n = 1 não descarta nenhuma)
    if len(descartadas) > 0:
        # Acrescenta as cartas separadas por vírgula e espaço
        linha1 += ' ' + ', '.join(str(carta) for carta in descartadas)
    # Guarda a primeira linha
    saida.append(linha1)
    # Guarda a segunda linha com a carta que sobrou
    saida.append('Remaining card: ' + str(cartas[0]))

# Imprime todas as linhas
print('\n'.join(saida))
