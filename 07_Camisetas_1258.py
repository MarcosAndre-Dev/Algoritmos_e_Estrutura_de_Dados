# =============================================================================
# Atividade 07 - Camisetas (beecrowd 1258)
# -----------------------------------------------------------------------------
# Ideia: guardar cada camiseta como (cor, tamanho, nome) e ordenar por:
#  1) cor em ordem crescente (branco antes de vermelho);
#  2) tamanho em ordem descendente (P, depois M, depois G);
#  3) nome em ordem crescente.
# A ordenação usa uma "chave" que devolve esses três critérios em sequência.
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys

# Posição de cada tamanho na ordem pedida (P vem primeiro, G por último)
ORDEM_TAMANHO = {'P': 0, 'M': 1, 'G': 2}


# Função que diz ao sort como comparar duas camisetas
def chave(camiseta):
    # Desmonta a tupla em cor, tamanho e nome
    cor, tamanho, nome = camiseta
    # Retorna os critérios na ordem de prioridade: cor, tamanho, nome
    return (cor, ORDEM_TAMANHO[tamanho], nome)


# Lê todas as linhas, remove espaços das pontas e descarta linhas vazias
linhas = [l.strip() for l in sys.stdin.read().split('\n') if l.strip() != '']
# Posição atual de leitura dentro da lista de linhas
pos = 0
# Lista que guarda o texto de saída de cada caso de teste
blocos = []

# Repete enquanto ainda houver linhas para ler
while pos < len(linhas):
    # Lê N, a quantidade de camisetas da turma
    n = int(linhas[pos])
    # Avança para a próxima linha
    pos += 1
    # N igual a zero indica o fim da entrada
    if n == 0:
        # Encerra o laço
        break
    # Lista com as camisetas desta turma
    camisetas = []
    # Lê as N camisetas (duas linhas para cada uma)
    for _ in range(n):
        # Primeira linha: nome do estudante
        nome = linhas[pos]
        # Segunda linha: cor e tamanho, separados por espaço
        cor, tamanho = linhas[pos + 1].split()
        # Avança duas linhas
        pos += 2
        # Guarda a camiseta como uma tupla (cor, tamanho, nome)
        camisetas.append((cor, tamanho, nome))
    # Ordena as camisetas usando a função chave definida acima
    camisetas.sort(key=chave)
    # Lista com as linhas de saída deste caso
    linhas_saida = []
    # Percorre as camisetas já ordenadas
    for cor, tamanho, nome in camisetas:
        # Monta a linha no formato "cor tamanho nome"
        linhas_saida.append(cor + ' ' + tamanho + ' ' + nome)
    # Junta as linhas deste caso e guarda como um bloco
    blocos.append('\n'.join(linhas_saida))

# Imprime os blocos separados por uma linha em branco
print('\n\n'.join(blocos))
