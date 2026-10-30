# Uma agência possui uma fila de atendimento. Os clientes recebem um número de identificação no momento em que entram na fila.

# O sistema deverá realizar as seguintes operações:

# - 1 X → adiciona o cliente X ao final da fila;
# - 2 → atende o primeiro cliente da fila;
# - 3 → mostra quem é o próximo cliente;
# - 4 → mostra a quantidade de clientes aguardando;
# - 0 → encerra o programa.

# Restrições

# É obrigatório implementar uma Fila.
# A fila deverá obedecer ao princípio FIFO — First In, First Out.
# É proibido utilizar queue.Queue.
# É proibido utilizar collections.deque.
# É proibido utilizar pop(0).
# É proibido utilizar remove() para retirar clientes.
# A fila deverá ser implementada utilizando uma lista.
# O controle da posição do primeiro cliente deverá ser realizado por meio de um índice.
# O programa deverá possuir uma variável responsável por indicar o início da fila.
# O programa deverá possuir uma variável responsável por indicar a quantidade de clientes aguardando.
# Quando um cliente for atendido, ele não deverá ser deslocado individualmente utilizando pop(0).
# A operação 3 não poderá alterar a fila.
# A operação 4 deverá apresentar a quantidade atual de clientes aguardando.
# O sistema deverá tratar corretamente uma tentativa de atendimento quando a fila estiver vazia.
# O sistema deverá tratar corretamente uma consulta quando a fila estiver vazia.
# Não é permitido utilizar sort() ou sorted().
# Não é permitido utilizar max() ou min().
# Não é permitido utilizar classes.
# Não é permitido criar funções utilizando def.
# O programa deverá continuar executando até receber a operação 0.

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

