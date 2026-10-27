fila = []
primeiro_fila = 0
counter = 0
while True:
#Aqui começo a repetição.

    programa = input().split()
    #Lendo o que o usuário digitar

    if not programa:
        continue
    #Este if serve para casos do usuário digitar um enter sem nada, o programa irá continuar

    comparacao = int(programa[0])
    #Estou tranformando o primeiro str em inteiro para fazer a comparação no while

    if comparacao == 0:
        break
    elif comparacao == 1:
        fila.append(int(programa[-1]))
        counter += 1
    elif comparacao == 2:
        if primeiro_fila < counter:
            atendimento = fila[primeiro_fila]
            primeiro_fila += 1
    elif comparacao == 3:
        if primeiro_fila < counter:
            atendimento = fila[primeiro_fila]
            print(atendimento)
        else:
            print("Próxima fila vazia")
    elif comparacao == 4:
        qtd_clientes = counter - primeiro_fila
        if qtd_clientes == 0:
            print("Fila vazia")
        else:
            print(qtd_clientes)

