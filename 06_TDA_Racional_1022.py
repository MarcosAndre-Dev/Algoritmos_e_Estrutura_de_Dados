# =============================================================================
# Atividade 06 - TDA Racional (beecrowd 1022)
# -----------------------------------------------------------------------------
# Ideia: ler as duas frações e o operador, calcular o numerador e o
# denominador do resultado usando as fórmulas do enunciado e depois
# simplificar dividindo ambos pelo MDC (máximo divisor comum).
# Cada linha tem 7 partes: N1 / D1 op N2 / D2
# =============================================================================

# Importa o módulo sys para ler a entrada
import sys
# Importa a função gcd, que calcula o MDC de dois números
from math import gcd

# Lê toda a entrada e separa em partes (números, barras e operadores)
dados = sys.stdin.read().split()
# A primeira parte é N, a quantidade de casos de teste
n = int(dados[0])
# Posição atual de leitura (logo após o N)
pos = 1
# Lista com as linhas de resposta
saida = []

# Repete para cada caso de teste
for _ in range(n):
    # Numerador da primeira fração
    n1 = int(dados[pos])
    # Denominador da primeira fração (dados[pos+1] é a barra '/')
    d1 = int(dados[pos + 2])
    # Operador da conta: '+', '-', '*' ou '/'
    op = dados[pos + 3]
    # Numerador da segunda fração
    n2 = int(dados[pos + 4])
    # Denominador da segunda fração (dados[pos+5] é a barra '/')
    d2 = int(dados[pos + 6])
    # Avança 7 posições para o próximo caso de teste
    pos += 7
    # Se a operação é soma
    if op == '+':
        # Numerador da soma: N1*D2 + N2*D1
        num = n1 * d2 + n2 * d1
        # Denominador da soma: D1*D2
        den = d1 * d2
    # Se a operação é subtração
    elif op == '-':
        # Numerador da subtração: N1*D2 - N2*D1
        num = n1 * d2 - n2 * d1
        # Denominador da subtração: D1*D2
        den = d1 * d2
    # Se a operação é multiplicação
    elif op == '*':
        # Numerador da multiplicação: N1*N2
        num = n1 * n2
        # Denominador da multiplicação: D1*D2
        den = d1 * d2
    # Se a operação é divisão
    else:
        # Numerador da divisão: N1*D2
        num = n1 * d2
        # Denominador da divisão: N2*D1
        den = n2 * d1
    # Calcula o MDC entre numerador e denominador (sempre positivo)
    mdc = gcd(num, den)
    # Divide o numerador pelo MDC para simplificar (mantém o sinal)
    num_simples = num // mdc
    # Divide o denominador pelo MDC para simplificar
    den_simples = den // mdc
    # Monta a linha: "resultado = resultado simplificado"
    saida.append(str(num) + '/' + str(den) + ' = ' + str(num_simples) + '/' + str(den_simples))

# Imprime todas as respostas, uma por linha
print('\n'.join(saida))
