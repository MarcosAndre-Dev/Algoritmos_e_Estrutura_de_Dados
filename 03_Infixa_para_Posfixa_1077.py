# =============================================================================
# Atividade 03 - Infixa para Posfixa (beecrowd 1077)
# -----------------------------------------------------------------------------
# Ideia: algoritmo clássico com PILHA de operadores.
#  - Letra ou número (operando): vai direto para a saída.
#  - '(' : é empilhado.
#  - ')' : desempilha para a saída tudo até encontrar o '(' correspondente.
#  - Operador: antes de empilhar, desempilha para a saída os operadores do
#    topo que têm prioridade MAIOR OU IGUAL à dele.
#  - No fim, tudo o que sobrou na pilha vai para a saída.
# Prioridades: ^ (3) > * / (2) > + - (1).
# =============================================================================

# Importa o módulo sys para ler a entrada inteira
import sys

# Dicionário com a prioridade de cada operador (maior número = resolve antes)
PRIORIDADE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# Lê todas as linhas, remove espaços das pontas e descarta linhas vazias
linhas = [l.strip() for l in sys.stdin.read().split('\n') if l.strip() != '']
# A primeira linha contém N, o número de expressões
n = int(linhas[0])

# Repete para cada uma das N expressões
for i in range(1, n + 1):
    # Pega a expressão infixa da linha atual
    expressao = linhas[i]
    # Pilha que guarda operadores e parênteses abertos
    pilha = []
    # Lista que vai montando a expressão posfixa
    saida = []
    # Percorre cada caractere da expressão
    for c in expressao:
        # Se for letra ou dígito, é um operando
        if c.isalnum():
            # Operandos vão direto para a saída
            saida.append(c)
        # Se for um parêntese que abre
        elif c == '(':
            # Empilha para marcar o início do grupo
            pilha.append(c)
        # Se for um parêntese que fecha
        elif c == ')':
            # Desempilha operadores até achar o '(' correspondente
            while len(pilha) > 0 and pilha[-1] != '(':
                # Cada operador desempilhado vai para a saída
                saida.append(pilha.pop())
            # Se ainda há algo na pilha, é o '('
            if len(pilha) > 0:
                # Remove o '(' (parênteses não aparecem na posfixa)
                pilha.pop()
        # Se for um dos operadores + - * / ^
        elif c in PRIORIDADE:
            # Enquanto o topo for operador com prioridade maior ou igual...
            while len(pilha) > 0 and pilha[-1] != '(' and PRIORIDADE[pilha[-1]] >= PRIORIDADE[c]:
                # ...desempilha esse operador para a saída
                saida.append(pilha.pop())
            # Depois empilha o operador atual
            pilha.append(c)
    # Ao terminar a expressão, esvazia o que restou na pilha
    while len(pilha) > 0:
        # Remove o elemento do topo
        topo = pilha.pop()
        # Só manda para a saída se não for parêntese
        if topo != '(':
            # Adiciona o operador na saída
            saida.append(topo)
    # Junta a lista em uma única string e imprime a expressão posfixa
    print(''.join(saida))
