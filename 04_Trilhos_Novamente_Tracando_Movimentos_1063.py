# =============================================================================
# Atividade 04 - Trilhos Novamente... Traçando Movimentos (beecrowd 1063)
# -----------------------------------------------------------------------------
# Ideia: a estação funciona como uma PILHA (o último vagão que entra é o
# primeiro que sai). Para cada vagão da saída desejada:
#  - enquanto o topo da pilha não for esse vagão e ainda houver vagões
#    chegando pelo lado A, empilha o próximo vagão ('I' = insere);
#  - se o topo for o vagão desejado, desempilha ('R' = remove);
#  - senão, é impossível obter a saída desejada.
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys

# Lê toda a entrada e separa em "palavras" (números e letras dos vagões)
dados = sys.stdin.read().split()
# Posição atual de leitura dentro da lista de dados
pos = 0

# Repete enquanto ainda houver dados para ler
while pos < len(dados):
    # Lê N, a quantidade de vagões
    n = int(dados[pos])
    # Avança a posição de leitura
    pos += 1
    # N igual a zero indica o fim da entrada
    if n == 0:
        # Encerra o laço
        break
    # Pega os N vagões na ordem em que chegam pelo lado A
    entrada = dados[pos:pos + n]
    # Avança a posição de leitura em N
    pos += n
    # Pega os N vagões na ordem em que devem sair pelo lado B
    desejada = dados[pos:pos + n]
    # Avança a posição de leitura em N
    pos += n
    # Pilha que representa os vagões parados dentro da estação
    pilha = []
    # Lista com a sequência de movimentos ('I' e 'R')
    movimentos = []
    # Índice do próximo vagão que ainda vai chegar pelo lado A
    proximo = 0
    # Indica se foi possível montar a saída desejada (começa como verdadeiro)
    possivel = True
    # Percorre cada vagão na ordem em que ele deve sair
    for vagao in desejada:
        # Enquanto o topo não for o vagão procurado e ainda houver vagões chegando
        while (len(pilha) == 0 or pilha[-1] != vagao) and proximo < n:
            # Coloca o próximo vagão da entrada dentro da estação
            pilha.append(entrada[proximo])
            # Passa para o vagão seguinte da entrada
            proximo += 1
            # Registra o movimento de inserção
            movimentos.append('I')
        # Se o topo da pilha é o vagão que precisa sair agora
        if len(pilha) > 0 and pilha[-1] == vagao:
            # Tira o vagão da estação em direção ao lado B
            pilha.pop()
            # Registra o movimento de remoção
            movimentos.append('R')
        # Se o vagão não está no topo e não há mais vagões para entrar
        else:
            # Marca que a saída desejada é impossível
            possivel = False
            # Interrompe as operações
            break
    # Junta os movimentos em uma única string
    resultado = ''.join(movimentos)
    # Se não foi possível completar a saída
    if not possivel:
        # Acrescenta um espaço e a palavra "Impossible"
        resultado += ' Impossible'
    # Imprime a sequência de movimentos deste caso
    print(resultado)
