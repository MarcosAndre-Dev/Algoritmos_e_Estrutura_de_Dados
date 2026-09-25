# =============================================================================
# Atividade 10 - Ordenação por Tamanho (beecrowd 1244)
# -----------------------------------------------------------------------------
# Ideia: separar as palavras de cada linha e ordená-las da MAIOR para a
# MENOR. A ordenação do Python (sort/sorted) é ESTÁVEL: palavras com o mesmo
# tamanho continuam na ordem original, exatamente como o enunciado pede.
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys


# Função que diz ao sort qual valor usar para comparar as palavras
def chave(palavra):
    # Tamanho negativo: assim a ordem crescente vira "maior tamanho primeiro"
    return -len(palavra)


# Lê todas as linhas da entrada e descarta as linhas vazias
linhas = [l for l in sys.stdin.read().split('\n') if l.strip() != '']
# A primeira linha contém N, a quantidade de casos de teste
n = int(linhas[0])

# Repete para cada caso de teste
for i in range(1, n + 1):
    # Separa a linha em palavras usando os espaços
    palavras = linhas[i].split()
    # Ordena as palavras pelo tamanho, do maior para o menor (ordenação estável)
    ordenadas = sorted(palavras, key=chave)
    # Junta as palavras com um espaço entre elas e imprime
    print(' '.join(ordenadas))
