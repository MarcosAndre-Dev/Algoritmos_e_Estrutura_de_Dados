# =============================================================================
# Atividade 21 - Dama (beecrowd 1087)
# -----------------------------------------------------------------------------
# Ideia: a dama anda qualquer distância em linha, coluna ou diagonal, então a
# resposta só pode ser 0, 1 ou 2:
#  - 0: a dama já está na casa de destino;
#  - 1: o destino está na mesma linha, mesma coluna ou mesma diagonal
#       (mesma diagonal = a diferença das linhas é igual à das colunas);
#  - 2: qualquer outro caso (sempre dá para chegar em 2 movimentos).
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys

# Lê toda a entrada e separa em números (em formato de texto)
dados = sys.stdin.read().split()
# Posição atual de leitura dentro da lista de dados
pos = 0
# Lista com as respostas de cada caso de teste
saida = []

# Repete enquanto houver pelo menos quatro números para ler
while pos + 3 < len(dados):
    # Linha de origem da dama
    x1 = int(dados[pos])
    # Coluna de origem da dama
    y1 = int(dados[pos + 1])
    # Linha de destino
    x2 = int(dados[pos + 2])
    # Coluna de destino
    y2 = int(dados[pos + 3])
    # Avança quatro posições
    pos += 4
    # Quatro zeros indicam o fim da entrada
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        # Encerra o laço
        break
    # Se a origem e o destino são a mesma casa
    if x1 == x2 and y1 == y2:
        # Não precisa de nenhum movimento
        saida.append('0')
    # Mesma linha, mesma coluna ou mesma diagonal (|dx| == |dy|)
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        # Chega com um único movimento
        saida.append('1')
    # Qualquer outra posição
    else:
        # Sempre é possível chegar com dois movimentos
        saida.append('2')

# Imprime as respostas, uma por linha
print('\n'.join(saida))