# =============================================================================
# Atividade 19 - Onde está o Mármore? (beecrowd 1025)
# -----------------------------------------------------------------------------
# Ideia: ordenar os mármores em ordem crescente e, para cada consulta, usar
# BUSCA BINÁRIA (bisect_left) para achar a PRIMEIRA posição onde o número
# aparece. Se naquela posição estiver o número procurado, ele foi encontrado
# (a posição é mostrada começando em 1); senão, não foi encontrado.
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys
# Importa a busca binária que devolve a primeira posição possível do valor
from bisect import bisect_left

# Lê toda a entrada e separa em números (em formato de texto)
dados = sys.stdin.read().split()
# Posição atual de leitura dentro da lista de dados
pos = 0
# Número do caso de teste atual
caso = 0
# Lista com as linhas de resposta
saida = []

# Repete enquanto houver pelo menos dois números (N e Q) para ler
while pos + 1 < len(dados):
    # N = quantidade de mármores
    n = int(dados[pos])
    # Q = quantidade de consultas
    q = int(dados[pos + 1])
    # Avança duas posições
    pos += 2
    # "0 0" indica o fim da entrada
    if n == 0 and q == 0:
        # Encerra o laço
        break
    # Passa para o próximo número de caso
    caso += 1
    # Lê os N mármores e converte cada um para inteiro
    marmores = [int(x) for x in dados[pos:pos + n]]
    # Avança a posição de leitura em N
    pos += n
    # Ordena os mármores em ordem crescente
    marmores.sort()
    # Imprime o cabeçalho do caso
    saida.append('CASE# ' + str(caso) + ':')
    # Responde cada uma das Q consultas
    for _ in range(q):
        # Lê o número consultado
        x = int(dados[pos])
        # Avança para a próxima consulta
        pos += 1
        # Busca binária: primeira posição onde x está (ou deveria estar)
        indice = bisect_left(marmores, x)
        # Se a posição é válida e contém exatamente x, ele foi encontrado
        if indice < n and marmores[indice] == x:
            # Mostra a posição começando em 1 (por isso o + 1)
            saida.append(str(x) + ' found at ' + str(indice + 1))
        # Caso contrário, x não está em nenhum mármore
        else:
            # Mostra que não encontrou
            saida.append(str(x) + ' not found')

# Imprime todas as linhas de resposta
print('\n'.join(saida))
