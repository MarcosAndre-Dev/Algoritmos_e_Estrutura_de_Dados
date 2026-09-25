# =============================================================================
# Atividade 18 - Balanço de Parênteses I (beecrowd 1068)
# -----------------------------------------------------------------------------
# Ideia: usar um contador de parênteses abertos (uma pilha simplificada).
#  - '(' soma 1;
#  - ')' subtrai 1; se ficar negativo, fechou sem ter aberto -> incorreto.
# No final, a expressão só está correta se o contador voltar a zero.
# =============================================================================

# Importa o módulo sys para ler a entrada até o fim do arquivo (EOF)
import sys

# Percorre cada linha da entrada até acabar o arquivo (EOF)
for linha in sys.stdin:
    # Remove espaços e a quebra de linha das pontas
    expressao = linha.strip()
    # Se a linha estiver vazia, não é uma expressão
    if expressao == '':
        # Pula para a próxima linha
        continue
    # Quantidade de parênteses abertos ainda não fechados
    abertos = 0
    # Indica se a expressão está correta (começa como verdadeiro)
    correta = True
    # Percorre cada caractere da expressão
    for c in expressao:
        # Se for um parêntese que abre
        if c == '(':
            # Soma um parêntese aberto
            abertos += 1
        # Se for um parêntese que fecha
        elif c == ')':
            # Fecha um dos parênteses abertos
            abertos -= 1
            # Se ficou negativo, fechou um parêntese que nunca foi aberto
            if abertos < 0:
                # Marca a expressão como incorreta
                correta = False
                # Não precisa olhar o resto da expressão
                break
    # Se sobrou parêntese aberto sem fechar, também está incorreta
    if abertos != 0:
        # Marca a expressão como incorreta
        correta = False
    # Imprime "correct" se estiver certa, ou "incorrect" caso contrário
    print('correct' if correta else 'incorrect')
