# =============================================================================
# Atividade 01 - Ácido Ribonucleico Alienígena (beecrowd 1242)
# -----------------------------------------------------------------------------
# Ideia: usar uma PILHA. Cada base lida é comparada com a base do topo da pilha.
# Se as duas formam par (B com S, ou C com F), elas se ligam: tiramos o topo da
# pilha e contamos 1 ligação. Se não formam par, a base é empilhada e espera
# um par que ainda pode aparecer mais à frente na fita.
# =============================================================================

# Importa o módulo sys, usado para ler a entrada até o fim do arquivo (EOF)
import sys

# Dicionário que informa qual é o par de cada base (B<->S e C<->F)
PAR = {'B': 'S', 'S': 'B', 'C': 'F', 'F': 'C'}

# Percorre cada linha da entrada, uma por vez, até acabar o arquivo (EOF)
for linha in sys.stdin:
    # Remove espaços e a quebra de linha ('\n') das pontas da linha lida
    fita = linha.strip()
    # Se a linha ficou vazia, ela não é um caso de teste
    if fita == '':
        # Pula direto para a próxima linha
        continue
    # Cria uma pilha vazia para guardar as bases que ainda não se ligaram
    pilha = []
    # Começa o contador de ligações deste caso de teste em zero
    ligacoes = 0
    # Percorre cada base da fita, da esquerda para a direita
    for base in fita:
        # Verifica se a pilha tem algo E se o topo é o par da base atual
        if len(pilha) > 0 and pilha[-1] == PAR[base]:
            # As duas bases se ligaram: remove a base do topo da pilha
            pilha.pop()
            # Soma 1 ao total de ligações
            ligacoes += 1
        # Se a pilha está vazia ou o topo não é o par da base atual
        else:
            # Empilha a base atual para tentar ligá-la mais tarde
            pilha.append(base)
    # Imprime o total de ligações encontradas nesta fita
    print(ligacoes)
