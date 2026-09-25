# =============================================================================
# Atividade 02 - Compactador de Arquivos (Professor Francisco)
# -----------------------------------------------------------------------------
# Ideia: percorrer a linha procurando sequências seguidas de '0' ou de ' '.
#  - Sequência de zeros   -> vira '#' + o caractere ASCII da quantidade.
#  - Sequência de espaços -> vira '$' + o caractere ASCII da quantidade.
#  - Sequências de 1 ou 2 caracteres NÃO são compactadas (não economizam nada).
#  - Se a sequência passar de 255, é dividida em blocos de 255 (ex.: 380 zeros
#    viram '#' + chr(255) + '#' + chr(125)).
# A leitura e a escrita são feitas em BYTES, porque a quantidade é gravada como
# um caractere da tabela ASCII (0 a 255) e precisa sair como 1 único byte.
# =============================================================================

# Importa o módulo sys para ler e escrever bytes diretamente
import sys

# Guarda o código ASCII do caractere '0' (zero), que é 48
ZERO = ord('0')
# Guarda o código ASCII do espaço em branco ' ', que é 32
ESPACO = ord(' ')
# Guarda o código ASCII do símbolo '#', usado para compactar zeros
SIMBOLO_ZERO = ord('#')
# Guarda o código ASCII do símbolo '$', usado para compactar espaços
SIMBOLO_ESPACO = ord('$')

# Lê toda a entrada de uma vez, em bytes, e separa em uma lista de linhas
linhas = sys.stdin.buffer.read().split(b'\n')
# A primeira linha contém N, a quantidade de casos de teste
n = int(linhas[0])
# Lista que vai guardar a linha compactada de cada caso de teste
saida = []

# Repete para cada caso de teste (linhas 1 até N)
for i in range(1, n + 1):
    # Pega a linha do caso; se o arquivo terminou antes, usa uma linha vazia
    linha = linhas[i] if i < len(linhas) else b''
    # Remove o '\r' do final (aparece em arquivos criados no Windows)
    linha = linha.rstrip(b'\r')
    # Cria um vetor de bytes vazio para montar a linha compactada
    resultado = bytearray()
    # Guarda o tamanho da linha original
    tamanho = len(linha)
    # Índice que percorre a linha original, começando no primeiro caractere
    j = 0
    # Continua enquanto não chegar ao fim da linha
    while j < tamanho:
        # Pega o código ASCII do caractere atual
        c = linha[j]
        # Verifica se o caractere atual é um zero ou um espaço
        if c == ZERO or c == ESPACO:
            # Começa a procurar o fim da sequência a partir da posição atual
            k = j
            # Avança k enquanto o caractere continuar igual ao primeiro
            while k < tamanho and linha[k] == c:
                # Vai para o próximo caractere
                k += 1
            # Calcula quantos caracteres iguais seguidos foram encontrados
            quantidade = k - j
            # Escolhe o símbolo: '#' para zeros ou '$' para espaços
            simbolo = SIMBOLO_ZERO if c == ZERO else SIMBOLO_ESPACO
            # Enquanto a quantidade for maior que 255 (limite de 1 byte)...
            while quantidade > 255:
                # ...grava o símbolo de compactação...
                resultado.append(simbolo)
                # ...seguido do caractere de código 255 (bloco cheio)
                resultado.append(255)
                # Desconta os 255 caracteres que já foram compactados
                quantidade -= 255
            # Se o que sobrou tem mais de 2 caracteres, vale a pena compactar
            if quantidade > 2:
                # Grava o símbolo de compactação
                resultado.append(simbolo)
                # Grava o caractere cujo código ASCII é a quantidade
                resultado.append(quantidade)
            # Se sobrou 1 ou 2 caracteres, não compensa compactar
            else:
                # Copia os caracteres originais sem alteração
                resultado.extend(bytes([c]) * quantidade)
            # Pula o índice para depois do fim da sequência tratada
            j = k
        # Se o caractere não é zero nem espaço
        else:
            # Copia o caractere para o resultado sem alteração
            resultado.append(c)
            # Avança para o próximo caractere
            j += 1
    # Guarda a linha compactada na lista de saída
    saida.append(bytes(resultado))

# Junta todas as linhas com '\n' e escreve os bytes na saída padrão
sys.stdout.buffer.write(b'\n'.join(saida) + b'\n')
