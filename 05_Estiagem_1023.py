# =============================================================================
# Atividade 05 - Estiagem (beecrowd 1023)
# -----------------------------------------------------------------------------
# Ideia: para cada imóvel, o consumo por pessoa é Y // X (arredondado para
# baixo). Usamos um dicionário que soma quantas pessoas existem para cada
# valor de consumo. Depois imprimimos os consumos em ordem crescente.
# O consumo médio é (soma de Y) / (soma de X), mostrado com 2 casas decimais
# SEM arredondar (apenas cortando). Para evitar erros de ponto flutuante, a
# conta é feita com inteiros: (soma de Y * 100) // (soma de X).
# =============================================================================

# Importa o módulo sys para leitura rápida (N pode ser até 1 milhão)
import sys

# Lê toda a entrada de uma vez e separa em números (em formato de texto)
dados = sys.stdin.buffer.read().split()
# Posição atual de leitura dentro da lista de dados
pos = 0
# Contador do número da cidade (1, 2, 3, ...)
cidade = 0
# Lista que guarda o texto de saída de cada cidade
blocos = []

# Repete enquanto ainda houver dados para ler
while pos < len(dados):
    # Lê N, a quantidade de imóveis da cidade
    n = int(dados[pos])
    # Avança a posição de leitura
    pos += 1
    # N igual a zero indica o fim da entrada
    if n == 0:
        # Encerra o laço
        break
    # Passa para o número da próxima cidade
    cidade += 1
    # Dicionário: consumo por pessoa -> total de pessoas com esse consumo
    pessoas_por_consumo = {}
    # Soma de todos os moradores da cidade
    total_pessoas = 0
    # Soma de todo o consumo da cidade
    total_consumo = 0
    # Lê os N imóveis
    for _ in range(n):
        # X = quantidade de moradores do imóvel
        x = int(dados[pos])
        # Y = consumo total do imóvel em m3
        y = int(dados[pos + 1])
        # Avança duas posições (X e Y já foram lidos)
        pos += 2
        # Consumo por pessoa, arredondado para baixo (divisão inteira)
        consumo = y // x
        # Soma os X moradores no grupo desse consumo (começa em 0 se não existir)
        pessoas_por_consumo[consumo] = pessoas_por_consumo.get(consumo, 0) + x
        # Acumula o total de moradores da cidade
        total_pessoas += x
        # Acumula o consumo total da cidade
        total_consumo += y
    # Lista com os textos "pessoas-consumo" em ordem crescente de consumo
    partes = []
    # Percorre os consumos em ordem crescente
    for consumo in sorted(pessoas_por_consumo):
        # Monta o texto no formato "quantidade-consumo"
        partes.append(str(pessoas_por_consumo[consumo]) + '-' + str(consumo))
    # Média multiplicada por 100 e cortada (sem arredondar), usando só inteiros
    media_x100 = (total_consumo * 100) // total_pessoas
    # Parte inteira da média
    inteiro = media_x100 // 100
    # Duas casas decimais da média
    decimais = media_x100 % 100
    # Monta a primeira linha da saída da cidade
    linha1 = 'Cidade# ' + str(cidade) + ':'
    # Monta a segunda linha juntando as partes com espaço
    linha2 = ' '.join(partes)
    # Monta a terceira linha; '%02d' garante 2 dígitos nos decimais (ex.: 05)
    linha3 = 'Consumo medio: %d.%02d m3.' % (inteiro, decimais)
    # Guarda as três linhas desta cidade como um único bloco
    blocos.append(linha1 + '\n' + linha2 + '\n' + linha3)

# Imprime os blocos separados por uma linha em branco (sem linha extra no fim)
print('\n\n'.join(blocos))
