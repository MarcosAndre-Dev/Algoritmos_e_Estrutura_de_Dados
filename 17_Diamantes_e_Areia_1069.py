# =============================================================================
# Atividade 17 - Diamantes e Areia (beecrowd 1069)
# -----------------------------------------------------------------------------
# Ideia: funciona como uma pilha de '<' abertos. Como só importa a QUANTIDADE,
# basta um contador:
#  - '<' : soma 1 nos "abertos";
#  - '>' : se houver algum '<' aberto, forma um diamante (diamantes + 1 e
#          abertos - 1);
#  - '.' : areia, é ignorada.
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys

# Lê toda a entrada e separa em linhas
linhas = sys.stdin.read().split('\n')
# A primeira linha contém N, a quantidade de casos de teste
n = int(linhas[0])

# Repete para cada caso de teste
for i in range(1, n + 1):
    # Pega a linha do caso; se o arquivo terminou antes, usa uma linha vazia
    mina = linhas[i] if i < len(linhas) else ''
    # Quantidade de '<' que ainda esperam um '>'
    abertos = 0
    # Quantidade de diamantes extraídos
    diamantes = 0
    # Percorre cada caractere da linha
    for c in mina:
        # Se for o início de um diamante
        if c == '<':
            # Guarda mais um '<' esperando fechamento
            abertos += 1
        # Se for o fim de um diamante e existe um '<' esperando
        elif c == '>' and abertos > 0:
            # O '<' foi usado para formar um diamante
            abertos -= 1
            # Soma um diamante extraído
            diamantes += 1
    # Imprime a quantidade de diamantes deste caso
    print(diamantes)
