# =============================================================================
# Atividade 08 - Tabelas Hash (beecrowd 1256)
# -----------------------------------------------------------------------------
# Ideia: criar uma tabela com M posições, onde cada posição é uma lista
# (encadeamento exterior). Cada chave vai para a posição h(x) = x mod M e é
# colocada no FINAL da lista dessa posição. Depois imprimimos cada posição no
# formato "i -> chave -> chave -> \".
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys

# Lê toda a entrada e separa em números (em formato de texto)
dados = sys.stdin.read().split()
# A primeira parte é N, a quantidade de casos de teste
n = int(dados[0])
# Posição atual de leitura (logo após o N)
pos = 1
# Lista que guarda o texto de saída de cada caso de teste
blocos = []

# Repete para cada caso de teste
for _ in range(n):
    # M = quantidade de endereços-base da tabela
    m = int(dados[pos])
    # C = quantidade de chaves a serem inseridas
    c = int(dados[pos + 1])
    # Avança duas posições
    pos += 2
    # Cria a tabela: M listas vazias, uma para cada endereço
    tabela = [[] for _ in range(m)]
    # Insere as C chaves
    for _ in range(c):
        # Lê a chave
        chave = int(dados[pos])
        # Avança para a próxima chave
        pos += 1
        # Calcula o endereço com a função de dispersão h(x) = x mod M
        endereco = chave % m
        # Coloca a chave no final da lista daquele endereço (encadeamento)
        tabela[endereco].append(chave)
    # Lista com as linhas de saída deste caso
    linhas_saida = []
    # Percorre todos os endereços de 0 até M-1
    for i in range(m):
        # Começa a linha com o número do endereço e a seta
        texto = str(i) + ' -> '
        # Percorre as chaves guardadas nesse endereço, na ordem de inserção
        for chave in tabela[i]:
            # Acrescenta a chave e mais uma seta
            texto += str(chave) + ' -> '
        # Termina a linha com a barra invertida (\\ vira uma única \)
        texto += '\\'
        # Guarda a linha pronta
        linhas_saida.append(texto)
    # Junta as linhas deste caso e guarda como um bloco
    blocos.append('\n'.join(linhas_saida))

# Imprime os blocos separados por uma linha em branco
print('\n\n'.join(blocos))
