# =============================================================================
# Atividade 15 - A Fila de Desempregados (beecrowd 1119)
# -----------------------------------------------------------------------------
# Ideia: representar o círculo com uma lista de "vivo" (True = ainda no
# círculo). Dois ponteiros andam ao mesmo tempo:
#  - p1 anda no sentido horário (índice +1) contando K pessoas;
#  - p2 anda no sentido anti-horário (índice -1) contando M pessoas.
# Só contam as pessoas que ainda estão no círculo. As duas pessoas escolhidas
# saem juntas (só depois das duas contagens). Cada número é impresso com
# largura 3 ('%3d'); pares são separados por vírgula.
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys

# Lê toda a entrada e separa em números (em formato de texto)
dados = sys.stdin.read().split()
# Posição atual de leitura dentro da lista de dados
pos = 0
# Lista com a linha de resposta de cada caso
saida = []

# Repete enquanto houver pelo menos três números para ler
while pos + 2 < len(dados):
    # N = quantidade de candidatos no círculo
    n = int(dados[pos])
    # K = passos do oficial que anda no sentido horário
    k = int(dados[pos + 1])
    # M = passos do oficial que anda no sentido anti-horário
    m = int(dados[pos + 2])
    # Avança três posições
    pos += 3
    # "0 0 0" indica o fim da entrada
    if n == 0 and k == 0 and m == 0:
        # Encerra o laço
        break
    # Todos os N candidatos começam no círculo (índice 0 = pessoa 1)
    vivo = [True] * n
    # Quantidade de pessoas que ainda estão no círculo
    restantes = n
    # p1 começa "antes" da pessoa 1, para que o 1º passo caia nela
    p1 = n - 1
    # p2 começa "depois" da pessoa N, para que o 1º passo caia nela
    p2 = 0
    # Lista com os grupos escolhidos em cada rodada
    escolhidos = []
    # Repete até não sobrar ninguém no círculo
    while restantes > 0:
        # Contador de pessoas contadas pelo oficial do sentido horário
        contados = 0
        # Anda até contar K pessoas que ainda estão no círculo
        while contados < k:
            # Avança uma posição no sentido horário (volta ao 0 após o fim)
            p1 = (p1 + 1) % n
            # Só conta se a pessoa ainda estiver no círculo
            if vivo[p1]:
                # Mais uma pessoa contada
                contados += 1
        # Zera o contador para o oficial do sentido anti-horário
        contados = 0
        # Anda até contar M pessoas que ainda estão no círculo
        while contados < m:
            # Recua uma posição no sentido anti-horário (vai ao fim após o 0)
            p2 = (p2 - 1) % n
            # Só conta se a pessoa ainda estiver no círculo
            if vivo[p2]:
                # Mais uma pessoa contada
                contados += 1
        # Retira do círculo a pessoa escolhida pelo oficial do sentido horário
        vivo[p1] = False
        # Retira do círculo a pessoa escolhida pelo oficial do sentido anti-horário
        vivo[p2] = False
        # Se os dois escolheram a mesma pessoa
        if p1 == p2:
            # Imprime o número dela uma única vez (largura 3)
            escolhidos.append('%3d' % (p1 + 1))
            # Saiu apenas uma pessoa
            restantes -= 1
        # Se escolheram pessoas diferentes
        else:
            # Imprime o par: primeiro a do sentido horário (cada um com largura 3)
            escolhidos.append('%3d%3d' % (p1 + 1, p2 + 1))
            # Saíram duas pessoas
            restantes -= 2
    # Junta os grupos separados por vírgula (sem vírgula após o último)
    saida.append(','.join(escolhidos))

# Imprime as respostas, uma por linha
print('\n'.join(saida))
