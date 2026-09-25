# =============================================================================
# Atividade 12 - Lista Telefônica Econômica (beecrowd 1211)
# -----------------------------------------------------------------------------
# Ideia: ordenando os telefones em ordem alfabética, números com prefixos
# parecidos ficam vizinhos. A economia máxima é a soma, para cada telefone a
# partir do segundo, do tamanho do prefixo comum com o telefone de cima.
# Exemplo: 535456, 535488, 835456 -> prefixos comuns 4 ("5354") e 0 -> total 4.
# =============================================================================

# Importa o módulo sys para ler a entrada até o fim do arquivo (EOF)
import sys

# Lê toda a entrada e separa em partes (N e os telefones, como texto)
dados = sys.stdin.read().split()
# Posição atual de leitura dentro da lista de dados
pos = 0
# Lista com a resposta de cada caso de teste
saida = []

# Repete enquanto ainda houver dados (a entrada termina em EOF)
while pos < len(dados):
    # Lê N, a quantidade de telefones da lista
    n = int(dados[pos])
    # Avança a posição de leitura
    pos += 1
    # Pega os N telefones como texto (preserva zeros à esquerda)
    telefones = dados[pos:pos + n]
    # Avança a posição de leitura em N
    pos += n
    # Ordena os telefones em ordem alfabética (deixa prefixos iguais vizinhos)
    telefones.sort()
    # Total de caracteres economizados neste caso
    economia = 0
    # Percorre os telefones a partir do segundo
    for i in range(1, n):
        # Telefone impresso logo acima
        anterior = telefones[i - 1]
        # Telefone atual
        atual = telefones[i]
        # Contador do tamanho do prefixo em comum
        j = 0
        # Avança enquanto os dígitos na mesma posição forem iguais
        while j < len(atual) and anterior[j] == atual[j]:
            # Mais um dígito em comum
            j += 1
        # Os j dígitos iniciais não precisam ser impressos
        economia += j
    # Guarda a economia deste caso como texto
    saida.append(str(economia))

# Imprime as respostas, uma por linha
print('\n'.join(saida))
