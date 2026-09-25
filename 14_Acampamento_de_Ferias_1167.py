# =============================================================================
# Atividade 14 - Acampamento de Férias (beecrowd 1167)
# -----------------------------------------------------------------------------
# Ideia: guardar as crianças em uma lista na ordem de entrada (lista circular,
# usando o operador % para "dar a volta"). Na lista:
#  - sentido ANTI-HORÁRIO  = índice aumentando (+1)
#  - sentido HORÁRIO       = índice diminuindo (-1)
# Valor ÍMPAR conta no sentido anti-horário; valor PAR no sentido horário.
#
# 1ª contagem: parte da 1ª criança (índice 0) e anda K casas:
#    ímpar -> índice (0 + K) % n        par -> índice (0 - K) % n
# Contagens seguintes: começam na criança vizinha à que acabou de sair.
# Se a criança removida estava no índice r, na lista nova (já sem ela):
#    ímpar -> índice (r + K - 1) % n    par -> índice (r - K) % n
# O K usado em cada rodada é o valor da ficha da criança que acabou de sair.
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys

# Lê toda a entrada e separa em partes (números e nomes)
dados = sys.stdin.read().split()
# Posição atual de leitura dentro da lista de dados
pos = 0
# Lista com as respostas de cada caso de teste
saida = []

# Repete enquanto ainda houver dados para ler
while pos < len(dados):
    # Lê N, a quantidade de crianças no círculo
    n = int(dados[pos])
    # Avança a posição de leitura
    pos += 1
    # N igual a zero indica o fim da entrada
    if n == 0:
        # Encerra o laço
        break
    # Lista com os nomes das crianças, na ordem em que entraram no círculo
    nomes = []
    # Lista com os valores das fichas, na mesma ordem dos nomes
    valores = []
    # Lê as N crianças
    for _ in range(n):
        # Guarda o nome da criança
        nomes.append(dados[pos])
        # Guarda o valor da ficha convertido para inteiro
        valores.append(int(dados[pos + 1]))
        # Avança duas posições (nome e valor)
        pos += 2
    # A primeira contagem usa o valor da ficha da primeira criança
    k = valores[0]
    # Marca que ainda estamos na primeira contagem
    primeira = True
    # Guardará o índice da última criança removida
    removido = 0
    # Repete até sobrar apenas uma criança
    while len(nomes) > 1:
        # Quantidade atual de crianças no círculo
        tamanho = len(nomes)
        # Se for a primeira contagem (parte da criança do índice 0)
        if primeira:
            # Valor ímpar: anda K casas no sentido anti-horário (+)
            if k % 2 == 1:
                # Índice da criança onde a contagem termina
                indice = (0 + k) % tamanho
            # Valor par: anda K casas no sentido horário (-)
            else:
                # Índice da criança onde a contagem termina
                indice = (0 - k) % tamanho
            # As próximas contagens já não são a primeira
            primeira = False
        # Contagens seguintes (partem da vizinha da criança removida)
        else:
            # Valor ímpar: conta K no sentido anti-horário
            if k % 2 == 1:
                # A vizinha anti-horária já ocupa o índice "removido" (conta como 1)
                indice = (removido + k - 1) % tamanho
            # Valor par: conta K no sentido horário
            else:
                # A vizinha horária está em "removido - 1" (conta como 1)
                indice = (removido - k) % tamanho
        # O valor da ficha da criança que sai define a próxima contagem
        k = valores[indice]
        # Remove o nome da criança eliminada
        nomes.pop(indice)
        # Remove o valor da ficha da criança eliminada
        valores.pop(indice)
        # Guarda a posição de onde a criança foi removida
        removido = indice
    # A única criança que sobrou é a vencedora
    saida.append('Vencedor(a): ' + nomes[0])

# Imprime as respostas, uma por linha
print('\n'.join(saida))
