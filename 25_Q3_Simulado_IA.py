import sys
first = 0
counter = 0

fila_atendimento = []

while True:

    programa = input().split()

    if not programa:
        continue

    comparacao = int(programa[0])

    if comparacao == 0:
        break
    elif comparacao == 1:
        fila_atendimento.append(int(programa[-1]))
        counter += 1
    elif comparacao == 2:
        if first < counter:
            atendimento = fila_atendimento[first]
            first += 1
            print(atendimento)
        else:
            print("Nenhuma senha para atender")
    elif comparacao == 3:
        if first < counter:
            atendimento = fila_atendimento[first]
            first += 1
        else:
            print("Nenhuma senha para cancelar")
    elif comparacao == 4:
        if first < counter:
            atendimento = fila_atendimento[first]
            print(atendimento)
        else:
            print("Fila vazia! ")
    elif comparacao == 5:
        qtd_clientes = counter - first
        print(qtd_clientes)
