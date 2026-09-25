# =============================================================================
# Atividade 09 - Diga-me a Frequência (beecrowd 1251)
# -----------------------------------------------------------------------------
# Ideia: para cada linha, contar quantas vezes aparece cada código ASCII
# usando um dicionário. Depois ordenar por:
#  1) frequência em ordem crescente;
#  2) em caso de empate, código ASCII MAIOR primeiro.
# =============================================================================

# Importa o módulo sys para ler a entrada até o fim do arquivo (EOF)
import sys


# Função que diz ao sort como comparar dois pares (codigo, frequencia)
def chave(par):
    # Desmonta o par em código ASCII e frequência
    codigo, frequencia = par
    # Frequência crescente; -codigo faz o maior código vir primeiro no empate
    return (frequencia, -codigo)


# Lista que guarda o texto de saída de cada linha de entrada
blocos = []

# Percorre cada linha da entrada até acabar o arquivo (EOF)
for linha in sys.stdin:
    # Remove só a quebra de linha (espaços fazem parte do texto e são contados)
    texto = linha.rstrip('\r\n')
    # Se a linha estiver vazia, não há caracteres para contar
    if texto == '':
        # Pula para a próxima linha
        continue
    # Dicionário: código ASCII -> quantidade de vezes que aparece
    contagem = {}
    # Percorre cada caractere da linha
    for caractere in texto:
        # Converte o caractere para o seu código ASCII (ex.: 'A' -> 65)
        codigo = ord(caractere)
        # Soma 1 na contagem desse código (começa em 0 se ainda não existir)
        contagem[codigo] = contagem.get(codigo, 0) + 1
    # Transforma o dicionário em lista de pares e ordena com a função chave
    ordenado = sorted(contagem.items(), key=chave)
    # Lista com as linhas de saída desta linha de entrada
    linhas_saida = []
    # Percorre os pares já ordenados
    for codigo, frequencia in ordenado:
        # Monta a linha no formato "codigo frequencia"
        linhas_saida.append(str(codigo) + ' ' + str(frequencia))
    # Junta as linhas e guarda como um bloco
    blocos.append('\n'.join(linhas_saida))

# Imprime os blocos separados por uma linha em branco
print('\n\n'.join(blocos))
