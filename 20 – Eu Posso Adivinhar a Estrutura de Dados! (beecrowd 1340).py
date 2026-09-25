# =============================================================================
# Atividade 20 - Eu Posso Adivinhar a Estrutura de Dados! (beecrowd 1340)
# -----------------------------------------------------------------------------
# Ideia: simular AO MESMO TEMPO as três estruturas (pilha, fila e fila de
# prioridade) com os mesmos comandos. No comando "2 x", cada estrutura
# remove o seu elemento; se ela estiver vazia ou o elemento removido não for
# o x esperado, essa estrutura é descartada. No fim, contamos quantas
# estruturas continuam possíveis.
# =============================================================================

# Importa o módulo sys para ler a entrada até o fim do arquivo (EOF)
import sys
# Importa o deque, uma fila que remove do início de forma rápida
from collections import deque
# Importa o heapq, que implementa uma fila de prioridade (heap)
import heapq

# Lê toda a entrada e separa em números (em formato de texto)
dados = sys.stdin.read().split()
# Posição atual de leitura dentro da lista de dados
pos = 0
# Lista com as respostas de cada caso de teste
saida = []

# Repete enquanto ainda houver dados (a entrada termina em EOF)
while pos < len(dados):
    # Lê n, a quantidade de comandos do caso de teste
    n = int(dados[pos])
    # Avança a posição de leitura
    pos += 1
    # Pilha simulada (último que entra é o primeiro que sai)
    pilha = []
    # Fila simulada (primeiro que entra é o primeiro que sai)
    fila = deque()
    # Fila de prioridade simulada (sai sempre o maior elemento)
    prioridade = []
    # Indica se ainda pode ser uma pilha
    pode_pilha = True
    # Indica se ainda pode ser uma fila
    pode_fila = True
    # Indica se ainda pode ser uma fila de prioridade
    pode_prioridade = True
    # Executa os n comandos
    for _ in range(n):
        # Tipo do comando: 1 (inserir) ou 2 (remover)
        tipo = int(dados[pos])
        # Valor x que acompanha o comando
        x = int(dados[pos + 1])
        # Avança duas posições (tipo e x)
        pos += 2
        # Se o comando é de inserção
        if tipo == 1:
            # Coloca x no topo da pilha
            pilha.append(x)
            # Coloca x no fim da fila
            fila.append(x)
            # Coloca -x no heap (o heapq tira o MENOR, então -x faz sair o maior)
            heapq.heappush(prioridade, -x)
        # Se o comando é de remoção (e o elemento retirado foi x)
        else:
            # Só testa a pilha se ela ainda for uma possibilidade
            if pode_pilha:
                # Se a pilha está vazia ou o topo retirado não é x...
                if len(pilha) == 0 or pilha.pop() != x:
                    # ...não pode ser uma pilha
                    pode_pilha = False
            # Só testa a fila se ela ainda for uma possibilidade
            if pode_fila:
                # Se a fila está vazia ou o primeiro retirado não é x...
                if len(fila) == 0 or fila.popleft() != x:
                    # ...não pode ser uma fila
                    pode_fila = False
            # Só testa a fila de prioridade se ela ainda for uma possibilidade
            if pode_prioridade:
                # Se está vazia ou o maior retirado não é x (desfaz o sinal com -)...
                if len(prioridade) == 0 or -heapq.heappop(prioridade) != x:
                    # ...não pode ser uma fila de prioridade
                    pode_prioridade = False
    # Conta quantas estruturas continuam possíveis (True vale 1, False vale 0)
    possiveis = pode_pilha + pode_fila + pode_prioridade
    # Nenhuma estrutura serve
    if possiveis == 0:
        # Guarda a resposta "impossible"
        saida.append('impossible')
    # Mais de uma estrutura serve
    elif possiveis > 1:
        # Guarda a resposta "not sure"
        saida.append('not sure')
    # Só a pilha serve
    elif pode_pilha:
        # Guarda a resposta "stack"
        saida.append('stack')
    # Só a fila serve
    elif pode_fila:
        # Guarda a resposta "queue"
        saida.append('queue')
    # Só a fila de prioridade serve
    else:
        # Guarda a resposta "priority queue"
        saida.append('priority queue')

# Imprime as respostas, uma por linha
print('\n'.join(saida))