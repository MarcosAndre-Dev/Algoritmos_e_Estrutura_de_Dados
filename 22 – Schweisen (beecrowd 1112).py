# =============================================================================
# Atividade 22 - Schweisen (beecrowd 1112)
# -----------------------------------------------------------------------------
# Ideia: usar uma ÁRVORE DE FENWICK 2D (Binary Indexed Tree), que permite:
#  - somar N em uma casa (X, Y) rapidamente;
#  - calcular a soma de um retângulo rapidamente.
# Somar célula por célula seria lento demais (campo de até 1000 x 1000 e até
# 10000 mensagens). A soma do retângulo sai por inclusão-exclusão:
#  soma(x1..x2, y1..y2) = S(x2,y2) - S(x1-1,y2) - S(x2,y1-1) + S(x1-1,y1-1)
# onde S(a,b) é a soma de todas as casas de (0,0) até (a,b).
# A árvore usa índices a partir de 1, por isso somamos 1 nas coordenadas.
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys


# Função que soma "valor" na casa (x, y) da árvore (x e y já começando em 1)
def atualizar(arvore, x, y, valor, largura, altura):
    # Começa pela linha x da árvore
    i = x
    # Percorre as linhas da árvore que "cobrem" a linha x
    while i <= largura:
        # Começa pela coluna y da árvore
        j = y
        # Percorre as colunas da árvore que "cobrem" a coluna y
        while j <= altura:
            # Soma o valor nesse nó da árvore
            arvore[i][j] += valor
            # Pula para o próximo nó responsável (soma o último bit 1 de j)
            j += j & (-j)
        # Pula para a próxima linha responsável (soma o último bit 1 de i)
        i += i & (-i)


# Função que devolve a soma de todas as casas de (1,1) até (x, y)
def soma_prefixo(arvore, x, y):
    # Acumulador da soma
    total = 0
    # Começa pela linha x da árvore
    i = x
    # Desce pelas linhas enquanto o índice for válido
    while i > 0:
        # Começa pela coluna y da árvore
        j = y
        # Desce pelas colunas enquanto o índice for válido
        while j > 0:
            # Soma o valor guardado nesse nó
            total += arvore[i][j]
            # Vai para o nó anterior (remove o último bit 1 de j)
            j -= j & (-j)
        # Vai para a linha anterior (remove o último bit 1 de i)
        i -= i & (-i)
    # Devolve a soma calculada
    return total


# Lê toda a entrada e separa em partes (letras e números)
dados = sys.stdin.read().split()
# Posição atual de leitura dentro da lista de dados
pos = 0
# Lista com as linhas de saída
saida = []

# Repete enquanto houver pelo menos três valores para ler
while pos + 2 < len(dados):
    # Largura do campo
    largura = int(dados[pos])
    # Altura do campo
    altura = int(dados[pos + 1])
    # Preço de cada deswevileutssen
    preco = int(dados[pos + 2])
    # Avança três posições
    pos += 3
    # X, Y e P iguais a 0 indicam o fim da entrada
    if largura == 0 and altura == 0 and preco == 0:
        # Encerra o laço
        break
    # Lê Q, a quantidade de mensagens
    q = int(dados[pos])
    # Avança a posição de leitura
    pos += 1
    # Cria a árvore zerada, com uma linha e uma coluna a mais (índice 0 não é usado)
    arvore = [[0] * (altura + 1) for _ in range(largura + 1)]
    # Processa as Q mensagens
    for _ in range(q):
        # Tipo da mensagem: 'A' (achei) ou 'P' (pergunta)
        tipo = dados[pos]
        # Se Conan encontrou schweisen
        if tipo == 'A':
            # Quantidade de schweisen encontradas
            n = int(dados[pos + 1])
            # Coordenada X da casa (somamos 1 porque a árvore começa em 1)
            x = int(dados[pos + 2]) + 1
            # Coordenada Y da casa (somamos 1 porque a árvore começa em 1)
            y = int(dados[pos + 3]) + 1
            # Avança quatro posições (A, N, X, Y)
            pos += 4
            # Soma as N schweisen na casa (x, y)
            atualizar(arvore, x, y, n, largura, altura)
        # Se Conan perguntou o custo de uma área
        else:
            # Lê o primeiro canto (X, Y) do retângulo
            xa = int(dados[pos + 1]) + 1
            # Coordenada Y do primeiro canto
            ya = int(dados[pos + 2]) + 1
            # Lê o segundo canto (Z, W) do retângulo
            xb = int(dados[pos + 3]) + 1
            # Coordenada W do segundo canto
            yb = int(dados[pos + 4]) + 1
            # Avança cinco posições (P, X, Y, Z, W)
            pos += 5
            # Menor X do retângulo (os cantos podem vir em qualquer ordem)
            x1 = min(xa, xb)
            # Maior X do retângulo
            x2 = max(xa, xb)
            # Menor Y do retângulo
            y1 = min(ya, yb)
            # Maior Y do retângulo
            y2 = max(ya, yb)
            # Soma do retângulo por inclusão-exclusão das somas de prefixo
            quantidade = (soma_prefixo(arvore, x2, y2)
                          - soma_prefixo(arvore, x1 - 1, y2)
                          - soma_prefixo(arvore, x2, y1 - 1)
                          + soma_prefixo(arvore, x1 - 1, y1 - 1))
            # Custo total = quantidade de schweisen vezes o preço
            saida.append(str(quantidade * preco))
    # Linha em branco após cada caso de teste (inclusive o último)
    saida.append('')

# Imprime todas as linhas de saída
print('\n'.join(saida))